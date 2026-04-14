# OOP - Object Oriented Programming

# class -> Blue Print 
# Student -> Real World Entity 

class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies():
        print("Student Info - Student Studies")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation
student_object = Student()    
# student_studies()
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

