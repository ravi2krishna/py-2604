# Student Management System

# Menu Based System -> In Future once you learn full stack, replace with UI Elements like Buttons 

# System Setup -> System Info - READ ONLY (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ ONLY (Tuple)
ADMIN_INFO = ("9900998800","admin@edify.com")

# Displaying System Info On Start Up 
print("=" * 50)
print(f"Welcome To: {SYSTEM_INFO[0]}")
print(f"Software Name: {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionality (CRUD)
# Add Student -> id, name, scores, skills 
# Representing Students Data inside Dictionary 

# https://jsoneditoronline.org/images/news/smart_json_formatting.png

# Students Data inside Dictionary 
students = {}

# Build Menu System For Operations 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Student")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        print("=" * 30)
        print("Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS!! Student Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
            
            print("========== Student Added ==========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print(students)
            
    
    elif choice == "2":
        print("=" * 30)
        print("Updating Student")
        print("=" * 30)
        
    
    elif choice == "3":
        print("=" * 30)
        print("Deleting Student")
        
        
    elif choice == "4":
        print("=" * 30)
        print("Reading Student")
        print("=" * 30)
        
    
    elif choice == "5":
        print("=" * 30)
        print("Exit Application")
        
        break
    
    else:
        print("=" * 30)
        print("Invalid Option, Only use (1-5)")
        print("=" * 30)
        
    