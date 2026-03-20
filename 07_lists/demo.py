# Working With Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# list with numeric data 
data = [10,20,30,40,50]
print(data)

data = list([10,20,30,40,50])
print(data)

# list with text data 
data = ["python","django","ai"]
print(data)

# list with mixed data 
data = [10,20,30,4.5,"python","django",True]
print(data)

# Accessing Data
data = [10,20,30,40,50]
print(data) # all data in list 

first_element = data[0]
print(first_element)

last_element = data[-1]
print(last_element)

# print(data[10]) # IndexError: list index out of range - same as strings
data = [10,20,30,40,50]
print(data)
print(data[1:3:1]) # 20, 30
print(data[0:5:2]) # 10, 30, 50

# Access Individual Data 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

# Access Individual Data -> 10k elements -> below is not efficient 
data = [10,20,30,40,50]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999])

# Access Individual Data -> 10k elements -> below is more efficient  
data = [10,20,30,40,50,10000]
for num in data:
    print(num)
    
# Apply Operators -> Req: Multiply Each Element with 10
data = [10,20,30,40,50]
for num in data:
    print(num * 10)
    
# Apply Conditionals -> Req: Give me only even values
data = [10,20,35,40,55]
for num in data:
    if num % 2 == 0:
        print(num)
   
# Req: ["python","django","ai"] take these courses and return them as ["Python","Django","Ai"]
data = ["python","django","ai"]   
for course in data:
    print(course.title())
        
# Duplicates Allowed 
data = [10,20,20,10,30]
print(data)

# Insertion Order Preserved
data = [10,20,20,10,30]
print(data)

# List Methods / Operations
print(dir(data))
