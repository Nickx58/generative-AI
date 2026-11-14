# Range based For Loop

for token in range(1,3):
    print(f"Token Number: {token} is ready")

names = ["Nikhil", "Nisha", "Manu", "Moonie"]

for name in names:
    print(f"Name is: {name}")

# Enumerate Example

foods = ["Kulcha", "Pav Bhaji", "Dal Makhni"]

for idx, item in enumerate(foods, start=1):
    print(f"{idx} : {item}")

# ZIP example

amount = [8,17,26,5]

for name,bill in zip(names,amount):
    print(f"Bill for: {name} is Rs: {bill}")

# While Loop
temp = 40
while temp <= 100:
    print(f"Current Temp is: {temp}")
    temp += 15
