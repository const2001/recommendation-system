import psycopg2


def connectPostgressDatabase():
    conn = psycopg2.connect(
        dbname="tuzrhmmv",
        user="tuzrhmmv",
        password="Hbcfv140k9-i19CRLWzazb3A5jOxHrci",
        host="isilo.db.elephantsql.com",
        port="5432",
    )
    return conn


def getDbCursor(conn):
    cursor = conn.cursor()
    return cursor


def getDbHostPort(cursor):
    cursor.execute("SELECT * FROM pg_settings WHERE name = 'port';")
    rows = cursor.fetchall()
    return rows


def addUserToDatabase(user_data):
    sql = """
    INSERT INTO users (birth_year, country, currency, gender, sport_pref, registration_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    conn = connectPostgressDatabase()
    curr = getDbCursor(conn)
    curr.execute(
        sql,
        (
            user_data["birth_year"],
            user_data["country"],
            user_data["currency"],
            user_data["gender"],
            user_data["sport_pref"],
            user_data["registration_date"],
        ),
    )
    conn.commit()
    curr.close()
    conn.close()


# Test database

if __name__ == "__main__":
    user_data = {
        "birth_year": 1991,
        "gender": "Male",
        "country": "Italy",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    }
    addUserToDatabase(user_data)

#     curr = getDbCursor(conn)
#     port = getDbHostPort(curr)
#     print(port)
