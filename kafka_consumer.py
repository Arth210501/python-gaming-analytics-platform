from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'analytics_group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['game_events'])


def consume_game_event():
    msg = c.poll(1.0)
    if msg is None:
        return
    if msg.error():
        print(f"Consumer error: {msg.error()}")
    else:
        print(f"Consumed message: {msg.value().decode('utf-8')}")
