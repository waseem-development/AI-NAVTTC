users = {
    "waseem_ahmed": {
        "password": "waseem123",
        "age": 22,
        "isStudent": True,
        "balance": 12000,
        "prevBalance": 12000
    },
    "ayesha_khan": {
        "password": "ayesha321",
        "age": 23,
        "isStudent": True,
        "balance": 5000,
        "prevBalance": 5000
    },
    "umar_hussain": {
        "password": "umar789",
        "age": 31,
        "isStudent": False,
        "balance": 15000,
        "prevBalance": 15000
    },
    "fatima_rahman": {
        "password": "fatima2026",
        "age": 22,
        "isStudent": True,
        "balance": 7000,
        "prevBalance": 7000
    },
    "zainab_saeed": {
        "password": "zainab456",
        "age": 28,
        "isStudent": False,
        "balance": 10000,
        "prevBalance": 10000
    },
    "hassan_qureshi": {
        "password": "hassan999",
        "age": 35,
        "isStudent": False,
        "balance": 20000,
        "prevBalance": 20000
    },
    "sana_malik": {
        "password": "sana1234",
        "age": 24,
        "isStudent": True,
        "balance": 4500,
        "prevBalance": 4500
    },
    "bilal_javed": {
        "password": "bilal789",
        "age": 29,
        "isStudent": False,
        "balance": 8000,
        "prevBalance": 8000
    }
}

def loanEligibility(user):   
    if user["age"] >= 20 and user["isStudent"]:
        print("You are eligible for a loan.\n")
    else:
        print("You are not eligible for a loan.\n")

def depositFunction(user):
    depositAmount = int(input("Enter the amount to deposit: "))
    user['prevBalance'] = user['balance']
    user['balance'] += depositAmount
    print("\nDeposit Successful!")
    print(f"Previous Balance: {user['prevBalance']} PKR")
    print(f"Deposited Amount: {depositAmount} PKR")
    print(f"New Balance: {user['balance']} PKR\n")

def withDrawFunction(user):
    withDrawAmount = int(input("Enter the amount to withdraw: "))
    if withDrawAmount <= user['balance']:
        user['prevBalance'] = user['balance']
        user['balance'] -= withDrawAmount
        print("\nWithdrawal Successful!")
        print(f"Previous Balance: {user['prevBalance']} PKR")
        print(f"Withdrawn Amount: {withDrawAmount} PKR")
        print(f"New Balance: {user['balance']} PKR\n")
    else: 
        print("Insufficient Balance\n")

def accountDetails(user):
    print("\n===== Account Details =====")
    print(f"Age: {user['age']}")
    print(f"Student: {'Yes' if user['isStudent'] else 'No'}")
    print(f"Previous Balance: {user['prevBalance']} PKR")
    print(f"Current Balance: {user['balance']} PKR\n")

def loginUser():
    while True:
        username = input("Enter your username: ")
        if username in users:
            password = input("Enter your password: ")
            if users[username]["password"] == password:
                print(f"\nLogin Successful. Welcome back {username}!\n")
                loanEligibility(users[username])
                return users[username]
            else:
                print("Incorrect password.\n")
        else:
            print("User not found.\n")
        
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice in ["n", "no"]:
            print("Exiting program. Goodbye!")
            exit()

def bankMenu(user):
    while True:
        print(
            """
===== Bank Menu =====
1) Deposit
2) Withdraw
3) View Account Details
4) Logout
"""
        )
        option = input("Choose an option (1-4): ").strip()
        
        if option == "1":
            depositFunction(user)
        elif option == "2":
            withDrawFunction(user)
        elif option == "3":
            accountDetails(user)
        elif option == "4":
            print("Logging out...\n")
            break
        else:
            print("Invalid option! Please choose 1, 2, 3, or 4.\n")

def main():
    print("***** Welcome to Waseem's ABC Bank *****\n")
    while True:
        loggedInUser = loginUser()
        bankMenu(loggedInUser)

main()