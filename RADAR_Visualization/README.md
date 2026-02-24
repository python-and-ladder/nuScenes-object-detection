# NuScenes Radar Data Extraction and Analysis

This project explores and analyzes **RADAR point cloud data (.pcd files)** from the **NuScenes dataset**. The goal is to extract radar data, understand the data structure, and visualize radar detections using Python tools.

This work is part of an **Object Detection and Sensor Data Exploration Task**.

---

## Project Objective

The objective of this project is to:

- Extract RADAR `.pcd` files
- Understand radar data structure
- Analyze radar features
- Visualize radar detections
- Prepare data for object detection tasks

---

## Radar Sensors Used

The following radar sensors are included:

- RADAR_BACK_LEFT
- RADAR_BACK_RIGHT
- RADAR_FRONT
- RADAR_FRONT_LEFT
- RADAR_FRONT_RIGHT

Example file: RADAR_BACK_LEFT.pcd

---

## Tools and Libraries

The following tools were used:

- Python 3.10
- NumPy
- Pandas
- Open3D
- Matplotlib
- NuScenes DevKit
- UV 

Install dependencies:

```bash
UV pip install numpy pandas open3d matplotlib nuscenes-devkit 

project/
│
├── radar_analysis.py
└── dataset/
├── RADAR_BACK_LEFT.pcd
├── RADAR_FRONT.pcd
├── RADAR_FRONT_LEFT.pcd
├── RADAR_FRONT_RIGHT.pcd
├── RADAR_BACK_RIGHT.pcd
│
└── README.md