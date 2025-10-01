import random
import csv
from datetime import datetime, timedelta
import psycopg2

items = [
    (1, "Tapioca Pearls", (2000, 5000)),     
    (2, "Tea Leaves", (500, 1500)),            
    (3, "Milk", (8, 20)),                     
    (4, "Creamer", (5, 15)),                   
    (5, "Sugar", (2000, 5000)),                
    (6, "Cups", (200, 500)),              
    (7, "Straws", (200, 500)),            
    (8, "Brown Sugar Syrup", (2, 6)),          
    (9, "Fruit Syrup - Mango", (1, 4)),        
    (10, "Fruit Syrup - Strawberry", (1, 4)),  
    (11, "Taro Powder", (500, 1500)),         
    (12, "Matcha Powder", (300, 1000)),        
    (13, "Condensed Milk", (5, 15)),        
    (14, "Ice", (20, 60)), 
    (15, "Coffee Powder", (500, 1500)),       
    (16, "Ice Cream", (2, 5)),             
    (17, "Honey Syrup", (1, 3)),              
    (18, "Pudding Mix", (500, 1000)),         
    (19, "Fruit Syrup - Peach", (1, 4)),      
    (20, "Fruit Syrup - Lemon", (1, 4))       
]

rows = []

for itemID, name, (min_q, max_q) in items:
  quantity = random.randint(min_q, max_q)
  cost_per_unit = round(random.uniform(0.01, 0.2),2)

  expiration_date = datetime.now() + timedelta(days=random.randint(3, 30))
  reorder_date = datetime.now() - timedelta(days=random.randint(0, 3))

  rows.append({
        "itemID": itemID,
        "itemName": name,
        "quantity": f"{quantity}",
        "cost": cost_per_unit,
        "expirationDate": expiration_date.date(),
        "reorderDate": reorder_date.date()
    })

csv_filename = "onHandInventory.csv"
with open(csv_filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["itemID", "itemName", "quantity", "cost", "expirationDate", "reorderDate"]
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Onhandinventory csv generated successfully.")

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()

with open("onHandInventory.csv", "r") as f:
  next(f)
  cur.copy_from(f, "onhandinventory", sep=",")

conn.commit()
cur.close()
conn.close()

print("Onhandinventory table populated successfully.")
