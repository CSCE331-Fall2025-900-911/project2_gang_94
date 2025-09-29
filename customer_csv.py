import csv
import random
import datetime

def random_datetime(start: str, end: str, dt_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Generate a random datetime between two datetimes.

    Args:
        start (str): Start datetime as string (e.g. "2025-01-01 08:00:00").
        end (str): End datetime as string (e.g. "2025-12-31 17:30:00").
        dt_format (str): Format of input/output datetime. Default = "%Y-%m-%d %H:%M:%S".

    Returns:
        str: Random datetime in given format.
    """
    # Convert strings to datetime objects
    start_dt = datetime.datetime.strptime(start, dt_format)
    end_dt = datetime.datetime.strptime(end, dt_format)

    # Convert to timestamps
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())

    # Pick random timestamp
    rand_ts = random.randint(start_ts, end_ts)

    # Convert back to datetime
    rand_dt = datetime.datetime.fromtimestamp(rand_ts)

    return rand_dt.strftime(dt_format)

data = [
    ['orderid', 'itemsused', 'balancespent', 'orderdate']
]

drinks = {'Pearl Milk Tea': 5.99, 'Fresh Matcha': 4.99, 'Lemonade': 3.99, 'Peach Tea': 4.99, 'Iced Tea': 3.99,
          'Strawberry Matcha': 5.99, 'Halo Halo': 4.99, 'Tiger Boba': 5.99, 'Oolong Tea': 3.99, 'Black Tea': 3.99,
          'Green Tea': 3.99, 'Green Honey Tea': 4.99, 'Black Honey Tea': 4.99, 'Coffee Milk Tea': 5.99,
           'Thai Pearl Milk Tea': 5.99, 'Coffee Crema': 5.99}

for i in range(0, 750000):
    selected_drink = list(drinks.keys())[random.randint(0,15)]
    bal = drinks[selected_drink]
    date = random_datetime("2023-01-01 09:00:00", "2025-01-01 17:00:00")
    iter_arr = {i, selected_drink, bal, date}
    print(i, selected_drink, bal, date)