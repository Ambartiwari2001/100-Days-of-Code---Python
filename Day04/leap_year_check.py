# Write a Python program that takes a year as input from the user and checks whether it is a leap year or not.

# A leap year is:

# Divisible by 4

# But NOT divisible by 100

# Unless it is also divisible by 400

# Your program should:

# Take input from the user

# Apply the leap year logic

# Print whether the year is a leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
