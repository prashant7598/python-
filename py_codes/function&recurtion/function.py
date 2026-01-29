# function defination

def avg():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = int(input("enter third number"))

    avg = a+b+c/3
    print("the average is ", avg)
    return avg
#in python we can return or not return any values in our function defination, if we return any values then we can store it in any variable we created

def great(name, ending = "thanks"): #we can as many argument we want 
    print(f"hello {name}")
    print("hello", name)
    print(ending)




# function call

# avg()
# d = avg() 
# print(d )
great("prashant")# we can have any datatype here as input
great(5,"thank you") # agr hum kuch argument pass kre to wo argument ko lega aur ni kre toh jo def m diye h usko lega