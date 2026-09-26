import os

# # Get Current Working Directory
# print(f"os.getcwd(): get current working directory: ({os.getcwd()})\n\n") 
# print(os.listdir())
# # Change Directory
# os.chdir("/home/waseem-dev/AI")
# print(f"\n\nos.getcwd(): get current working directory: ({os.getcwd()})") 

# # List Files and Directories
# print(os.listdir())
# print(os.listdir("AI-NAVTTC"))
# Check wheter a file exists

# if os.path.exists("cats.csv"):
#     print("File exists")
# else:
#     print("File doesn't exist")

# Check File vs Folder

# print(os.path.isfile("cats.csv"))
# print(os.path.isdir("datasets"))


# Joining Paths
# directory = "Assignment_1_Python"
# file = "1_marks_checker.py"

# path = os.path.join(directory, file)

# print(path)


# Create Directory
# os.mkdir("models")
# os.makedirs("models", exist_ok=True)

# Delete a file
# os.remove("123.py")


# Rename a file
# os.rename("cats.csv", "cat_dataset.csv")

# Move a file:
# os.rename(
#     "processed/cats.csv",
#     "datasets/cats.csv"
# )


# Print Environment Data
# print(os.environ)


# Get one Environment Variable
api_key = os.getenv("API_KEY")
print(api_key)