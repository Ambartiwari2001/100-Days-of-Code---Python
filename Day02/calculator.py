#print for simple calculator

print("simple calculator")

# let's get for first input 

num1= int(input("enter first number : "))

# let's get for second input 

num2= int(input("enter second number : "))

#print for choose operation : 

print("Choose operation: +  -  *  / : ")

operation = input("enter the operation : ")


if operation == '+':
    print("Result : " , num1 + num2)
elif operation == '-':
    print("Result : ", num1 - num2)
elif operation == '*':
    print("Result : ", num1 * num2)
elif operation == '/':
    if num2 != 0:
          print("Result : ", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")   
