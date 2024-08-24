from confluent_kafka import Consumer, KafkaError, KafkaException, Producer
import json, cv2, os
import numpy as np
import base64, sys, requests


me = 'MahmoudHassanen-1'
topics = [me]
ERROR_TOPIC = me + 'error-topic'
groupid = me + 'group'

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',
    'group.id': groupid,
    'enable.auto.commit': True,
    'auto.offset.reset': 'smallest'
}

producer_conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094'
}
producer = Producer(producer_conf)

consumer = Consumer(conf)
consumer.subscribe(topics)

IMAGES_DIR = 'images'  # where images are stored
PROCESSED_DIR = 'processed_grey'  # processed grey images will be saved
if not os.path.exists(PROCESSED_DIR):
    os.mkdir(PROCESSED_DIR)

def process_image(msg):
    try:
        # Parse the message
        message_data = json.loads(msg.value().decode('utf-8'))
        image_id = message_data.get('id')
        if not image_id:
            raise ValueError("Message does not contain 'id'")
        # Construct the image path based on the ID
        image_path = os.path.join(IMAGES_DIR, f"{image_id}.jpeg")
        # Check if the file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image {image_path} not found")
        # Load the image
        img = cv2.imread(image_path)
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Save the processed image
        processed_image_path = os.path.join(PROCESSED_DIR, f"{image_id}_gray.jpeg")
        cv2.imwrite(processed_image_path, gray_img)

        print(f"Processed image for id: {image_id}")

    except Exception as e:
        print(f"Error processing message: {e}")
        # Send error message to error-topic
        # error_message = {"id": image_id if 'image_id' in locals() else None, "error": str(e)}
        producer.produce(ERROR_TOPIC, key=image_id if 'image_id' in locals() else None, value=json.dumps({"id": id, "status": "Failed"}))
        producer.flush()

def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue  # End of partition
                else:
                    raise KafkaException(msg.error())

            process_image(msg)

    except Exception as e:
        print(f"Error in consumer loop: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()