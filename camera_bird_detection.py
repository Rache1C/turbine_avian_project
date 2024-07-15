import yolov5
import cv2 
import torch
import numpy as np

# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or 'yolov5m', 'yolov5l', 'yolov5x'

# Simulated function to get the GPS coordinates of the camera
def get_camera_coordinates():
    # Example coordinates (latitude, longitude)
    return 34.0522, -118.2437

# Define a function to detect birds in an image
def detect_birds(image):
    results = model(image)
    return results

# Function to check if detected object is a bird
def is_bird(label):
    return label == 14  # Assuming 14 is the class index for birds in COCO dataset

# Function to process detections and output coordinates
def process_detections(image, results):
    labels, cords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    birds_detected = []
    for i in range(len(labels)):
        if is_bird(labels[i]):
            # Get camera coordinates
            latitude, longitude = get_camera_coordinates()
            birds_detected.append((latitude, longitude))
    return {"latitude":latitude, "longitude":longitude}

# Load an example image
image_path = 'Untitled.jpg'
image = cv2.imread(image_path)

# Detect birds in the image
results = detect_birds(image)

# Process detections and get coordinates
bird_coordinates = process_detections(image, results)

# Output the coordinates of detected birds
# def lat_long_output(lat,lon):
#     for idx, (lat, lon) in enumerate(bird_coordinates):
#     bird_location = {"latitude": {lat}, "longitude": {lon}}
#     return(bird_location)

def lat_long_output():
    return bird_coordinates
