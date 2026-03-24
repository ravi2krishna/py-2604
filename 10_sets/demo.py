# Working With Sets 

# empty set 
empty_set = {} # empty curly braces are always dictionaries
print(empty_set)
print(type(empty_set))

# empty set 
empty_set = set()
print(empty_set)
print(type(empty_set))

# set with numeric data 
data = {10,20,30,40,50} # Unordered i.e order not preserved 
print(data)

data = set({10,20,30,40,50})
print(data)

# set with text data 
data = {"python","django","ai"}
print(data)

# set with mixed data 
data = {10,20,30,4.5,"python","django",True}
print(data)

# Accessing Data
data = {10,20,30,40,50}
print(data) # all data in set 

# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print(first_element)
# print(data[1:3:1]) # No Slicing Support 

# Access Individual Data -> 10k elements -> below is more efficient  
data = {10,20,30,40,50,10000}
for num in data:
    print(num)
    

# Apply Operators -> Req: Multiply Each Element with 10
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
    

# Apply Conditionals -> Req: Give me only even values
data = {10,20,35,40,55}
for num in data:
    if num % 2 == 0:
        print(num)
        
# Req: ["python","django","ai"] take these courses and return them as ["Python","Django","Ai"]
data = {"python","django","ai"}   
for course in data:
    print(course.title())

# Duplicates Not Allowed i.e removed
data = {10,20,20,10,30}
print(data)

# Insertion Order Not Preserved
data = {10,20,30,40,50}
print(data)

# Set Methods / Operations
print(dir(data))

# Frozenset 
data = frozenset({10,20,30,40,50})
print(data)
print(type(data))

data = frozenset({10,20,30,10,40,20,50})
print(data)
print(type(data))

# Frozenset Methods / Operations
print(dir(data))