#Write a program to calculate the factorial of a number entered by the user.

# Input: 5
# Output: 120 (Because 5*4*3*2*1 = 120)

num = int(input("Enter the number: "))
result = 1

while num >= 1:
    result = result * num
    num-=1

print("Result: ", result)