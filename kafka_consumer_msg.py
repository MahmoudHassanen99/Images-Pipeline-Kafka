from confluent_kafka import Consumer, KafkaError


me = 'MahmoudHassanen-1'
groupid=me+'group'
# Kafka configuration
conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',
    'group.id': 'test-group',
    'auto.offset.reset': 'smallest',  # Change to 'earliest' to process all messages from the beginning
    'max.poll.interval.ms': 600000 
}

# Create Consumer instance
consumer = Consumer(conf)

# Define topics
ERROR_TOPIC = 'MahmoudHassanen-1error-topic'
COMPLETED_TOPIC = 'MahmoudHassanen-1'

# Subscribe to topics
consumer.subscribe([ERROR_TOPIC, COMPLETED_TOPIC])

def consume_messages():
    messages = {'errors': [], 'completed': []}
    
    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll for messages
            if msg is None:
                continue  # No message available

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue  # End of partition
                else:
                    print(f"Error: {msg.error()}")
                    continue
            
            # Process the message
            if msg.topic() == ERROR_TOPIC:
                messages['errors'].append(msg.value().decode('utf-8'))
            elif msg.topic() == COMPLETED_TOPIC:
                messages['completed'].append(msg.value().decode('utf-8'))
            
            # Print messages for debugging
            print("Errors:", messages['errors'])
            print("Completed:", messages['completed'])
    
    except KeyboardInterrupt:
        print("Consumer interrupted")
    
    finally:
        consumer.close()  # Close the consumer connection

if __name__ == "__main__":
    consume_messages()
    