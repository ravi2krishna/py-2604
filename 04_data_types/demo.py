# Data Types 

# Numeric Types 

data = 10 
print(type(data))

data = -10 
print(type(data))

data = 10.5 
print(type(data))

data = -10.5 
print(type(data))

# data = 3 + i5
# print(type(data))

data = 3 + 5j
print(type(data))

# Boolean Type
data = True
print(type(data))

data = False 
print(type(data))

# None Type
data = None 
print(type(data))

# String Type
data = "python"
print(type(data))

# List 
data = [10,20,30,40,50]
print(type(data))

# Tuple
data = (10,20,30,40,50)
print(type(data))

# Set
data = {10,20,30,40,50}
print(type(data))


# Frozenset
data = frozenset({10,20,30,40,50})
print(type(data))

# Dictionary
data = {"course":"python","time":12,"duration":60}
print(type(data))
 
# Custom Datatype
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_gpa = 9.5 
    student_enrolled_courses = ["python","cloud","devops"]

data = Student()
print(type(data))
print(data.student_id)
print(data.student_name)