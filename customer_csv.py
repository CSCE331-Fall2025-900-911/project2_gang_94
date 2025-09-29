import csv
import pandas as pd
import random
from datetime import datetime, timedelta

data = [
    ['orderid', 'itemsused', 'balancespent', 'orderdate']
]

drinks = {'Pearl Milk Tea': 5.99, 'Fresh Matcha': 4.99, 'Lemonade': 3.99, 'Peach Tea': 4.99, 'Iced Tea': 3.99,
          'Strawberry Matcha': 5.99, 'Halo Halo': 4.99, 'Tiger Boba': 5.99, 'Oolong Tea': 3.99, 'Black Tea': 3.99,
          'Green Tea': 3.99, 'Green Honey Tea': 4.99, 'Black Honey Tea': 4.99, 'Coffee Milk Tea': 5.99,
           'Thai Pearl Milk Tea': 5.99, 'Coffee Crema': 5.99}

toppings = {}


# Start of dataset
start_date = datetime(2024, 10, 1, 9, 0, 0)
# Ends each day
end_time = timedelta(hours=17)
num_days = 273
min_daily_entries = 20
max_daily_entries = 300
seconds_gap = 45

order_id = 0

for d in range(num_days):
    # Generates how many orders will be placed each day
    
    # Date + offset of loop variable
    daily_start = start_date + timedelta(days=d)
    
    # First parameter is date, last is time
    day_end = datetime.combine(daily_start.date(), (datetime.min + end_time).time())

    # Sets reasonable gap between orders
    seconds_range = int((day_end-daily_start).total_seconds())
    max_given_time = seconds_range // seconds_gap

    # Number of entries per day bounded by possible amount of time (9 am - 5 pm)
    num_entries = min(random.randint(min_daily_entries, max_daily_entries), max_given_time)

    # Random offset 
    offset = sorted(random.sample(range(max_given_time), num_entries))

    for o in offset:
        # Creates timestamp within day
        ts = daily_start + timedelta(seconds=o*seconds_gap)
        selected_drink = list(drinks.keys())[random.randint(0,15)]
        bal = drinks[selected_drink]
        # Formats datetime object as readable string
        iter_arr = [order_id, selected_drink, bal, ts.strftime("%Y-%m-%d %H:%M:%S")]
        data.append(iter_arr)
        order_id += 1
        # print(iter_arr)

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
