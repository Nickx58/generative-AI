chai_type = ["light", "strong", "ginger"]

strong_chai = list(filter(lambda chai: chai !="ginger",chai_type))
print(strong_chai)