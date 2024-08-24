# Image Processing Pipeline with Apache Kafka

This repository contains an image processing pipeline built using Apache Kafka, Flask, and OpenCV. As part of Kafka module at Data Engineering Track at ITI.

## Project Overview

The pipeline is designed to:
1. **Handle Image Uploads**: A Flask server accepts image uploads and validates them.
2. **Publish Messages to Kafka**: Upon successful upload, the server sends a message to a Kafka topic, and if there is an error also send to error-topic Topic in kafka
3. **Process Images**:
   - **Random Image Classification**: A Kafka consumer simulates image classification usnig random function to test not real model.
   - **Grayscale Conversion**: Another Kafka consumer processes images to grayscale using OpenCV.

## Usage

1. **Upload an Image**: Send a `POST` request to `http://localhost:5000/` with an image file.
2. if the image will upload and send success message to kafka, and if not it will display simple alert and send failed message to kafka topic.
3. **View Processed Results**: Check the specified output directories for classification results and grayscale images.
## Components

### Flask Server
- **Function**: Accepts image uploads, validates the file format, saves the image, and sends a message to Kafka.
- **Endpoint**: `POST /upload` – Uploads an image and initiates processing.

### Kafka Producer
- **Function**: Publishes image upload events to a Kafka topics.

### Kafka Consumers
- **Random Image Classification Consumer**: Listens to the Kafka topic and performs simulated classification.
- **Grayscale Conversion Consumer**: Converts images to grayscale and saves the processed images.

## Technologies Used

- **Apache Kafka**: For message brokering and event handling.
- **Flask**: To create the web server and handle image uploads.
- **OpenCV**: For image processing tasks.
- **Python**: Programming language used for all components.

## Getting Started

### Prerequisites

- Kafka and Zookeeper installed and running.
- Python 3
- Required Python packages: `flask`, `kafka-python`, `opencv-python`

**Run the Flask server**:
   ```bash
   python server.py
   ```
**Start Kafka Consumers**:
   - **Random Image Classification**:
     ```bash
     python consumer-1.py
     ```
   - **Grayscale Conversion**:
     ```bash
     python consumer-2.py
     ```



