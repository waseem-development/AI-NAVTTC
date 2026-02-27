import random as rdm
import string as st

def generatePassword(length):
    passStr = "" + st.ascii_lowercase

    while True:
        askUppercase = input("Do u want your password to contain uppercase letters (A-Z)? Type Y/N: ")

        if askUppercase == "Y".lower():
            passStr += st.ascii_uppercase
            break
        elif askUppercase == "N".lower():
            break
        else:
            print("Invalid character! Please enter valid character.")
            continue
    
    while True:
        askDigits = input("Do u want your password to contain digits (0-1)? Type Y/N: ")
        if askDigits == "Y".lower():
            passStr += st.digits
            break
        elif askDigits == "N".lower():
            break
        else:
            print("Invalid character! Please enter valid character.")
            continue
    
    while True:
        askSpecialCharacters = input("Do u want your password to contain Special Characters (#@%^ etc)? Type Y/N: ")
        if askSpecialCharacters == "Y".lower():
            passStr += st.punctuation
            break
        elif askSpecialCharacters == "N".lower():
            break
        else:
            print("Invalid character! Please enter valid character.")
            continue

    password = "".join(rdm.choices(passStr, k=length))
    return password

while(True):
    length = int(input("Enter the length of your password: "))
    password = generatePassword(length)
    print("Your generated password: ", password)

    while True:
        again = input("Do you want to continue? Y/N: ")
        if again == "Y".lower():
            break
        elif again == "N".lower():
            exit()
        else: 
            print("Invalid character! Please enter Y or N.")



