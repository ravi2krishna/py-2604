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

print("=" * 20)  
     
# Arbitrary Positional Arguments

# def add_numbers(n1)

# def add_numbers(n1,n2)

# def add_numbers(n1,n2,n3)

# def add_numbers(n1,n2,n3,...,n10)

def add_numbers(*nums):
    print(nums)
    
add_numbers(10,20)
add_numbers(10,20,30)

def add_numbers(*nums):
    # find sum 
    total = 0
    for num in nums:
        # print(num)
        total += num
    print(f"Total Sum is {total}")

add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50)

# Real World Scenario Use Case: Carts in Ecommerce Application 

print("=" * 20)  

# Arbitrary Keywords Arguments
def profile(**info):
    print(info)
    
profile(fname="Ravi")
profile(fname="Ravi",lname="Krishna")
profile(fname="Ravi",lname="Krishna",email="ravi2krishna@gmail.com")

# Real World Use Case -> jan=2000,feb=3500,mar=5000
# Get Total Transactions Value and Number Of Transactions 
def bank_transactions(**transactions):
    print(transactions)
    total = 0
    transactions_count = 0
    for transaction in transactions:
        print(transaction)
        print(transactions[transaction])
        total += transactions[transaction]
        transactions_count += 1
    print(f"You have Done {transactions_count} Transactions, Which Totals To {total}")

bank_transactions(jan=2000,feb=3500,mar=5000)
bank_transactions(jan=2000,feb=3500,mar=5000,apr=5500,may=7000,jun=10000)

print("=" * 20)  

# Without return 
def add(a,b):
    a + b 
    
add(10,20)
print(add(10,20)) # When you don't use a return, by default a function returns "None" 

# With return 
def add(a,b):
   return a + b 

add(10,20)
print(add(10,20))
print(add(30,60))

# function composition (function calling another function)
def sub(c,d,e): # add c & d, then minus e -> c + d - e
    return add(c,d) - e 

print(sub(3,4,5)) # 3 + 4 - 5 -> 2 

print("=" * 20)  

# return - make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started")
    return a + b 
    print("Calculation Completed") # Code is structurally unreachable

print(add(200,100))    

print("=" * 20) 

# with multiple return statements, first will be considered
def math_ops(num1,num2):
    return num1 + num2 
    return num1 - num2 
    return num1 * num2
    return num1 / num2 

print(math_ops(30,60))

print("=" * 20) 

# with multiple return statements, conditional approach 
def math_ops(num1,num2,operator):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2 
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2 
    else:
        return "Invalid Operator"
    

print(math_ops(40,60,"+"))    
print(math_ops(40,60,"*"))
print(math_ops(40,60,"$"))
  
print("=" * 20) 
    
# Local Scope: A local variable i.e declared "inside the function"
def add():
    la = 10 # local variable 
    lb = 20 # local variable 
    print(la) # Accessed Within Function 
    print(lb) # Accessed Within Function 

add()

# print(lb) # Accessed Outside Function # NameError: name 'lb' is not defined

def add(la,lb): # local variables la & lb 
    print(la) # Accessed Within Function 
    print(lb) # Accessed Within Function
    
add(10,20)

# print(lb) # NameError: name 'lb' is not defined
    
print("=" * 20) 

# Global Scope 
ga = 100 # Global i.e outside the function 
def add(la,lb): # local variables la & lb 
    print(la) # Accessed Within Function 
    print(lb) # Accessed Within Function
    print(ga) # Global Variable Accessed Within Function 

add(30,40)
print(ga) # Global Variable Accessed Outside Function 

# name conflict issue
ga = 100 # Global i.e outside the function 
def add(la,lb,ga): # local variables la & lb 
    print(la) # Accessed Within Function 
    print(lb) # Accessed Within Function
    print(ga) # local variable, as per preference 
    print(globals()['ga']) # global variable, Accessed Within Function  

add(3,4,5)

# global variables outside the function 
count = 0
print(count)
count += 1
print(count)

# global variables inside the function 
count = 0
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count 

print(increment())

# Built In Functions
# print()
# id()
# type()
# dir()
# input()

# User Defined Functions 
# add()
# employee_info()
# math_ops()
# increment()

# without lambda function / Regular Function 
def add(a,b):
    return a+b 
print(add(10,10))
# With lambda function
# lambda arguments:expression
lambda a,b:a+b 
print((lambda a,b:a+b) (20,10)) # IILE 

# without lambda 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 

print(is_even_num(11))
print(is_even_num(10))

# with lambda 
lambda num:num % 2 == 0
print((lambda num:num % 2 == 0) (10)) # IILE 
print((lambda num:num % 2 == 0) (11)) # IILE 

# without lambda 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

# with lambda 
# lambda arguments:expression
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")) (emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")) # IILE 

# Without Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

# With Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
# syntax -> map(function, iterable)
map((lambda num: num * num),[1,2,3,4,5])
print(map((lambda num: num * num),[1,2,3,4,5]))
print(list(map((lambda num: num * num),[1,2,3,4,5])))

# Real World Use Case Of Working With Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

# real world use case of map -> find me prices after discounts 

# find me prices after discount (How To Do - imperative)
prices_after_discount = []
for product in products:
    # print(product)
    price = product["price"]
    # print(price)
    discount = product["discount"]
    
    price_after_discount = price - (price * discount / 100)
    # print(price_after_discount)
    prices_after_discount.append(price_after_discount)
    
print(prices_after_discount)

# real world use case of map -> find me prices after discounts 

# syntax -> map(function,iterable) (What To Do - declarative)
map((lambda product: product["price"] - product["price"] * product["discount"] / 100 ),products)
print(map((lambda product: product["price"] - product["price"] * product["discount"] / 100 ),products))
print(list(map((lambda product: product["price"] - product["price"] * product["discount"] / 100 ),products)))
print(list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100 ),products)))

prices_after_discount = list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100 ),products))
print("Prices After Discounts: ",prices_after_discount)


# without filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]

def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# with filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
# filter(function, iterable)
# lambda num: num % 2 == 0
filter((lambda num: num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num: num % 2 == 0),[1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num: num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])))


# Real World Use Case Of Working With Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

# find me premium products i.e a product with price above 25000 
premium_products = []

for product in products:
    price = product["price"]
    if price > 25000:
        premium_products.append(product)
        
print(premium_products)
print(premium_products[0]['name'], premium_products[0]['price'])

print(list(filter((lambda p: p['price'] > 25000),products)))
premium_products = list(filter((lambda p: p['price'] > 25000),products))
print("Premium Products: ",premium_products)

for p in premium_products:
    print(p['name'], p['price'])
