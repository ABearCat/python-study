from pprint import pprint
import json
import random


with open('nested.json', 'r', encoding='utf-8') as data:
    donuts = json.load(data)

batters = []
toppings = []

for donut in donuts:
    currentDonut = donut
    for currentBatter in currentDonut["batters"]["batter"]:
        batter_type = currentBatter["type"]
        if batter_type not in batters:
            batters.append({"batter": batter_type})
    for currentTopping in currentDonut["topping"]:
        topping_type = currentTopping["type"]
        if topping_type not in toppings:
            toppings.append({"topping": topping_type})

#Pulls the list of batters available
with open('batters.json', 'w', encoding='utf-8') as output:
    json.dump(batters, output, indent = 4)

#Pulls the list of toppings available
with open('toppings.json', 'w', encoding='utf-8') as output:
    json.dump(toppings, output, indent = 4)

