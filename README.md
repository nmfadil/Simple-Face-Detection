# Simple Face Detection

A beginner-friendly Computer Vision project that detects faces in real-time using OpenCV and a Haar Cascade classifier.

## Overview
This was my first project in a Data Science and AI course, introducing me to Computer Vision. It captures webcam video, detects faces using a pretrained Haar Cascade model, and draws green rectangles around them.

## Features
- Real-time face detection with a webcam.
- Green bounding boxes around detected faces.

## Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/nmfadil/Simple-Face-Detection.git
   cd Simple-Face-Detection
   ```

2. Install dependencies:
    ```bash
    pip install opencv-python numpy
    ```
3. Run the script:
    ```bash
    python face_detection.py
    ```
4. Press `q` to exit.

## Requirements

- Python 3.13
- `opencv-python` (install via pip install `opencv-python`)

## How It Works

- Uses OpenCV’s `cv2.CascadeClassifier` with `haarcascade_frontalface_default.xml` to detect faces.
- Converts frames to grayscale and applies `detectMultiScale` for face detection.
- Draws rectangles with `cv2.rectangle` on the mirrored video feed.

## Troubleshooting

- No Webcam Detected: Ensure your webcam is connected and not in use by another app.
- Window Not Opening: Check that `opencv-python` is installed correctly.

## Acknowledgments

- Built as part of a Data Science and AI internship course.
- Thanks to the OpenCV community for the Haar Cascade model.
