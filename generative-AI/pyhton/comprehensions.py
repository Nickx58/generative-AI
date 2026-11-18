menu = [
    "Pav Bhaji",
    "Kulcha",
    "COffe",
    "Biryani"
]

pav_bhaji = [pav for pav in menu if "Pav Bhaji" in pav]
print(pav_bhaji)


fav_food = [
    "Dosa", "Pav","Dal", "Paneer", "Panner burzi", "Masala Dosa", "Dosa"
]

unique_food = {food for food in fav_food}
print(unique_food)

tea_price_inr = {
    "Masala Chai" : 40,
    "Green Tea" : 80,
    "Lemon Tea" : 60
}

tea_price_usd = {tea: price / 80 for tea, price in tea_price_inr.items()}
print(tea_price_usd)

