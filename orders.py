import json
import time
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 100

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Will generate one unique order every 0.5 seconds")
time.sleep(0.5)

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"random_{i}",
        "total_cost": i * 5,
        "items": "item1, item2",
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(0.5)