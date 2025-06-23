# Print the Multiplication Table of a Number
# expected output
# Input:
# Enter a number: 5

# Output:

# python-repl
# Copy
# Edit
# 5 x 1 = 5  
# 5 x 2 = 10  
# ...  
# 5 x 10 = 50

num = int(input("Enter the number: "))
i = 1

while i <= 10:
    print(num ,"x",i,"=",num*i)
    i+=1

