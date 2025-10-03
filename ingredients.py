import random
import csv
from datetime import datetime, timedelta
import psycopg2

#list of ingredients
items = [
    (1, "Tapioca Pearls", (20000, 50000)),
    (2, "Tea Leaves", (5000, 15000)),
    (3, "Milk", (80, 200)),
    (4, "Creamer", (50, 150)),
    (5, "Sugar", (20000, 50000)),
    (6, "Cups", (2000, 5000)),
    (7, "Straws", (2000, 5000)),
    (8, "Brown Sugar Syrup", (20, 60)),
    (9, "Fruit Syrup - Mango", (10, 40)),
    (10, "Fruit Syrup - Strawberry", (10, 40)),
    (11, "Taro Powder", (5000, 15000)),
    (12, "Matcha Powder", (3000, 10000)),
    (13, "Condensed Milk", (50, 150)),
    (14, "Ice", (200, 600)),
    (15, "Coffee Powder", (5000, 15000)),
    (16, "Ice Cream", (20, 50)),
    (17, "Honey Syrup", (10, 30)),
    (18, "Pudding Mix", (5000, 10000)),
    (19, "Fruit Syrup - Peach", (10, 40)),
    (20, "Fruit Syrup - Lemon", (10, 40))
]

#generate ingredients data
ingredient_rows = []

for itemID, name, (min_q, max_q) in items:
    quantity = random.randint(min_q, max_q)
    cost_per_unit = round(random.uniform(0.01, 0.2), 2)
    expiration_date = datetime.now() + timedelta(days=random.randint(5, 40))
    reorder_date = datetime.now() - timedelta(days=random.randint(0, 5))

    ingredient_rows.append({
        "item_id": itemID,
        "quantity": quantity,
        "cost": cost_per_unit,
        "expiration": expiration_date.date(),
        "estimated_reorder_date": reorder_date.date()
    })

with open("ingredients.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["item_id", "quantity", "cost", "expiration", "estimated_reorder_date"]
    )
    writer.writeheader()
    writer.writerows(ingredient_rows)

print("ingredients.csv generated successfully.")

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()

# load Ingredients and insert into postgreSQL database using copy from
with open("ingredients.csv", "r") as f:
    next(f)
    cur.copy_from(f, "ingredients", sep=",")

conn.commit()
cur.close()
conn.close()