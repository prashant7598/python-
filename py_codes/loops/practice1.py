# Q> Write a program to print multiplication table of a given number using for loop. 
a = int(input("enter a number"))

'''
for i in range(1,  11):
    print(i ,"*" , a, " = ", i*a )
'''

# to print in reverse order

for i in range(1, 11):
    print(f" {a} X {11- i} = {a*(11-i)}")