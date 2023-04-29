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


def addEventToDatabase(event_data):
    sql = """
    INSERT INTO events (event_id, begin_timestamp, country, end_timestamp, league, participants, sport)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
    conn = connectPostgressDatabase()
    curr = getDbCursor(conn)
    curr.execute(
        sql,
        (
            event_data["event_id"],
            event_data["begin_timestamp"],
            event_data["country"],
            event_data["end_timestamp"],
            event_data["league"],
            event_data["participants"],
            event_data["sport"],
        ),
    )
    conn.commit()
    curr.close()
    conn.close()


def addCouponToDatabase(coupon_data):
    sql = """
    INSERT INTO coupons (coupon_id, selections, stake, timestamp, user_id)
    VALUES (%s, %s, %s, %s, %s)
    """
    conn = connectPostgressDatabase()
    curr = getDbCursor(conn)
    curr.execute(sql, (coupon_data['coupon_id'], coupon_data['selections'], coupon_data['stake'], coupon_data['timestamp'], coupon_data['user_id']))

    conn.commit()
    curr.close()
    conn.close()


# Test database

if __name__ == "__main__":
    user_data = {
        "birth_year": 1990,
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
