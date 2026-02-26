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
```

## ⚙️ How to Run
1. Clone the repository
    ```
    git clone https://github.com/lorranybarross/object_tracking.git
    cd object_tracking
2. Install dependencies

    It is highly recommended to use a virtual environment (venv). Install the required libraries using pip:
    ```bash
    pip install ultralytics opencv-python
3. Run the script
   ```
   python main.py
   ```
   Controls during execution:

   Press the `ESC` key to stop the video playback and exit the program.

## 🧠 How It Works
1. Model Loading: The script initializes the YOLO model using the specified weights (`yolo26n.pt`).
2. Video Capture: OpenCV loads the video from the local directory.
3. Processing Loop: The code reads the video frame by frame. For each frame, the `model.track()` function detects objects and assigns unique IDs to them to maintain continuous tracking over time.
4. Visualization: The `plot()` method draws bounding boxes around the detected objects and displays them in an interactive window using OpenCV.
