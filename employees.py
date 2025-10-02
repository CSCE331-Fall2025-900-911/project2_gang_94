import random
from datetime import datetime, timedelta
import csv 
import psycopg2

# random employees names 
employees = [
    "Alice", "Arisu", "Usagi", "Chishiya", "Ann",
    "Bunda", "Mira", "Hannah", "Chota", "Niragi", "Jade"
]

# assign each employee a unique, consistent id
employee_ids = {name: idx+1 for idx, name in enumerate(employees)}

start_date = datetime(2024, 10, 1)  # starting date
num_days = 273  # generate 39 weeks of schedules
shifts_per_day = 1  # e.g., morning & evening shifts

data = [["employee_id", "name", "schedule_date", "hours_worked", "customers_served"]]

for d in range(num_days):
    schedule_date = start_date + timedelta(days=d)

    for _ in range(shifts_per_day):
        # Pick random employee
        name = random.choice(employees)
        emp_id = d  # get the fixed ID for this employee

        # Simulate hours worked (short vs long shifts)
        hours_worked = random.choice([4, 6, 8])

        # Customers served (based on hours worked)
        customers_served = random.randint(hours_worked * 5, hours_worked * 15)
        
        data.append([emp_id, name, schedule_date.strftime("%Y-%m-%d"), hours_worked, customers_served])

# Save to CSV
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("✅ Employee schedule data written to employees.csv")

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()
#insert csv data into postgreSQL database using copy_from
with open("employees.csv", "r") as f:
  next(f)
  cur.copy_from(f, "employees", sep=",")

#commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("employees table populated successfully.")
