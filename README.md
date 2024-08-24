# Image Processing Pipeline with Apache Kafka

This repository contains an image processing pipeline built using Apache Kafka, Flask, and OpenCV. As part of Kafka module at Data Engineering Track at ITI.

## Project Overview

This pipeline does the following:
- **Handles Image Uploads:** A Flask server accepts and validates image uploads.
- **Publishes Messages to Kafka:** After a successful upload, the server sends a message to a Kafka topic. If there’s an error, a message is sent to an `error-topic` in Kafka.
- **Processes Images:**
  - **Random Image Classification:** A Kafka consumer simulates image classification using a random function (not a real model).
  - **Grayscale Conversion:** Another Kafka consumer converts images to grayscale using OpenCV.

## Usage

1. **Upload an Image:**
   - Send a `POST` request to `http://localhost:5000/upload` with your image file.
   - If the upload is successful, a success message is sent to Kafka. If the upload fails, an alert is displayed and a failure message is sent to Kafka.

2. **View Processed Results:**
   - Check the specified output directories for classification results and grayscale images.

3. **Display Success and Failure Messages:**
   - Send a `POST` request to `http://localhost:5000/messages` to view the success and failure messages.

## Components

- **Flask Server:**
  - **Function:** Manages image uploads, validates file formats, saves images, and sends messages to Kafka.
  - **Endpoint:** `POST /upload` – Uploads an image and starts processing.

- **Kafka Producer:**
  - **Function:** Publishes image upload events to Kafka topics.

- **Kafka Consumers:**
  - **Random Image Classification Consumer:** Listens to the Kafka topic and performs simulated classification.
  - **Grayscale Conversion Consumer:** Converts images to grayscale and saves the results.

- **Message Display Function:**
  - **Function:** Displays success and failure messages from Kafka.

## Technologies Used

- **Apache Kafka:** For message brokering and event handling.
- **Flask:** For creating the web server and handling image uploads.
- **OpenCV:** For image processing tasks.
- **Python:** The programming language used for all components.

## Getting Started

### Prerequisites

- Kafka and Zookeeper installed and running.
- Python 3.x
- Required Python packages: `flask`, `kafka-python`, `opencv-python`

### Installation and Running

1. **Run the Flask Server:**
   ```bash
   python server.py
   ```

2. **Start Kafka Consumers:**
   - **Random Image Classification:**
     ```bash
     python consumer-1.py
     ```
   - **Grayscale Conversion:**
     ```bash
     python consumer-2.py
     ```

