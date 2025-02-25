import pika
from datetime import datetime

# Connection parameters
connection_params = pika.ConnectionParameters('10.10.1.62', 5672, '/', pika.PlainCredentials('test', 'test'))
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# List of routing keys corresponding to each consumer
routing_keys = ['key1', 'key2', 'key3']

# Send 10 messages in a loop, each message sent to a different consumer
for i in range(10):
    # Determine which consumer will receive the message
    routing_key = routing_keys[i % len(routing_keys)]  # Cycle through the consumers
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[{timestamp}] Message {i + 1}"

    # Send the message to the exchange
    channel.basic_publish(exchange='direct_logs', routing_key=routing_key, body=message)
    print(f" [x] Sent '{message}' with routing key '{routing_key}' at {timestamp}")

connection.close()
