products = [
    {"name": "Processor", "price": 12000},
    {"name": "Board", "price": 8500},
    {"name": "Mug", "price": 450},
    {"name": "Notebook", "price": 600},
    {"name": "Keycaps", "price": 250},
    {"name": "Headphones", "price": 3500},
    {"name": "Watch", "price": 4200},
    {"name": "AI Kit", "price": 30000},
    {"name": "Server", "price": 7000},
    {"name": "Bag", "price": 1800}
]

def productDetails():
    while True: 
        productName = input("Enter the product name: ").lower()
        found = False
        for product in products:
            if product["name"].lower() == productName:
                print(f"{product['name']} costs {product['price']} pkr.")
                found = True
                break  
        if not found:
            print("Product Not Found")
        
        while True:
            wantToContinue = input("Do you want to continue? (y/n): ").lower()
            if wantToContinue in ["y", "yes"]:
                break
            elif wantToContinue in ["n", "no"]:
                print("Goodbye!")
                exit()
            else: 
                print("Please enter valid input (y/yes or n/no)")
productDetails()