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

## Roboflow Object Detection Model
To enable the shelf system to automatically recognize and count products, we trained a custom object detection model using Roboflow.

Model URL: miniproject-cx2n2/my-first-project-j4pm9-instant-3

## 🔧 Hardware Required
-ESP32 Xiao (or any ESP32 with camera support)
-Camera Module (OV2640 or similar)
-USB cable for flashing

## ✅ Prerequisites
Hardware:
-ESP32-S3 or XIAO ESP32S3 Sense
-OV2640 camera module
-Micro-USB cable
-Wi-Fi access

Software:
-Arduino IDE with ESP32 board support
-Python 3.8+
-pip (Python package installer)
-Roboflow API key
-Pushbullet API key (for notifications)

## 🔧 Setup Instructions
Step 1: Set up the ESP32 Camera
Location: Camera Server/CameraWebServer_for_esp_arduino_3_0_x.ino
1.Open Arduino IDE.
2.Install the ESP32 board support package (via Board Manager).
3.Open CameraWebServer_for_esp_arduino_3_0_x.ino.
4.Ensure camera_index.h and camera_pins.h are in the same folder.
5.In camera_pins.h, uncomment the line for your camera model. For example:
#define CAMERA_MODEL_XIAO_ESP32S3
6.Edit the .ino file and add your Wi-Fi credentials and Flask server IP:

const char* ssid = "YourSSID";
const char* password = "YourPassword";
const char* serverUrl = "http://<your_computer_ip>:5000/uploads";

7.Upload the code to your ESP32 board.

Step 2: Run the Flask Server (Image Receiver)

1.Open a terminal and navigate to the Intergration/ folder.
2.Install Flask:

pip install flask

3.Run the server:

python int_server3.py

Step 3: Configure and Run

1.Open model.py and update:

-Your Roboflow API key
-Your Roboflow workspace and workflow ID
-Your Pushbullet API key

2.Update the path to the captured image:

filepath = "uploads/image.jpg"

3.Run the inference script:

python model.py

##🧪 How It Works
ESP32 Camera captures an image and sends it to the Flask server.

Flask server saves it in the uploads/ folder.

model.py picks up the image, runs inference using Roboflow, and sends push notifications for low-stock items.

## Example Result

[
  {"class": "m7"},
  {"class": "s3"}
]

m-matchbox
s-soap
the number represents the count.







