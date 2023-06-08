import json
from kafka import KafkaConsumer
from DatabaseManager import addEventToDatabase, getDbCursor, connectPostgressDatabase, DatabaseConnection
import os


def save_events_to_DB():
    conn = DatabaseConnection().get_connection()
    bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
    # Kafka Consumer
    consumerOfEvents = KafkaConsumer(
        'events',
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    try:
        # Insert producer's messages (users) into Postgres database
        for message in consumerOfEvents:
            event_data = message.value
            if event_data is not None:
                 addEventToDatabase(event_data, conn)
                 print(event_data)
    
    except KeyboardInterrupt:
        # Close the consumer upon keyboard interrupt
        consumerOfEvents.close()
        DatabaseConnection.close_connection()
        print("Consumer stopped.")

if __name__ == '__main__':
    save_events_to_DB()
