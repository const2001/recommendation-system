import json
import threading
from kafka import KafkaConsumer
from DatabaseManager import addUserToDatabase,addEventToDatabase


def save_users_to_DB():
    #Insert producer's messages(users) in Postgres database
    for message in consumerOfUsers:
        user_data = json.loads(message.value)
        if user_data is not None:
            for user in user_data:  
                print(user)  
                #addUserToDatabase(user)
 
def save_events_to_DB():
    #Insert producer's messages in Postgres
    for message in consumerOfEvents:
        event_data = json.loads(message.value)
        if event_data is not None:
               for event in event_data:
                print(event)  
                #addEventToDatabase(event)


if __name__ == '__main__':

    # Kafka Consumers
    consumerOfUsers = KafkaConsumer(
        'users',
        bootstrap_servers='localost:9092',
        auto_offset_reset='earliest'
    )

    consumerOfEvents = KafkaConsumer(
        'events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    save_users_to_DB()
    save_events_to_DB()
  


