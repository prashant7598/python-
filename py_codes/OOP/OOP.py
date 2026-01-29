class employee:
    
    salary = 12000 #this is an class attribute
    age = 19

    def getinfo(self):
        print(f" the salary is {self.salary}. the age is {self.age}")

    @staticmethod
    def greet():
        print("goodmorning") 

class constructor:
    def __init__(self, name, salary, age):
        print("I am creating an constructor")
        self.name = name
        self.salary = salary
        self.age = age

prash = employee() #this is an object attribute
prash.name ="prashant" 
print(prash.name, prash.age, prash.salary)

# here name is object attribute and salary, age are class attribute as they directly belong to the class
prash.greet()
prash.getinfo()

raj = constructor("raj gupte", 500 , 19)
print(raj.name, raj.salary, raj.age)
