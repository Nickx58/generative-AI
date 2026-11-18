def north_food():
    yield "Dal Makhni"
    yield "Panner Butter"

def south_food():
    yield "Dosa"
    yield "Biryani"

def full_menu():
    yield from north_food()
    yield from south_food()

for food in full_menu():
    print(food)
