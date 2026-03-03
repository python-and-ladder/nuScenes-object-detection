import numpy as np
import pandas as pd
import open3d as o3d
import matplotlib.pyplot as plt


# Load Radar PCD File

file_path = "D:\\nuScenes-object-detection\\RADAR_Visualization\\dataset\\RADAR_FRONT.pcd"   # change path if needed

pcd = o3d.io.read_point_cloud(file_path)

points = np.asarray(pcd.points)

print("\nRadar Point Cloud Loaded")
print("-------------------------")
print("Total Points:", len(points))
print("Shape:", points.shape)


# 2. Convert to DataFrame

df = pd.DataFrame(points, columns=['x','y','z'])

print("\nSample Data:")
print(df.head())

# Basic Statistics

print("\nStatistics:")
print(df.describe())


# Distance Calculation

df['distance'] = np.sqrt(
    df['x']**2 +
    df['y']**2 +
    df['z']**2
)

print("\nDistance Stats:")
print(df['distance'].describe())


# Plot Radar Points (Top View)

plt.figure(figsize=(6,6))

plt.scatter(df['x'], df['y'], s=1)

plt.title("Radar Top View")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()

# 3D Visualization

print("\nOpening 3D Viewer...")
o3d.visualization.draw_geometries([pcd])

print("\nAnalysis Completed")