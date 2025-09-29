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

start_date = datetime(2024, 10, 1, 9, 0, 0)
end_time = timedelta(hours=17)
num_days = 273
min_entries = 10
max_entries = 50

order_id = 0

for d in range(num_days):
    num_entries = random.randint(min_entries, max_entries)
    daily_start = start_date + timedelta(days=d)
    day_end = datetime.combine(daily_start.date(), (datetime.min + end_time).time())

    seconds_range = int((day_end-daily_start).total_seconds())

    offset = sorted(random.sample(range(seconds_range), num_entries))

    for o in offset:
        ts = daily_start + timedelta(seconds=o)
        selected_drink = list(drinks.keys())[random.randint(0,15)]
        bal = drinks[selected_drink]
        iter_arr = [order_id, selected_drink, bal, ts.strftime("%Y-%m-%d %H:%M:%S")]
        data.append(iter_arr)
        order_id += 1
        # print(iter_arr)

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


# for i in range(0, 1000):
    
    # date = random_datetime("2024-10-01 09:00:00", "2025-10-01 17:00:00")
    # iter_arr = {i, selected_drink, bal, date}
    # print(i, selected_drink, bal, date)