year = int(input("Enter starting year: "))

count = 0

while count < 20:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
        count += 1
    year += 1