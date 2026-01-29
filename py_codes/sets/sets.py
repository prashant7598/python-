# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    return a.intersection(b)
    

# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    # Your code here
    return a.difference(b)

# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    return a.union(b)
    
    
#User function Template for python3

# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    # Your code here
    return s.add(element)
    
# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Your code here
    return s.remove(element)
       
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    # Your code here
    return sum(s)
    
    