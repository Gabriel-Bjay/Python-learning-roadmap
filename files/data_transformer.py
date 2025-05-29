with open("names.txt", "r") as file:
    name = file.read().strip().split(",")[0]
    print(f"Hello, {name}!")