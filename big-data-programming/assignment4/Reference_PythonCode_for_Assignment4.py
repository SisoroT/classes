from os import truncate
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DoubleType
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.functions import isnull, when, count, col
from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.appName("Iris Data").getOrCreate()


# loading IRIS dataset
dataset = spark.read.format("csv").option("header", "true").load("Iris.csv")

dataset.show(20)

# required vector transformation to get a dependent column based on independent columns
# here, the dependent column is species
# converting the data type to double before applying vector transformations
dataset = dataset.withColumn(
    "SepalLengthCm", dataset["SepalLengthCm"].cast(DoubleType())
)
dataset = dataset.withColumn("SepalWidthCm", dataset["SepalWidthCm"].cast(DoubleType()))
dataset = dataset.withColumn(
    "PetalLengthCm", dataset["PetalLengthCm"].cast(DoubleType())
)
dataset = dataset.withColumn("PetalWidthCm", dataset["PetalWidthCm"].cast(DoubleType()))

# displaying the dataset upto 20 records
dataset.show(20)

# Assigning the set of columns as input (required features)
# output column as features
required_features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
vectorAssembler = VectorAssembler(inputCols=required_features, outputCol="features")

# Joining them to a single column using VectorAssembler
dataset2 = vectorAssembler.transform(dataset)
dataset2.show(20)

# So, as we got the feature column , we can drop the independent colums (un necessary now)
df = dataset2.drop("SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm")
df.show(3)

# converting text to index value using stringindexer
# (like 0 or 1)
dataset3 = StringIndexer(inputCol="Species", outputCol="Group")

# Updated values is now set to our current dataset and transformed to binary data
df = dataset3.fit(df).transform(df)
df.show(3)

# Here, we are using 80% for training and 20% for testing stage
(trainingData, testData) = df.randomSplit([0.8, 0.2])

# using decision tree classifier feeding the data to classifier
dec_tree = DecisionTreeClassifier(labelCol="Group", featuresCol="features")

# Training the model
model = dec_tree.fit(trainingData)

# Feed test data to the model and prediction results are generated.
predictions = model.transform(testData)

# select example rows to display
# Select (prediction, true label) and compute test error.
predictions.select("prediction", "Group").show(5)

evaluator = MulticlassClassificationEvaluator(
    labelCol="Group", predictionCol="prediction", metricName="accuracy"
)

# Evaluate model on training instances
accuracy = evaluator.evaluate(predictions)

# Finding accuracy using classification evaluator function
print("Test Accuracy of Decision Tree =", accuracy)
