# Write a program to find the sum of first n natural numbers using while loop. 

n = int(input("enter a number"))
i = 0
total = 0
while( i <= n):
    total += i
    i+= 1
print("the sum is", total)