# Working with txt files
with open("notes.txt", "w") as file:
    file.write("This is a note.\n")
    # file.write("This is another note.\n")

with open("notes.txt", "r") as file:
    note = file.read()
    print(f"This is the note: {note}")

# Working with csv files
import csv

with open("text.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Occupation"])
    writer.writerow(["Alice", "30", "Engineer"])
    writer.writerow(["Bob", "25", "Designer"])

with open("dict.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Occupation"])
    writer.writerow({"Name": "Charlie", "Age": "35", "Occupation": "Teacher"})

with open("dict.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)

# Working with json files
import json
some_data = {
    "name": "Alice",
    "age": 30,
    "children": ["Mark", "Lucy"]
}

with open('data.json', 'w') as file:
    json.dump(some_data, file, indent=4)
