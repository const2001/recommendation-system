import json
from kafka import KafkaProducer
from RandomGenerators import generate_user,generate_event,generate_coupon
import time
import os


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')
bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=serializer
)


try:   
  while True:    
        producer.send('users',generate_user())
        producer.send('events',generate_event())
        producer.send('coupons',generate_coupon())
        time.sleep(10)
        

except KeyboardInterrupt:
        print("Stopping the producer.") 
        producer.flush()      
        producer.close()   
      
      

        