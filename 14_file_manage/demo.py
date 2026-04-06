# Working With Files & Directories(Folders)

# Using Persistent Storage 

# Syntax - 1

file = open("14_file_manage/file.txt","r")
print(file)

# NOTE: Here we need to "explicitly close" files after operations are performed
print(file.closed) # False -> Still Open 
file.close() # explicitly close
print(file.closed) # True -> Now Closed

print("=" * 20)

# Syntax - 2 # Recommended Way 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file.closed) # True -> Implicitly Closed

# Reading Data From File - Whole file 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())
    
# Reading Data From File - Character Wise 
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
        
# Reading Data From File - Word Wise 
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read().split():
        print(char)
        

# Reading Data From File - Line Wise (one line)        
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
    
# Reading Data From File - Line Wise (multiple line)      
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())
    
with open("14_file_manage/file.txt","r") as file_data:
    list_data = file_data.readlines()
    for line in list_data:
        print(line.strip())
        
# Write Data Using 'w' mode 

# Using Write Mode To Create File 
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)
    
# Write Data To File 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Python Language")
    
    
# Write Data To File - Multiple Lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Hello From Python\n', 'next line \n', 'followed by another line\n'])

# Append Mode 'a' mode 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Python Language")
    
# Append Mode 'a' mode 
with open("14_file_manage/write.txt","a") as file_data:
    file_data.write(" Is Very Easy")

with open("14_file_manage/write.txt","a") as file_data:
    file_data.write(" To Learn")
    
    
# Creating Directory / Folder 
directory_name = "14_file_manage/students_data"
# mkdir(directory_name) # NameError: name 'mkdir' is not defined
import os 
# os.mkdir(directory_name) # FileExistsError: [Errno 17] File exists: '14_file_manage/students_data'
if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Create a file in students_data Directory / Folder 
with open("14_file_manage/students_data/student.txt","w") as file_data: 
    file_data.write("Python Students")

# Deleting File 
os.remove("14_file_manage/students_data/student.txt")

# Deleting Empty Directory / Folder 
os.rmdir("14_file_manage/students_data")

# Deleting Non Empty Directory / Folder 
# os.rmdir("14_file_manage/data") # OSError: [Errno 66] Directory not empty: '14_file_manage/data'
import shutil 
shutil.rmtree("14_file_manage/data")

