# Program: Count Alphabets, Digits, and Special Characters from a String

input_string = input("Enter a string: ")
letters = 0
digits = 0
special = 0

for ch in input_string:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1


print("Alphabets: ", letters)
print("Digits: ", digits)
print("Special Characters: ", special)