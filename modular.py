from utils import greet

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("This is a modular program.")
    print("Addition of 5 and 3 is:", add(5, 3))
    print("Subtraction of 5 and 3 is:", subtract(5, 3))
    print(greet("John"))  # Call the greet function from utils module


main()