def serve_chai():
    yield "Cup 1: Masala CHai"
    yield "Cup 2: Ginger Chai"

stall = serve_chai()

#for cup in stall:
#    print(cup)

print(next(stall))
print(next(stall))

# Infinite generators
def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()

for _ in range(3):
    print(next(refill))


# send generators

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield # program will wait here to pass us the value if we don't pass ss.send() the function will stop here

    while True:
        print(f"Preparing: {order}")
        order = yield # stopping the function here

ss = chai_customer()
next(ss) # we started the generator here

ss.send("Lemon Chai") # we send the value