import json
from kafka import KafkaConsumer
from DatabaseManager import addEventToDatabase,getDbCursor,connectPostgressDatabase,DatabaseConnection




def save_events_to_DB():
    conn = DatabaseConnection().get_connection()
    for message in consumerOfEvents:
        event_data = json.loads(message.value)
        if event_data is not None:
               for event in event_data:
                print(event)  
                addEventToDatabase(event,conn)


if __name__ == '__main__':
    consumerOfEvents = KafkaConsumer(
        'events',
        bootstrap_servers='localost:9092',
        auto_offset_reset='earliest'
    )

    save_events_to_DB()