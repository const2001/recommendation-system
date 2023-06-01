import json
from kafka import KafkaProducer
from RandomGenerators import generate_user,generate_event,generate_coupon
import time


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

bootstrap_servers = 'kafka1:9092,kafka2:9092,kafka3:9092'
# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=serializer
)


try:   # Infinite loop - runs until you kill the program
  while True:    
        producer.send('users',generate_user())
        producer.send('events',generate_event())
        producer.send('coupons',generate_coupon())
        
        time.sleep(10)
        

except KeyboardInterrupt:
        print("Stopping the producer.")   
      
finally:
      producer.flush()      
      producer.close() 

        