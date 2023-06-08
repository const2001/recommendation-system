import json
from kafka import KafkaConsumer
from DatabaseManager import addUserToDatabase, getDbCursor, connectPostgressDatabase, DatabaseConnection
import os

def save_users_to_DB():
    conn = DatabaseConnection().get_connection()
    bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
    # Kafka Consumer
    consumerOfUsers = KafkaConsumer(
        'users',
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    try:
        # Insert producer's messages (users) into Postgres database
        for message in consumerOfUsers:
            user_data = message.value
            if user_data is not None:
                addUserToDatabase(user_data, conn)
                print(user_data)
    
    except KeyboardInterrupt:
        # Close the consumer upon keyboard interrupt
        consumerOfUsers.close()
        DatabaseConnection.close_connection()
       # conn.close()
        print("Consumer stopped.")

if __name__ == '__main__':
    save_users_to_DB()

