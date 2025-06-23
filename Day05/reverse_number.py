#  Q3: Reverse the Digits of a Number
# expected output 
# Input:
# Enter number: 1234

# Output:
# Reversed number: 4321

num = int(input("Enter number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(f"Reverse number for {original} is : {rev}")


