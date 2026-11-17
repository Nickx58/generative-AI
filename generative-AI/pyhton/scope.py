def update_order():
    chai_type = "Ginger"
    def kitchen():
        nonlocal chai_type
        chai_type = "Lemon"
    kitchen()
    print("After Kitchen Update", chai_type)

update_order()

chai_type = "Plain"

def front_desk():

    def kitchen():
        global chai_type
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final GLobal Chai:", chai_type)