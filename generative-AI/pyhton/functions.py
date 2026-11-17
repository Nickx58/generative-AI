def print_name(name):
    print(f"Hello {name}!!")

print_name("Nick")

def cal_bill(chai,amount):
    return chai * amount

my_bill = cal_bill(2,50)
print(my_bill)


def serve_chai():
    chai_type = "MAsala" # Local scope
    print(f"Inside Function: {chai_type}")

chai_type = "Lemon"
serve_chai()