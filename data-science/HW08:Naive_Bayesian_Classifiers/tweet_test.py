import csv
import pickle as pk
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

import util

# Read in the word list
with open("vocablist_tweet.pkl", "rb") as f:
    vocab_list = pk.load(f)

# Convert dictionary (str -> index) for faster lookup
vocab_lookup = {word: i for i, word in enumerate(vocab_list)}

pk_file = open("frequencies_tweet.pkl", "rb")

# Read in the log of the word and sentiment frequencies
log_word_frequencies, log_sentiment_frequencies = pk.load(pk_file)
log_word_frequencies = log_word_frequencies.T
log_sentiment_frequencies = log_sentiment_frequencies.T
sentiment_frequencies = np.exp(log_sentiment_frequencies)

assert log_word_frequencies.shape == (3, 2000), "log_word_frequecies is the wrong shape"
assert log_sentiment_frequencies.shape == (
    3,
), "log_sentiment_frequencies is the wrong shape"

# We should compare ourselves to some baseline
most_common_sentiment = np.argmax(sentiment_frequencies)
freq_of_most_common = sentiment_frequencies[most_common_sentiment]
print(
    f'Would get {freq_of_most_common * 100.0:.1f}% accuracy by guessing "{most_common_sentiment}" every time.'
)

# Gather ground truth and predictions
gt_sentiments = []
predicted_sentiments = []
prediction_confidences = []

# Step through the test.csv file
with open("test_tweet.csv", "r") as f:
    reader = csv.reader(f)

    skipped_tweet_count = 0
    for row in reader:

        # Check to see if the row has two entries
        if len(row) != 2:
            continue

        # Get the tweet and its ground truth sentiment
        tweet = row[0]
        sentiment = int(row[1])

        # Convert the tweet to a wordlist
        wordlist = util.str_to_list(tweet)

        # Convert the wordlist to a word_counts vector
        word_counts = util.counts_for_wordlist(wordlist, vocab_lookup)

        # Did this tweet have no common words?
        if word_counts is None:
            skipped_tweet_count += 1
            continue

        # Compute the log likelihoods for all three sentiments
        # (refer to the lecture) (It is a matrix times a vector)
        log_likelihoods = log_word_frequencies @ word_counts
        assert log_likelihoods.shape == (3,), "log_likelihoods is the wrong shape"

        # Add the log priors to the log_likelihoods to get the log_posteriors (unnormalized)
        log_posteriors = log_likelihoods + log_sentiment_frequencies

        # Get a prediction (0, 1 or 2)
        prediction = np.argmax(log_posteriors)

        # Move posterior out of "log space"
        unnormalized_posteriors = np.exp(log_posteriors - np.max(log_posteriors))

        # They must add up to 1, so normalize them
        normalized_posteriors = unnormalized_posteriors / np.sum(
            unnormalized_posteriors
        )

        # Get your confidence in the prediction
        confidence = normalized_posteriors[prediction]
        assert (
            confidence > 0.33
        ), "Confidence lower than 33 percent, there are only three sentiments"
        assert confidence <= 1.0, "Confidence is more than 100 percent."

        # Store the result in lists
        gt_sentiments.append(sentiment)
        predicted_sentiments.append(prediction)
        prediction_confidences.append(confidence)

print(f"Skipped {skipped_tweet_count} rows for having none of the common words")

# Convert gathered data into numpy arrays
gt = np.array(gt_sentiments)
predictions = np.array(predicted_sentiments)
confidence = np.array(prediction_confidences)

# Show some basic statistics
tweet_count = len(gt)
correct_count = np.sum(gt == predictions)
print(
    f"{tweet_count} lines analyzed, {correct_count} correct ({100.0 * correct_count/tweet_count:.1f}% accuracy)"
)
cm = confusion_matrix(gt, predictions)
print(f"Confusion: \n{cm}")

# Save out a confusion matrix plot
fig, ax = plt.subplots()
cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=util.labels)
cm_display.plot(ax=ax, cmap="Blues", colorbar=False)
fig.savefig("confusion_tweet.png")
print('Wrote confusion matrix as "confusion_tweet.png"')

# Plot how many you get right vs confidence thresholds
steps = 32
thresholds = np.linspace(0.33, 1.0, steps)
correct_ratio = np.zeros(steps)
confident_ratio = np.zeros(steps)

for i in range(steps):
    threshold = thresholds[i]
    confident = confidence >= threshold
    confident_sum = np.sum(confident)

    correct_ratio[i] = (
        np.sum(gt[confident] == predictions[confident]) / confident_sum
        if confident_sum > 0
        else 1
    )
    confident_ratio[i] = confident_sum / tweet_count

# Make a plot
fig, ax = plt.subplots()
ax.set_title("Confidence and Accuracy Are Correlated")
ax.plot(
    thresholds, correct_ratio, "blue", linewidth=0.8, label="Accuracy Above Threshold"
)
ax.set_xlabel("Confidence Threshold")
ax.yaxis.set_major_formatter(lambda x, pos: f"{x*100.0:.0f}%")
ax.hlines(
    freq_of_most_common,
    0.33,
    1,
    "blue",
    linestyle="dashed",
    linewidth=0.8,
    label=f"Accuracy Guessing {most_common_sentiment}",
)
ax.plot(
    thresholds,
    confident_ratio,
    "r",
    linestyle="dashed",
    linewidth=0.8,
    label="Tweets scoring above threshold",
)
ax.legend()
fig.savefig("confidence_tweet.png")
