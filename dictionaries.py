inventory = {
    "assault_rifle": "Ak117-Grim_reaper",
    "battle_axe": "Battle_axe",
    "sniper_rifle": "Dlqq3",
    "shotgun": "By15",
    "ammo": "5.56mm",
    "armor": "Kinetic_armor",
    "grenade": ["Molotov_cocktail", "Flashbang", "Smoke_grenade"],
    "backpack": "Backpack-level-3",
}

print(inventory)  # Output the inventory dictionary

# Adding a new item to the inventory
inventory["pistol"] = "M1911"
print(inventory)  # Output the updated inventory dictionary

# Output the sniper rifle & grenade list from the inventory
print(inventory.get("sniper_rifle"))
print(inventory.get("grenade"))
# Output a default message if the key is not found
print(inventory.get("health", "Item not found"))

# Changing the value of an existing item
inventory["assault_rifle"] = "M4-Black Gold Royal"

print(inventory["assault_rifle"])  # Output the updated assault rifle


# Looping through the inventory
print(len(inventory))  # Output the number of items in the inventory

"""
Create a dictionary called student with keys: 'name', 'grade', 'courses'
Then add a new key 'age' and 'graduated ' ,
with the value '19' and 'False' to the dictionary
"""
student = dict(
    Name='Bjay',
    Grade='A-',
    Courses=[
        'Software Engineering',
        'Calculus',
        'Wireless networks',
        'Programming Languages'
    ]
)

print(student)  # Output the student dictionary

student['Age'] = 19
student['Graduate'] = 'False'
print(student)  # Output the updated student dictionary

# Looping through the student dictionary
for key, value in student.items():
    # Output each key-value pair in the student dictionary
    print(f"{key}: {value}")
