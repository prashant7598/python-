a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if( a > b  and a>c ):
    print("first number is greatest")
elif(b > a and b > c):
    print("second number is greatest")
else:
    print("third number is greatest")
