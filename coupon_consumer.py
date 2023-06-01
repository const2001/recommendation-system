import json
from kafka import KafkaConsumer
from DatabaseManager import addCouponToDatabase, getDbCursor, connectPostgressDatabase, DatabaseConnection
import os


def save_coupons_to_DB():
    #conn = DatabaseConnection().get_connection()
    bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
    # Kafka Consumer
    consumerOfCoupons = KafkaConsumer(
        'events',
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    try:
        # Insert producer's messages (users) into Postgres database
        for message in consumerOfCoupons:
            coupon_data = message.value
            if coupon_data is not None:
                 #addCouponToDatabase(coupon_data, conn)
                 print(coupon_data)
    
    except KeyboardInterrupt:
        # Close the consumer upon keyboard interrupt
        consumerOfCoupons.close()
        #conn.close()
        print("Consumer stopped.")

if __name__ == '__main__':
    save_coupons_to_DB()
