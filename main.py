from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO('yolo26n.pt')

# Load video
VIDEO_PATH = './data/person_dog.mp4'
cap = cv2.VideoCapture(VIDEO_PATH)

# Read frames
ret = True
while ret:
    ret, frame = cap.read()

    if ret:
        # Detect and track objects
        results = model.track(frame, persist=True)

        # Plot results
        frame_ = results[0].plot()

        # Visualize
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xff == 27:
            break