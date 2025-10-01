import csv
import pandas as pd
import random
from datetime import datetime, timedelta

data = [
    ['orderid', 'itemsused', 'balancespent', 'orderdate']
]

drinks = {'Pearl Milk Tea': 5.80, 'Fresh Matcha': 6.25, 'Lemonade': 5.20, 'Peach Tea': 6.25, 'Iced Thai Tea': 6.75,
          'Strawberry Matcha': 6.50, 'Halo Halo': 6.95, 'Tiger Boba': 6.50, 'Oolong Tea': 4.65, 'Black Tea': 4.65,
          'Green Tea': 4.65, 'Green Honey Tea': 4.85, 'Black Honey Tea': 4.85, 'Coffee Milk Tea': 6.25,
           'Thai Pearl Milk Tea': 6.25, 'Coffee Crema': 6.50}

toppings = {'Boba Pearls': .75, 'Ice Cream': 1.00, 'Honey Jelly': .75, 'Pudding': .75}


# Start of dataset
start_date = datetime(2024, 10, 1, 9, 0, 0)
# Ends each day
end_time = timedelta(hours=17)
num_days = 273
min_daily_entries = 20
max_daily_entries = 300
seconds_gap = 45

order_id = 0

peak_days = 1

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

    if (daily_start.month == 12 and daily_start.day == 25):
        num_entries = min(500, max_given_time)
    # Random offset 
    offset = sorted(random.sample(range(max_given_time), num_entries))

    for o in offset:
        # Creates timestamp within day
        ts = daily_start + timedelta(seconds=o*seconds_gap)
        num_drinks = random.randint(1,5) - 1
        selected_drink = list(drinks.keys())[random.randint(0,len(drinks) - 1)]
        bal = drinks[selected_drink]
        total_drinks = selected_drink

        num_toppings = random.randint(0,3)

        while (num_drinks > 0):
            selected_drink = list(drinks.keys())[random.randint(0,len(drinks) -1)]
            bal += drinks[selected_drink]
            if (num_toppings > 0):
                selected_topping = list(toppings.keys())[random.randint(0, len(toppings) - 1)]
                total_drinks += " (add " + selected_topping + ")"
                bal += toppings[selected_topping]
                num_toppings -= 1
            total_drinks += ", " + selected_drink
            num_drinks -= 1
        # Formats datetime object as readable string
        iter_arr = [order_id, total_drinks, round(bal,2), ts.strftime("%Y-%m-%d %H:%M:%S")]
        data.append(iter_arr)
        order_id += 1

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

profits = 0
for i in range(1, order_id):
    profits += data[i][2]

print(profits)


