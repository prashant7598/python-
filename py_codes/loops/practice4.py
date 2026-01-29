# Write a program to calculate the factorial of a given number using for loop.

n = int(input("enter a number"))
total = 1
for i in range(1,n+1):
    total *= i
    i+= 1
print("the factorial is is", total)