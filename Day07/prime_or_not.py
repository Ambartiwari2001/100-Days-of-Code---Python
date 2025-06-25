# Q1. Check Prime Number or not 

num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, num):
            if num % i== 0:
                print(num, "is not a prime number.")
                break

    else:
       print(num , "is prime number.")
         
else:
    print(num, "is not a prime number.")