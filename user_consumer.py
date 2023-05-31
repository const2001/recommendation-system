import json
from kafka import KafkaConsumer
from DatabaseManager import addUserToDatabase,getDbCursor,connectPostgressDatabase,DatabaseConnection


def save_users_to_DB():
    conn = DatabaseConnection().get_connection()
    #Insert producer's messages(users) in Postgres database
    for message in consumerOfUsers:
        user_data = json.loads(message.value)
        if user_data is not None:
            for user in user_data:  
                #print(user)  
                addUserToDatabase(user,conn)
 



if __name__ == '__main__':

    # Kafka Consumers
   
    consumerOfUsers = KafkaConsumer(
        'users',
        bootstrap_servers='localost:9092',
        auto_offset_reset='earliest'
    )

    save_users_to_DB()

  


