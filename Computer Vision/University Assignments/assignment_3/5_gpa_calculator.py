marks = []

for i in range(6):
    mark = int(input(f"Enter marks for course {i+1}: "))
    marks.append(mark)

total_gp = 0

for m in marks:
    if m >= 80:
        gp = 4.0
    elif m >= 70:
        gp = 3.0
    elif m >= 60:
        gp = 2.0
    elif m >= 50:
        gp = 1.0
    else:
        gp = 0.0

    total_gp += gp

gpa = total_gp / 6

print("\n--- Result ---")
print("Total Grade Points:", total_gp)
print("GPA of Semester:", round(gpa, 2))