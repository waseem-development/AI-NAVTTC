name = input("Enter student name: ")
print()
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
