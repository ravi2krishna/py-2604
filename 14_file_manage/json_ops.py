# Working With JSON Files / JSON Data 

student = {
    "id": "101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","reactjs"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Write Data to JSON File
import json
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)
    
# Write Data to JSON File with Indentation
import json
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
# Read Data From JSON File 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print("Loading Data: ", data)
    print(type(data))
    
# Requirement: Get Student Name & Number Of Courses he joined from student.json 
with open("14_file_manage/student.json","r") as file_data:
    json_reader = json.load(file_data)

print("Student Name: ",json_reader['name'] )
print("Number Of Courses: ",json_reader['courses'])
print("Number Of Courses: ",len(json_reader['courses']))
    
# Requirement: Check If Student Passed Or Not, based on GPA above 7
with open("14_file_manage/student.json","r") as file_data:
    json_reader = json.load(file_data)
    
if json_reader['gpa'] > 7:
    print(f"{json_reader['name']} Passed")
else:
    print(f"{json_reader['name']} Failed")

# Python Object Based -> dumps() & loads()
student = {
    "id": "101",
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","reactjs"],
    "gpa": 9.5
}

json_data = json.dumps(student)
print(json_data)
print(type(json_data))

string_data = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "reactjs"], "gpa": 9.5}'
print(string_data)
print(type(string_data))
dict_data = json.loads(string_data)
print(dict_data)
print(type(dict_data))

# Assuming i'm a python full stack developer 
# Working On a API - JSON Data 
# https://dummyjson.com/

# https://medium.com/@themathlab/api-requests-json-parsing-in-python-a-guide-in-data-collection-31e985981ea3

import requests

url = "https://dummyjson.com/users"
response = requests.get(url)

print(response.status_code)
print(response.text)
print(type(response.text))
raw_data = response.text
print("=" * 20)
# Convert Data 
api_data = json.loads(raw_data)
print(api_data)
print(type(api_data))

# Customer Requirement: List me Users 
all_users = api_data['users']
print(all_users)
print("Number Of Users: ", len(all_users))

# Customer Requirement: List me all Users usernames
for user in all_users:
    print(user['id'], user['username'], user['age'])
    
# Customer Requirement: List me all Young Users i.e age below 30
print("=" *30)
print("Junior Employees")
print("=" *30)
for user in all_users:
    if user['age'] < 30:
        print(user['id'], user['username'], user['age'])