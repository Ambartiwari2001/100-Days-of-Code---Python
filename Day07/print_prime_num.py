# Q3. Print All Prime Numbers from 1 to N
# makefile
# Copy
# Edit
# Input: 20
# Output: 2 3 5 7 11 13 17 19

num = int(input("Enter the number: "))

for i in range(2, num + 1):    
    for j in range(2, i):
        if i % j == 0:
            break             
    else:
        print(i, end=" ")  