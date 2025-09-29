import spycopg2

conn = psycopg2.connect(
    database="gang_94_db",
    user='gang_94',
    password='gang_94',
    host='csce-315-db-engr.tamu.edu',
    port='5432'
)

cursor = conn.cursor()

insert_query = """
INSERT INTO onHandInventory(quantiy, Cost, expiration, reorderDate)
VALUES (%s, %s, %s, %s)
"""
data = [(25, )]

cur.execute(insert_query, data)

conn.commit

cur.close()
conn.close()