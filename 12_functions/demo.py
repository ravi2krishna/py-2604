# Functional Programming 

# Without Functions

num1 = 10
num2 = 5

# Math Operations 

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# Another Uses Wants To Calculate With 20 & 10 

num1 = 20
num2 = 10

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# Another Uses Wants To Calculate With 200 & 100

num1 = 200
num2 = 100

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# With Functions

def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# User 1 -> 10 & 5
num1 = 10
num2 = 5
math_ops()
print("=" * 20)
# User 2 -> 20 & 10
num1 = 20
num2 = 10
math_ops()
print("=" * 20)
# User 3 -> 200 & 100
# User N 
num1 = 200
num2 = 100
math_ops()
print("=" * 20)

# Function With Parameters
def math_ops(num1,num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5)
print("=" * 20)
math_ops(20,10)
print("=" * 20)
math_ops(200,100)
print("=" * 20)

# Positional Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

# employee_info("hyderabad","ravi") # TypeError: employee_info() missing 1 required positional argument: 'emp_location'      
employee_info("hyderabad","ravi","ravi@gmail.com")    
employee_info("ravi","ravi@gmail.com","hyderabad")    
print("=" * 20)

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabad","ravi","ravi@gmail.com") 
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com") 

print("=" * 20)

# No Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email}, working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com",org_name="Google")     
employee_info(emp_location="pune",emp_name="krishna",emp_email="krishna@gmail.com",org_name="Google")     
employee_info(emp_location="sydney",emp_name="john",emp_email="john@gmail.com",org_name="Google")  
# 20 other employees same company 

print("=" * 20)

# With Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email}, working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")     
employee_info(emp_location="pune",emp_name="krishna",emp_email="krishna@gmail.com")     
employee_info(emp_location="sydney",emp_name="john",emp_email="john@gmail.com")  
# 20 other employees same company 

# Employee mike is from META 
employee_info(emp_location="new jersey",emp_name="mike",emp_email="mike@gmail.com")
employee_info(emp_location="new jersey",emp_name="mike",emp_email="mike@gmail.com",org_name="META")

# Placement Requirement
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile):
#     print(f"Hi {emp_name}, your email is {emp_email}, working for {org_name} at location {emp_location}")

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email}, working for {org_name} at location {emp_location}")
     
def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="Google",planet="Earth"):
     print(f"Hi {emp_name}, your email is {emp_email}, working for {org_name} at location {emp_location}") 