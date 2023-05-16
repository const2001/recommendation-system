import json
from kafka import KafkaProducer
from FillDatabase import getDummyUsers,getDummyEvents


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':

    # Infinite loop - runs until you kill the program
        producer.send('users',getDummyUsers())
        producer.send('events',getDummyEvents())

        