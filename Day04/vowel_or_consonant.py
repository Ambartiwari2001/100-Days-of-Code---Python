# Write a program that takes a single character as input and checks if it's a vowel or consonant. 
# If it's not an alphabet, print "Invalid input".

# Expected Output:

# Input:
# Enter a character: a

# Output:
# a is a vowel.

# Input:
# Enter a character: z

# Output:
# z is a consonant.

# Input:
# Enter a character: 3

# Output:
# Invalid input

char = input("Enter a character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input")