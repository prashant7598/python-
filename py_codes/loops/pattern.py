n =  int(input("enter the number"))

'''
to print 
  *
 ***
***** for n = 3'''

# for i in range(1, n+1):
#     print(" "* (n - i), end="") #in python print statement give a new line to avoid this new line we use end=""
#     print("*"* (2*i -1))


'''
to print  
*
***
***** for n = 3
'''
# for i in range(1, n+1):
#     print("*"*(2*i - 1))

'''
to print 
***
* *
*** for n = 3 it is like a ring'''


for i in range(1, n+1):
    if(i ==1 or i == n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")