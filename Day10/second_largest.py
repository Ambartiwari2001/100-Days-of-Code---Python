"""
Day 10 – Python Program

❓ Question:
Write a Python program that takes a list of integers from the user and returns the **second largest** number in that list.

📌 Conditions:
- Do not use built-in sort() or max() functions.
- Your code should handle duplicate maximum values properly.
- It should also handle edge cases where the list is too short.

🔍 Example:
Input: 10 25 99 54 99
Output: 54
"""

def find_second_largest(arr):
    # If the list has fewer than 2 elements, there's no second largest
    if len(arr) < 2:
        return None

    # Initialize two variables to negative infinity (very small starting values)
    first = second = float('-inf')

    # Loop through each number in the list
    for num in arr:
        if num > first:
            # If current number is greater than the highest so far
            # Then update second to first, and first to current number
            second = first
            first = num
        elif num > second and num != first:
            # If current number is not the highest but greater than second highest
            # Then update second only
            second = num

    # If second never got updated (like all elements were equal), return None
    return second if second != float('-inf') else None


# 🔰 Take input from the user
user_input = input("Enter numbers separated by space: ")

# Convert the string input into a list of integers
# Example: "10 25 99" → [10, 25, 99]
arr = list(map(int, user_input.strip().split()))

# Call the function and store the result
result = find_second_largest(arr)

# Output the result based on what the function returns
if result is not None:
    print("Second largest number is:", result)
else:
    print("Second largest number not found (maybe all values are the same or only one number was entered).")

