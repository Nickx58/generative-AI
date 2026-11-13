beer_order = dict(type = "Wheat Beer", size="Large", brand = "Bira")
print(f"Beer Type: {beer_order}")

maggie_recipe = {}

maggie_recipe["water"] = "hot"
maggie_recipe["massala"] = "extra"
maggie_recipe["noddles"] = "long-type"

print(f"Maggie: {maggie_recipe}")
del maggie_recipe["massala"]
print(f"Maggie: {maggie_recipe}")
