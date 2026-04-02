registeredUsers = []

def registerNewUser():
    print("\n*** Register New User ***\n")
    newName = input("Enter your full name: ")
    newUsername = input("Enter your username: ")
    newEmail = input("Enter your email: ")
    newPassword = input("Enter your password: ")
    
    hasUpper = any(c.isupper() for c in newPassword)
    hasDigit = any(c.isdigit() for c in newPassword)
    hasSpecial = any(c in "!@#$%^&*=+-_" for c in newPassword)

    if not (hasUpper and hasDigit and hasSpecial):
        print("Password must contain at least one uppercase, one digit, and one special character.")
        return

    newId = len(registeredUsers) + 1
    newUser = {
        "id": newId,
        "name": newName,
        "username": newUsername,
        "email": newEmail,
        "password": newPassword
    }
    registeredUsers.append(newUser)
    print(f"Registration successful! Welcome {newName}. You can now login.")


def findUser(username=None, email=None):
    for user in registeredUsers:
        if (username and user["username"] == username) or (email and user["email"] == email):
            return user
    return None


while True:
    print("\n*** Please Login ***\n")
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        username = input("Enter your username (or press enter to skip): ").strip() or None
        email = input("Enter your email (or press enter to skip): ").strip() or None
        password = input("Enter your password: ")

        user = findUser(username=username, email=email)
        if user:
            if user["password"] == password:
                print(f"Login successful. Welcome Back {user['name']}!")
                break 
            else:
                attempts += 1
                print(f"Incorrect password. Attempts left: {max_attempts - attempts}")
        else:
            print("No users found. Please register first.")
            registerNewUser()
            break 
    else:
        print("Maximum login attempts reached. Try again later.")
        break  