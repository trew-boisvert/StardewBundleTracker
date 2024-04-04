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