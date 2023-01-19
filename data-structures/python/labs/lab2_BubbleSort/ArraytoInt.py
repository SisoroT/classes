year = ""
arr = [1, 9, 8, 9]

# add each number to an empty string
for i in arr:
    year += str(i)

# convert the string back to an integer
year = int(year)

# print the integer year and year + 1
print(year, year + 1)
