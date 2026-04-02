# age = 25
# status = "Welcome" if (age >= 25) else "Good Bye"
registeredUsers = [
    {"id": 1,
    "name": "Waseem", 
    "email": "waseemdevelopment2002@gmail.com",
    "password": "WaseemPassword@123"
    },
    {"id": 2,
    "name": "Ahmed", 
    "email": "ahmeddevelopment2002@gmail.com",
    "password": "AhmedPassword@123"
    },
    {"id": 3,
    "name": "Khan", 
    "email": "khandevelopment2002@gmail.com",
    "password": "KhanPassword@123"
    },
]
def registerNewUser():
    print("\n*** Register new User ***\n")
    newName = input("Enter your name: ")
    newEmail = input("Enter your email: ") 
    newPassword = input("Enter your password: ")

    newId = len(registeredUsers) + 1
    newUser = {
        "id": newId,
        "name": newName,
        "email": newEmail,
        "password": newPassword
    }
    registeredUsers.append(newUser)
    print(f"Registration successful! Welcome {newName}. You can now login.")
    
def findRegisterUsers(enteredEmail):

    for user in registeredUsers:
        if user["email"] == enteredEmail:
            return user
    else:
        return

while True:
    print("\n*** Please Login ***\n")
    name = input("Enter your name: ")
    email = input("Enter your email: ") 
    password = input("Enter your password: ")

    hasUpper = False
    hasDigit = False
    hasSpecial = False

    specialCharacters = "!@#$%^&*=+-_"
    for char in password:
        if char.isupper():
            hasUpper = True
        if char.isdigit():
            hasDigit = True
        if char in specialCharacters:
            hasSpecial = True
        
    foundUser = findRegisterUsers(email)

    if foundUser:
        if (password == foundUser["password"] and 
            hasDigit and hasSpecial and hasUpper and 
            "@" in email and "." in email):
            
            print(f"Login successful. \n\t\tWelcome Back {foundUser['name']}")
        else: 
            print("Login failed: Incorrect password or invalid format.")
    else: 
        print("No users found, please Register first, Please register first.")
        registerNewUser()
