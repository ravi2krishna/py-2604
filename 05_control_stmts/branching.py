# Branching Structures / Statements (Jump Statements)

for num in range(1,11):
    print(num)
    
# break - help you exit the loops 
for num in range(1,11):
    if num == 5: # stop the loop from here
        break 
    print(num)
    
# continue : help you skip the current iteration 
for num in range(1,11):
    if num == 5: # skip the current iteration
        continue 
    print(num)
    
# pass : acts as a placeholder, does nothing
# Requirement - To perform some future operations 
emp_salary = 15000
if emp_salary > 25000:
    pass # _________

# After 6 Months 
emp_salary = 15000
if emp_salary > 25000:  
    print("Promoted To Senior Employee")
    
# Working with OOP 
class Employee: 
    pass 

class Organization:
    pass 