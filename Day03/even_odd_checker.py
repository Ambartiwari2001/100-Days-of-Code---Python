#Write a Python program that asks the user to enter a number and tells if it is even or odd.

# Expected Output:
# Enter a number: 7
# Output: Odd Number


num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")