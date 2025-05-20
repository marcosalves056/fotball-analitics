import numpy as np
from ultralytics import YOLO

# Load a base model (YOLOv8 nano - smallest version)
model = YOLO("yolo11n.pt")

# Train on your dataset
model.train(
    task="detect",  # train or train-augmented
    data="datasets/data.yaml",
    epochs=1000,
    imgsz=640,
    batch=16,
    augment=True
)
