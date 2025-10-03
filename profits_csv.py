import csv
import random
from datetime import datetime, timedelta
import psycopg2

data = [['start_date', 'total_sales', 'total_expenses', 'profit_change']]

sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
expenses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('customers.csv', 'r', newline='') as f_read:
    reader = csv.reader(f_read)

    for row in reader:
        # Skips header
        if (row[3] == 'order_date'):
            continue
        stamp = row[3]
        # Formats date for easier access
        dt = datetime.strptime(stamp, "%Y-%m-%d %H:%M:%S")
        sales[dt.month - 1] += float(row[2])

# Start based on customer_csv.py
month = 10
year = 2024
for i in range(len(sales)):
    # Skips dates with no sales (range is less than a year)
    if (sales[month-1] == 0):
        continue
    expenses[month-1] = random.uniform(4000, 5000)
    iter_arr = [f"{year}-{month}-01", round(sales[month-1],2), round(expenses[month-1], 2), 0]
    # Finds change in profits if the previous month had sales
    if (sales[month-2] > 0):
        iter_arr[3] = round((sales[month-1] - expenses[month-1]) - (sales[month-2] - expenses[month-2]),2)
    data.append(iter_arr)
    month += 1
    # Updates date
    if (month > 12):
        month = 1
        year += 1

# print(data)

with open('profits.csv', 'w', newline='') as f_write:
    writer = csv.writer(f_write)
    writer.writerows(data)

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db.engr.tamu.edu',
    port='5432'
)

cur = conn.cursor()
#insert csv data into postgreSQL database using copy_from
with open("profits.csv", "r") as f:
  next(f)
  cur.copy_from(f, "profits", sep=",")

#commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("profits table populated successfully.")





