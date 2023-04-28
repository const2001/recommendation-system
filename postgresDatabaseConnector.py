import psycopg2

conn = psycopg2.connect(
    dbname="tuzrhmmv",
    user="tuzrhmmv",
    password="Hbcfv140k9-i19CRLWzazb3A5jOxHrci",
    host="isilo.db.elephantsql.com",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM pg_settings WHERE name = 'port';")
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

cur.close()
conn.close()