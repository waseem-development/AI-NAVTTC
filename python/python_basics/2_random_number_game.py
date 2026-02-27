import random

number = int(input("Choose a number between 1 and 100: "))
rdm = random.randint(1, 100)
attempt = 0
while True:
    if rdm > number:
        print("Oops!! try bigger number please!")
        attempt += 1
        number = int(input("Enter another number: "))
    elif rdm < number:
        print("Oops!! try smaller number please!")
        attempt += 1
        number = int(input("Enter another number: "))
    else:
        attempt +=1
        print("Yepppiiiiiiiii! guessed it in", attempt, "the number is: ", number)
        character = input("Would u like to play another game? (Y/N): ")
        if character == "n" or character == "N":
            break
        elif character == "y" or character == "Y":
            attempt = 0
            number = int(input("Choose a number between 1 and 100: "))
            rdm = random.randint(1, 100)
            continue