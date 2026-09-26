from pathlib import Path

# path = Path.cwd()

# print(path)
# print(type(path))

# path = Path("processed/cat_dataset.csv")

# print(path.exists())


# path.is_file()


# path.is_dir()

# path = Path("processed")

# if path.is_dir():
#     print("It's a directory")

file_path = Path("processed") / "cat_dataset.csv"
print(file_path)


print(file_path.name)
print(file_path.suffix)
print(file_path.stem)
print(file_path.parent)
folder = Path("models")

folder.mkdir(exist_ok=True)