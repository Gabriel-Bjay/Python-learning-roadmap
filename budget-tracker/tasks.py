# Function to set the budget

grocery_list = {}  # Initialize an empty dictionary to store grocery items
budget = 0.0  # Initialize budget to 0.0


def set_budget():
    global budget
    budget = float(input("Enter your budget: "))
    print(f"Your budget is set to {budget}.")
# Function to add a new task


def add_item():
    item = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))
    grocery_list[item] = (quantity, price)
    print(f"Item '{item}' with price {price} added to the list.")
# Function to view all items


def view_items():
    if not grocery_list:
        print("No items in the list.")
    else:
        print("Items in the list:")
        for item, (qty, price) in grocery_list.items():
            print(f"{item}: {qty} @ {price} = {qty * price}")
# Function to view total items


def view_total_items():
    total = sum(qty * price for qty, price in grocery_list.values())
    print(f"Total cost of items: {total}")
    print(f"Remaining budget: {budget - total}")
    if total > budget:
        print("Warning: You are over the budget!")
# Function to delete an item


def delete_item():
    item = input("Enter the name of the item to delete: ")
    if item in grocery_list:
        del grocery_list[item]
        print(f"Item '{item}' deleted from the list.")
    else:
        print(f"Item '{item}' not found in the list.")
# Function to apply discount


def apply_discount():
    item = input("Enter item to discount: ")
    if item in grocery_list:
        discount = float(input("Enter discount %: "))
        qty, price = grocery_list[item]
        discounted_price = round(price * (1 - discount/100), 2)
        grocery_list[item] = (qty, discounted_price)
        print(f"New price for {item}: {discounted_price}")
    else:
        print("Item not on list")
