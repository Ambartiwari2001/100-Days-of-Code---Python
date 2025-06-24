# Input: 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

num = int(input("Enter the number: "))

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end=" ")
    for k in range (i):
        print("*", end=" ")
    print()

