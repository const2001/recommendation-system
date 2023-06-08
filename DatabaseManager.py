import psycopg2
import json



def connectPostgressDatabase():
    conn = psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
    )
    return conn

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "connection"):
            self.connection = connectPostgressDatabase()
    
    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        self.connection.close()


def getDbCursor(conn):
    cursor = conn.cursor()
    return cursor


def getDbHostPort(cursor):
    cursor.execute("SELECT * FROM pg_settings WHERE name = 'port';")
    rows = cursor.fetchall()
    return rows


def addUserToDatabase(user_data,connector = connectPostgressDatabase()):
    sql = """
    INSERT INTO users (birth_year, country, currency, gender, sport_pref, registration_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    conn = connector
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
    
    


def addEventToDatabase(event_data,connector = connectPostgressDatabase()):
    sql = """
    INSERT INTO events (begin_timestamp, country, end_timestamp, league, participants, sport)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
    conn = connector
    curr = getDbCursor(conn)
    curr.execute(
        sql,
        (
            
            event_data["begin_timestamp"],
            event_data["country"],
            event_data["end_timestamp"],
            event_data["league"],
            event_data["participants"],
            event_data["sport"],
        ),
    )
    conn.commit()
   
    


def addCouponToDatabase(coupon_data,connector = connectPostgressDatabase()):
    sql = """
    INSERT INTO coupons ( selections, stake, timestamp, user_id)
    VALUES (%s, %s, %s, %s)
    """
    coupon_selections = json.dumps(coupon_data['selections'])
    conn = connector
    curr = getDbCursor(conn)
    curr.execute(sql, (coupon_selections, coupon_data['stake'], coupon_data['timestamp'], coupon_data['user_id']))

    
    curr.close()
    

def getUsersFromDatabase(connector = connectPostgressDatabase()):
    sql = """
    SELECT user_id, birth_year, gender, country, sport_pref, currency, registration_date
    FROM users
    ORDER BY user_id
    """

    conn = connector
    curr = getDbCursor(conn)
    curr.execute(sql)

    users = []
    rows = curr.fetchall()

    for row in rows:
        user = {
            "user_id": row[0],
            "birth_year": row[1],
            "gender": row[2],
            "country": row[3],
            "sport_pref": row[4],
            "currency": row[5],
            "registration_date": row[6].isoformat()
        }
        users.append(user)

    curr.close()
    
    return users

def getEventsFromDatabase(connector = connectPostgressDatabase()):
    sql = """
    SELECT * FROM events
    ORDER BY event_id
    """

    conn = connector
    curr = getDbCursor(conn)
    curr.execute(sql)

    events = []
    rows = curr.fetchall()

    for row in rows:
        event = {
            "event_id": row[0],
            "league": row[4],
            "sport": row[6],
            "country": row[2],
            "begin_timestamp": row[1],
            "end_timestamp": row[3],
            "participants": row[5]
        }
        events.append(event)
    
    curr.close()
     
    return events    

def getCouponsFromDatabase(connector = connectPostgressDatabase()):
    sql = """
    SELECT * FROM coupons
    ORDER BY coupon_id
    """

    conn = connector
    curr = getDbCursor(conn)
    curr.execute(sql)

    coupons = []
    rows = curr.fetchall()

    for row in rows:
        coupon = {
            "coupon_id": row[0],
            "selections": row[4],
            "stake": float(row[1]),
            "timestamp": row[2],
            "user_id": row[3]
        }
        coupons.append(coupon)

    
    curr.close()
  
    return coupons


# Test database


if __name__ == "__main__":
    # coupons = getCouponsFromDatabase()
    # print(coupons)
    conn = DatabaseConnection().get_connection()
    curr = getDbCursor(conn)
    port = getDbHostPort(curr)
    conn.close()
    print(port)
