# Input: 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

num = int(input("Enter the number: "))
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()