snack = input("Enter your fav snack: ").lower()

if snack == 'samosa' or snack == 'pav':
    print("Great Choice")
else:
    print("Not available at the moment")


cup = input("Enter cup size: ").lower()

if cup == 'small':
    print("Price is 10")
elif cup == 'medium':
    print("Price is 15")
elif cup == "large":
    print("Price is 20")
else:
    print("Invalid price")

# Convert string to int
order_amount = int(input("Enter the Order Amount: "))

delivery_fees = 0 if order_amount > 300 else 30