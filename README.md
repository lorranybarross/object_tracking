# Object Tracking with YOLO and OpenCV

## 📖 About the Project
This is a practical, introductory Computer Vision project developed to learn and apply object detection and tracking concepts. 

The script uses the YOLO model (via the `ultralytics` library) alongside `OpenCV` to process video footage. The current use case analyzes a video of a girl skateboarding while walking her dog, successfully identifying and tracking both subjects frame by frame.

## 🚀 Technologies Used
* **Python 3.x**
* **Ultralytics (YOLO):** For object detection and tracking.
* **OpenCV (`cv2`):** For reading, manipulating, and displaying video frames.

## 📁 Folder Structure
To ensure the code runs correctly, make sure your directory is organized as follows:

```text
├── main.py               # Main script
└── data/
    └── person_dog.mp4    # Sample video used for testing