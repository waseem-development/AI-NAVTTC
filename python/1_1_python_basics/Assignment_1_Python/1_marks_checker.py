import random

subjects = ["Calculus", "Discrete Mathematics", "Linear Algebra", "Machine Learning", "Deep Learning"]

while True: 
    subject_marks = [random.randint(35, 100) for _ in subjects]  # list comprehension

    def averageAndSum(marks):
        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        return total, average, grade

    total, average, grade = averageAndSum(subject_marks) # this is called tupple unpacking

    print("\nMarks:")
    for subject, mark in zip(subjects, subject_marks):
        print(f"{subject}: {mark}")

    print("\nTotal:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade, "\n")


    while True:
        toContinue = input("Do you want to continue? (yes/no): ").lower()
        if toContinue in ["yes", "y"]:
            break  
        elif toContinue in ["no", "n"]:
            print("Goodbye!")
            exit()  
        else:
            print("Please enter either yes or no:")