chai_menu = {
    "masala": 30,
    "ginger": 40
}
try:
    chai_menu["elachi"]
except KeyError:
    print("The key that you are trying to access does not exists")

def server_chai(flavor):
    try:
        print(f"Preparing {flavor} chai....")
        if flavor == "unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else :
        print("Chai is served")
    finally:
        print("Next customer this")

server_chai("unknown")
server_chai("Massla")
