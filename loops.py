# for-loops
for i in range(9):
    print("Bjay")

for j in range(1, 10):
    print(j)

for k in range(0, 10, 2):
    print(f"{k} is even")
for odd_num in range(1, 10, 2):
    print(f"{odd_num} is odd")
# while-loops
count = 1
while count <= 10:
    print(f"Count is: {count}")
    count += 1

even_numbers = 0
while even_numbers <= 10:
    print(f"{even_numbers} is even")
    even_numbers += 2
odd_numbers = 1
while odd_numbers <= 10:
    if odd_numbers % 2 != 0:
        print(f"{odd_numbers} is odd")
        odd_numbers += 2
