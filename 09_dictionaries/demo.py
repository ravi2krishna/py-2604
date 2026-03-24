# Working With Dictionaries 

# empty dict 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# empty dict 
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# dict with numeric data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

data = dict({1:10,2:20,3:30,4:40,5:50})
print(data)

# dict with text data 
data = {"c1":"python","c2":"django","c3":"ai"}
print(data)

# dict with mixed data 
data = {1:10,2:20,3:30,"c1":"python","c2":"django","passed":True}
print(data)

# Accessing Data
data = {1:10,2:20,3:30,4:40,5:50}
print(data) # all data in list 

# Accessing Individual Elements is done using keys not index 
# first_element = data[0] # KeyError: 0
first_element = data[1]
print(first_element)

last_element = data[5]
print(last_element)

# Access Individual Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Data -> 10k elements -> below is not efficient 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
# print(data[9999])

# Access Individual Data -> 10k elements -> below is more efficient  
data = {1:10,2:20,3:30,4:40,5:50,10000:500000000}
for num in data: # only keys we can access 
    print(num)

for key in data:
    print(key)
    
for key in data:
    print(data[key])
    
# Apply Operators -> Req: Multiply Each Element with 10
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)
    
# Apply Conditionals -> Req: Give me only even values
data = {1:10,2:20,3:35,4:40,5:55}
print(data)
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
        
# Req: ["python","django","ai"] take these courses and return them as ["Python","Django","Ai"]
data = {"c1":"python","c2":"django","c3":"ai"}
for key in data:
    print(data[key].title())
    
# Duplicates Allowed For Values
data = {1:10,2:20,3:10,4:40,5:10}
print(data)

# Keys Should be Immutable
# data = {["key1"]:10,["key1"]:20}
print(data) # TypeError: unhashable type: 'list'

data = {("key1"):10,("key1"):20}
print(data) 

# Duplicates Will Override for keys 
data = {1:10,2:20,1:30,4:40,1:50}
print(data)

# Real World Dictionaries Looks Like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU

students = {
    "101": {
        "name": "Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","django","sql"],
        "courses_fee": (10000,8000,5000)
    },
    "102": {
        "name": "John",
        "email": "john@yahoo.com",
        "courses": ["devops","cloud","python"],
        "courses_fee": (25000,20000,10000)
    }    
} 

# Above Covers all the data structures we learnt so far i.e lists, tuples & dictionaries

# Get all students data 
print(students)
print("=" * 50)
# Get me student 102 Info Only 
# print(students[102]) # KeyError: 102
print(students["102"])

# Access 2nd Course Enrolled By John 
# {'name': 'John', 'email': 'john@gmail.com', 'courses': ['devops', 'cloud', 'python'], 'courses_fee': (25000, 20000, 10000)}
print(students["102"]['courses'])
print(students["102"]['courses'][1])
print("2nd Course Enrolled By John is: ", students["102"]['courses'][1])

# Check John is google customer or not 
if students["102"]['email'].endswith("@gmail.com"):
    print("Google customer")
else:
    print("Not Google customer")
    
# List Methods / Operations
print(dir(data))