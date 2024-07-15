# turbine_avian_project

## Bird Detection and Alert System for Wind Turbines
## Project Overview

This project aims to detect the presence of birds around wind turbines and send an alert to the turbine system to minimize the risk of bird collisions. Additionally, the system classifies the birds to better understand bird movements and patterns, which can be used for ecological studies and improving turbine operation strategies.

### Features:

- Bird Detection: Uses a pre-trained YOLOv5 model to detect birds in real-time from video feeds or images.
- Geolocation Mapping: Integrates with a GPS system to provide the latitude and longitude of detected birds.
- Bird Classification: Classifies birds using a fine-tuned ResNet model to identify different species.
- Alert System: Sends an alert to the wind turbine control system when a bird is detected within a 1-mile radius.
