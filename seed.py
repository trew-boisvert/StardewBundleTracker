import os
import json
from random import choice, randint
from datetime import datetime

import model
import server

os.system("dropdb stardew")
os.system("createdb stardew")

model.connect_to_db(server.app)
model.db.create_all()

trew = model.User(screenname="trew-vaille", password="test")

model.db.session.add(trew)
model.db.session.commit()

farm = model.SaveFile(user_id=1, farm_name="Pipa Farm")

model.db.session.add(farm)
model.db.session.commit()

items = [
        {
            'item_name': "Wild Horseradish",
            'bundle_name': "Spring Foraging Bundle",
            'seasons_available': "spring",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Daffodil",
            'bundle_name': "Spring Foraging Bundle",
            'seasons_available': "spring",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Leek",
            'bundle_name': "Spring Foraging Bundle",
            'seasons_available': "spring",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Dandelion",
            'bundle_name': "Spring Foraging Bundle",
            'seasons_available': "spring",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Grape",
            'bundle_name': "Summer Foraging Bundle",
            'seasons_available': "summerfall",
            'locations_available': "outside anywhere but beach in summer",
            'conditions_available': "also fall farming"
        },
        {
            'item_name': "Spice Berry",
            'bundle_name': "Summer Foraging Bundle",
            'seasons_available': "summer",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "also Farm Cave (fruit bat option)"
        },
        {
            'item_name': "Sweet Pea",
            'bundle_name': "Summer Foraging Bundle",
            'seasons_available': "summer",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Common Mushroom",
            'bundle_name': "Fall Foraging Bundle",
            'seasons_available': "springfall",
            'locations_available': "Secret woods",
            'conditions_available': "also Farm Cave(mushroom option) and tapping a Mushroom Tree"
        },
        {
            'item_name': "Wild Plum",
            'bundle_name': "Fall Foraging Bundle",
            'seasons_available': "fall",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "also Farm Cave (fruit bat option)"
        },
        {
            'item_name': "Hazelnut",
            'bundle_name': "Fall Foraging Bundle",
            'seasons_available': "fall",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Blackberry",
            'bundle_name': "Fall Foraging Bundle",
            'seasons_available': "fall",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "also Farm Cave (fruit bat option)" 
        },
        {
            'item_name': "Winter Root",
            'bundle_name': "Winter Foraging Bundle",
            'seasons_available': "winterall",
            'locations_available': "tilling soil or artifact spots in winter",
            'conditions_available': "dropped by Blue Slimes on floors 41-79 of The Mines"
        },
        {
            'item_name': "Crystal Fruit",
            'bundle_name': "Winter Foraging Bundle",
            'seasons_available': "winterall",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "dropped by Dust Sprites on floors 41-79 of The Mines" 
        },
        {
            'item_name': "Snow Yam",
            'bundle_name': "Winter Foraging Bundle",
            'seasons_available': "winter",
            'locations_available': "tilling soil or artifact spots in winter",
            'conditions_available': "no special conditions"
        },
        {
            'item_name': "Crocus",
            'bundle_name': "Winter Foraging Bundle",
            'seasons_available': "winter",
            'locations_available': "outside anywhere but beach",
            'conditions_available': "no special conditions"
        }

]

for item in items:
    new_item = model.Item(item_name=item["item_name"], bundle_name=item["bundle_name"], seasons_available=item["seasons_available"], locations_available=item["locations_available"], conditions_available=item["conditions_available"])
    model.db.session.add(new_item)
    model.db.session.commit()