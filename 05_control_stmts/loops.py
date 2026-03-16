# Looping Structures / Statements (Iteration Statements)

# While Loop
# while True:
#     print("This Line Always Executes - Forms Infinite Loop")
    # To Terminate the loops use control + c on keyboard
    
while False:
    print("This Line Always Executes - Forms Infinite Loop")
    
# While Loop
# Counters
count = 1
while count <= 5 :
    print("Count: ", count)
    count += 1
    
# You found a lost phone, trying to break passcode 
# At which attempt the phone will be unlocked ?
actual_passcode = "1234"
user_given_passcode = ""

while user_given_passcode != actual_passcode:
    user_given_passcode = input("Enter Passcode: ")
    
print("Phone Unlocked")

# for loop 
prices_products = [1000,1500,2500,5000] 
# Some Offer is running - apply a discount of 500 on each product 
# [1000-500,1500-500,2500-500,5000-500] 
print(prices_products[0]) # 1000
print(prices_products[1]) # 1500

print(prices_products[0]-500) # 1000
print(prices_products[1]-500) # 1500
print(prices_products[2]-500) 
print(prices_products[3]-500) 

print("============")

# for loop -> Now we have 1000 products 
prices_products = [1000,1500,2500,5000,8000,10000,12000,15000] 
# Some Offer is running - apply a discount of 500 on each product 
for price in prices_products:
    # print(price)
    print(price - 500)
    
# Say Hello 
print("Hello")

# Say Hello 10 Times 
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# for loop with range()
for num in range(0,5,1):
    print(num) 
    
for num in range(7,13,1):
    print(num) 
    
for num in range(5):
    print(num) 
    
for num in range(2,5):
    print(num) 
    
for num in range(5,50,5):
    print(num) 
    
for num in range(1,10,1):
    print(num) 

print("=====")
    
for num in range(1,10,-1):
    print(num) 

print("=====")
    
for num in range(10,1,-1):
    print(num) 
    
# Say Hello 100 Times 
for num in range(100):
    print("Hello")
    