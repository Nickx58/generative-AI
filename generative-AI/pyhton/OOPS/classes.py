class Coffee:
    origin = "India"

# creating object from Coffe
filer_coffe = Coffee()
print(filer_coffe.origin)


class Chaicup:
    size = 150 #ml

    def describe(self):   # self -> refernce to all object inside class
        return f"A {self.size} ml chai cup"


cup = Chaicup()
print(cup.describe())