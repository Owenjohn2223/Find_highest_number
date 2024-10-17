# Finding_highest_number
numbers = input("Enter 5 numbers separated by spaces: ").split()

num1 = float(numbers[0])
num2 = float(numbers[1])
num3 = float(numbers[2])
num4 = float(numbers[3])
num5 = float(numbers[4])

# Assuming na the first number is the highest
highest = num1

# Compare the first to second number
if num2 > highest:
    highest = num2

# ...the third and the fourth number
if num3 > highest:
    highest = num3

if num4 > highest:
    highest = num4

# ...and the fith number
if num5 > highest:
    highest = num5

# Print off the highest number
print ("The highest number is:", highest)

