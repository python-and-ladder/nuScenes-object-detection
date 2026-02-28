from ultralytics import YOLO
import json
import os

# Load YOLO model
model = YOLO("yolov8n.pt")

# Radar image folder
image_folder = "D:\\AI Intern Projects\\YOLO\\radar_images"

# Output folder
os.makedirs("sample_output/json", exist_ok=True)


for file in os.listdir(image_folder):

    if file.endswith(".png"):

        image_path = os.path.join(image_folder, file)

        # Run YOLO
        results = model(image_path)

        detections = []

        boxes = results[0].boxes

        for box in boxes:

            cls_id = int(box.cls[0])

            confidence = float(box.conf[0])

            bbox = box.xyxy[0].tolist()

            detections.append({

                "class_id": cls_id,

                "confidence": confidence,

                "bbox": bbox

            })


        data = {

            "image": file,

            "detections": detections

        }


        save_path = os.path.join(
            "sample_output/json",
            file.replace(".png",".json")
        )


        with open(save_path,"w") as f:

            json.dump(data,f,indent=4)


print("JSON Output Saved")