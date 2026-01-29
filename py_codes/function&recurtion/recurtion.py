def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1) #here the function is calling itself 

n = int(input("enter a number"))

print(f"the factorial of given number is {factorial(n)}")