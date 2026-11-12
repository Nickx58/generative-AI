cars_brand = {"maruti", "hyndai", "kia", "bmw", "skoda"}
reliable_brand = {"tata", "bmw", "skoda", "mahindra"}

set_brands = cars_brand | reliable_brand

print(f"Car Brands that are good: {set_brands}")

print(f"Check if 'bmw' is in car brand? {'bmw' in set_brands}" )