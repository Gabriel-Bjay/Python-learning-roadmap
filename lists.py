cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

cars.append("Ferrari")  # Adds a new car at the end of the list
fruits.insert(1, "Fig")  # Adds a new fruit at the first index of the list
cars.remove("Honda")  # Removes "Honda" from the list
fruits.pop(2)  # Removes the fruit at index 2
del cars[-1]  # Deletes the last car in the list
numbers.sort()

# Print the updated lists
print("Updated Cars List:", cars)
print("Updated Fruits List:", fruits)
