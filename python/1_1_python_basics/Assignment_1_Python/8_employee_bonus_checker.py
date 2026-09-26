employees = [
    {"name": "Waseem", "salary": 500000},
    {"name": "Zyron", "salary": 462000},
    {"name": "Kael", "salary": 489000},
    {"name": "Nyra", "salary": 475000},
    {"name": "Orin", "salary": 451000},
    {"name": "Zarael", "salary": 493000},
    {"name": "Ishara", "salary": 468000},
    {"name": "Riven", "salary": 477000},
    {"name": "Tavish", "salary": 459000},
    {"name": "Elowen", "salary": 482000}
]

def employeeSalaryFunction():
    while True: 
        bonusRate = 0.15
        employeeName = input("Enter your name: ").lower()
        
        found = False
        
        for employee in employees:
            if employee["name"].lower() == employeeName:
                found = True
                
                if employee["salary"] > 470000:
                    annualBonus = employee["salary"] * bonusRate
                    totalIncome = employee["salary"] + annualBonus
                    print(f"{employeeName}'s salary is {totalIncome} with bonus of {annualBonus}")
                else:
                    print("Bonus not valid for this employee")
                
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
                print("Invalid Choice Please enter correct input")
                continue

employeeSalaryFunction()