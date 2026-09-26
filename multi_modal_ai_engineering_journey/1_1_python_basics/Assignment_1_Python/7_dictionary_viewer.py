students = [
    {"name": "Waseem", "marks": 500},
    {"name": "Zyron", "marks": 462},
    {"name": "Kael", "marks": 489},
    {"name": "Nyra", "marks": 475},
    {"name": "Orin", "marks": 451},
    {"name": "Zarael", "marks": 493},
    {"name": "Ishara", "marks": 468},
    {"name": "Riven", "marks": 477},
    {"name": "Tavish", "marks": 459},
    {"name": "Elowen", "marks": 482}
]
def studentMarksFunction():
    while True: 
        studentName = input("Enter your name: ").lower()
        found = False
        for student in students:
            if student["name"].lower() == studentName:
                print(student["marks"])
                found = True
                break
        if not found:
             print("Invalid Name")
        
        while True:
            userChoice = input("""\nDo u want to continue? 
            1) Yes
            2) No
            ==> """).lower()
            if userChoice in ["yes", "y"]:
                    break
            elif userChoice in ["no", "n"]:
                 exit()
            else: 
                 print("Invalid Choice Please enter correct number")
                 continue
studentMarksFunction()