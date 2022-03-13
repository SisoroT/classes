low, high = 0, 0
response = ""

range_of_nums = int(input("Enter a number: "))
while range_of_nums < 1:
    range_of_nums = int(input("Please enter a positive integer: "))

high = range_of_nums

# asks user to pick a number between 0 and n-1
print(
    f"Welcome to Guess My Number!\nPlease think of a number between 0 and {range_of_nums - 1}."
)

# computer will continue to guess the midpoint of the
# available numbers until the correct answer is given
while response.lower() != "C".lower():
    guess = (low + high) // 2
    print(f"Is your number: {guess}?")
    print("Please enter C for correct, H for too high, or L for too low.")
    response = input("Enter your response (H/L/C): ")

    # if the user's number is higher than the made guess, low becomes guess+1
    if response.lower() == "h":
        low = guess + 1
    # if the user's number is higher than the made guess, low becomes guess+1
    if response.lower() == "l":
        high = guess - 1
    # if the user's number matches the made guess the game ends
    if response.lower() == "c":
        print("Thank you for playing Guess my Number!")
