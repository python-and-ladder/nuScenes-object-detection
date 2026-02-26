from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

folder = "lidar_images"

files = os.listdir(folder)

os.makedirs("results",exist_ok=True)

for file in files:

    if file.endswith(".png"):

        path = os.path.join(folder,file)

        print("Processing:",file)

        results = model(path)

        save_path = os.path.join("results",file)

        results[0].save(save_path)

print("All Results Saved!")