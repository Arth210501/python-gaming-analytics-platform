from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def produce_game_event(event):
    p.produce('game_events', value=event, callback=delivery_report)
    p.flush()
