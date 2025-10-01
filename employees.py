import random
from datetime import datetime, timedelta
import csv 

# ramdon employees names 
employees = [
    "Alice", "Arisu", "Usagi", "Chishiya", "Ann",
    "Bunda", "Mira", "Hannah", "Chota", "Niragi","Jade"
]

start_date = datetime(2024, 10, 1)  # starting date
num_days = 273  # generate 39 weeks of schedules
shifts_per_day = 1  # e.g., morning & evening shifts

data = [["employee_id", "name", "schedule_date", "hours_worked", "customers_served"]]

emp_id = 2

for d in range(num_days):
    schedule_date = start_date + timedelta(days=d)

    for _ in range(shifts_per_day):
        # Pick random employee
        name = random.choice(employees)

        # Simulate hours worked (short vs long shifts)
        hours_worked = random.choice([4, 6, 8])

        # Customers served (based on hours worked)
        customers_served = random.randint(hours_worked * 5, hours_worked * 15)
        data.append([emp_id, name, schedule_date.strftime("%Y-%m-%d"), hours_worked, customers_served])
        emp_id += 1

# Save to CSV
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("✅ Employee schedule data written to employees.csv")
