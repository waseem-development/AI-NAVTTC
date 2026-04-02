pollingStations = {
    "1001": "City Hall, Block A",
    "1002": "Community Center, Block B",
    "1003": "Library Hall, Block C",
    "1004": "Town Hall, Block D",
    "1005": "Sports Complex, Block E",
    "1006": "Cultural Center, Block F",
    "1007": "High School Gym, Block G",
    "1008": "Municipal Office, Block H",
    "1009": "Community Hall, Block I",
    "1010": "Senior Center, Block J"
}

def checkVotingEligibility():
    while True: 
        age = int(input("Enter your age: "))
        
        if age >= 18:
            areaCode = input("Enter your area code: ").strip()
            
            if areaCode in pollingStations:
                print(f"You are eligible to vote at Polling Station: {pollingStations[areaCode]} with area code {areaCode}")
            else:
                print("Area code not found. You are not eligible during this campaign.")
        else: 
            print("You are under 18. Therefore not eligible to vote.")
        
        while True:
            wantToContinue = input("Do you want to continue? (y/n): ").lower()
            if wantToContinue in ["y", "yes"]:
                break
            elif wantToContinue in ["n", "no"]:
                print("Goodbye!")
                exit()
            else: 
                print("Please enter valid input (y/yes or n/no)")
checkVotingEligibility()