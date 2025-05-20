# 🛒 Commercial Smart Shelf: An AIoT Approach

This project presents a smart retail shelf system that automates stock monitoring using AI and IoT. Built using a microcontroller with a camera module and a custom-trained object detection model, the system captures shelf images at regular intervals, detects product types and quantities, and sends low-stock alerts via push notifications.

## 📌 Project Overview

Traditional "smart" retail systems often rely on manual checks to manage inventory. Our system eliminates manual intervention by combining AI-based object detection with IoT devices to automatically monitor and report stock levels.

### 🎯 Key Features
- Real-time shelf image capture using ESP32 Xiao and camera module.
- Custom object detection model (trained with Roboflow) to identify and count products.
- Flask backend to process image data and manage stock thresholds.
- Push notification alerts when product stock falls below set levels.
- Precision: 80.9% | Recall: 100%

## 🧠 Technologies Used
- **Hardware**: ESP32 Xiao (Microcontroller), Camera Module
- **Software**: Python, Flask
- **Machine Learning**: Custom Object Detection Model via Roboflow
- **Communication**: HTTP requests from ESP32 to Flask server
- **Notifications**: Pushbullet API

## 📷 How It Works
1. ESP32 captures an image of the shelf at set intervals.
2. Image is sent to the Flask server.
3. Flask server uses a Roboflow model to detect and count products.
4. If product quantity is below threshold, a push notification is sent.

