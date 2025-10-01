import random
import csv
from datetime import datetime, timedelta
import psycopg2

machines = [
  (1, "Tapioca Cooker"),
  (2, "Tea Brewer"),
  (3, "Ice Machine"),
  (4, "Sealing Machine"),
  (5, "Blender"),
  (6, "POS System"),
  (7, "Fridge/Freezer"),
  (8, "Water Boiler"),
  (9, "Shaker Machine"),
  (10, "Syrup Dispenser")
]

comments = [
    "Replaced worn parts",
    "Calibrated machine",
    "Fixed leakage issue",
    "Software update applied",
    "Routine check completed",
    "Motor replaced",
    "Filter cleaned",
    "Electrical wiring fixed",
    "Lubricated moving parts",
    "Temperature sensor replaced"
]
rows = []

for menuID, name in machines:
    last_repair = datetime.now() - timedelta(days=random.randint(1, 180))
    comment = random.choice(comments)
    repair_cost = round(random.uniform(20, 300), 2)

    rows.append({
        "MenuID": menuID,          
        "MachineName": name,          
        "LastRepair": last_repair.date(),
        "FunctionComments": comment,
        "CostOfRepair": repair_cost
    })


csv_filename = "maintenance.csv"
with open(csv_filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["MenuID", "MachineName", "LastRepair", "FunctionComments", "CostOfRepair"]
    )
    writer.writeheader()
    writer.writerows(rows)

print("Maintenance csv generated successfully!")

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()

with open("maintenance.csv", "r") as f1:
  next(f1)
  cur.copy_from(f1, "maintenance", sep=",")

conn.commit()
cur.close()
conn.close()

print("Maintenance table populated.")


