from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="radar_images",
    save=True
)

print("Prediction Done")