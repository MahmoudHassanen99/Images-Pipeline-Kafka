from confluent_kafka.admin import NewTopic, AdminClient,KafkaException
import logging
conf = {
    'bootstrap.servers': 'localhost:9092',
}
admin_client = AdminClient(conf)

# Define the topic configuration
me = 'MahmoudHassanen-1'
me_error=me+'error-topic'
num_partitions = 3
replication_factor = 1

# Create a NewTopic object with the desired configuration
new_topic = NewTopic(me, num_partitions=num_partitions, replication_factor=replication_factor)

error_topic = NewTopic(me_error, num_partitions=num_partitions, replication_factor=replication_factor)

# Add the new topic to the Kafka admin client
admin_client.create_topics([new_topic])[me].result()

admin_client.create_topics([error_topic])[me_error].result()


admin_client = AdminClient(conf)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

current_topics = admin_client.list_topics(timeout=10).topics
existing_topics = set(current_topics.keys())
logger.info(f"Existing topics: {existing_topics}")
