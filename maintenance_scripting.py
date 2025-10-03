import random
import csv
from datetime import datetime, timedelta
import psycopg2

# List of machines with IDs
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
# Maintenance comment
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

# Generate random maintenance records for each machine
for menu_id, name in machines:
    last_repair = datetime.now() - timedelta(days=random.randint(1, 180))
    comment = random.choice(comments)
    repair_cost = round(random.uniform(20, 300), 2)

    rows.append({
        "menu_id": menu_id,          
        "machine_name": name,          
        "last_repair": last_repair.date(),
        "function_comments": comment,
        "cost_of_repair": repair_cost
    })

#write maintenance data into csv
csv_filename = "maintenance.csv"
with open(csv_filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["menu_id", "machine_name", "last_repair", "function_comments", "cost_of_repair"]
    )
    writer.writeheader()
    writer.writerows(rows)

print("Maintenance csv generated successfully!")

#connect to database
conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()
#load data from csv to postgreSQL using copy_from
with open("maintenance.csv", "r") as f1:
  next(f1)
  cur.copy_from(f1, "maintenance", sep=",")

#commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Maintenance table populated.")


