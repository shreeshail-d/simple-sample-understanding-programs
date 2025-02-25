import pika
from datetime import datetime

# Connection parameters
connection_params = pika.ConnectionParameters('10.10.1.62', 5672, '/', pika.PlainCredentials('test', 'test'))
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare direct exchange and queue
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
queue_name = channel.queue_declare(queue='', exclusive=True).method.queue

# Bind the queue to the routing key for this consumer
routing_key = 'key2'
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=routing_key)

print(f" [*] Waiting for messages with routing key '{routing_key}'")

# Callback to process messages
def callback(ch, method, properties, body):
    receive_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f" [x] Received '{body.decode()}' with routing key '{method.routing_key}' at {receive_time}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
