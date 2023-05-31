import json
from kafka import KafkaProducer
from RandomGenerators import generate_coupons


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
   producer.send('events',generate_coupons(20))