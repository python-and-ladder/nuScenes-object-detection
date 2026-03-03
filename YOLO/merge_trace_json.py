import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os
import json
from ultralytics import YOLO

# -----------------------
# CONFIG
# -----------------------
dataset_root = "D:/AI Intern Projects/YOLO/dataset"
output_folder = "json_output"
os.makedirs(output_folder, exist_ok=True)

model = YOLO("yolov8n.pt")

sensor_map = {
    "RADAR_BACK_LEFT": "back-left",
    "RADAR_BACK_RIGHT": "back-right",
    "RADAR_FRONT": "front",
    "RADAR_FRONT_LEFT": "front-left",
    "RADAR_FRONT_RIGHT": "front-right"
}

all_traces = set()

# Collect trace names from all 5 folders
for sensor_folder in sensor_map.keys():

    folder_path = os.path.join(dataset_root, sensor_folder)

    if os.path.exists(folder_path):

        for file in os.listdir(folder_path):

            if file.endswith(".pcd"):
                all_traces.add(file)

# Convert to list
trace_files = list(all_traces)

print("Total traces found:", len(trace_files))

for trace_file in all_traces:

    if not trace_file.endswith(".pcd"):
        continue

    print("Processing trace:", trace_file)

    merged_data = {
        "back-left": [],
        "back-right": [],
        "front": [],
        "front-left": [],
        "front-right": []
    }

    # Loop through 5 radar sensors
    for folder_name, json_key in sensor_map.items():

        pcd_path = os.path.join(
            dataset_root,
            folder_name,
            trace_file
        )

        if not os.path.exists(pcd_path):
            continue

        # Load PCD
        pcd = o3d.io.read_point_cloud(pcd_path)
        points = np.asarray(pcd.points)

        if len(points) == 0:
            continue

        # Convert to temporary image
        x = points[:,0]
        y = points[:,1]

        temp_img = "temp.png"

        plt.figure(figsize=(5,5))
        plt.scatter(x, y, s=2)
        plt.axis("off")
        plt.savefig(temp_img)
        plt.close()

        # Run YOLO
        results = model(temp_img)

        detections = []

        for box in results[0].boxes:

            detections.append({
                "class_id": int(box.cls[0]),
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist()
            })

        merged_data[json_key] = detections

    # Save JSON with trace name
    json_name = trace_file.replace(".pcd", ".json")
    json_path = os.path.join(output_folder, json_name)

    with open(json_path, "w") as f:
        json.dump(merged_data, f, indent=4)

    print("Saved:", json_name)

print("All traces processed successfully.")