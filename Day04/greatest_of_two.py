#Write a Python program that takes two numbers as input from the user and prints which number is greater, or if both are equal.

# Expected Output:
# Input:
# Enter first number: 45
# Enter second number: 23

# Output:
# First number is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1 , "is greater for" , num2)
elif num1 == num2:
    print("both value is same. ")
else:
    print(num2 , "is greater for" , num1)