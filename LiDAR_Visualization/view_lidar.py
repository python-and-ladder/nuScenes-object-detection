import numpy as np
import open3d as o3d
import os
import time

# LIDAR folder path
folder_path = r"C:\Users\v.priyadharshini\OneDrive\Desktop\Internship\v1.0-mini\v1.0-mini\samples\LIDAR_TOP"

# Get all bin files
files = os.listdir(folder_path)

print("Total LiDAR files:", len(files))

# Sort files
files.sort()

# Show each LiDAR file
for file in files:

    if file.endswith(".bin"):

        file_path = os.path.join(folder_path, file)

        print("Showing:", file)

        # Load bin file
        points = np.fromfile(file_path, dtype=np.float32)
        points = points.reshape(-1,5)

        xyz = points[:, :3]

        # Convert to Open3D
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)

        # Show visualization
        o3d.visualization.draw_geometries([pcd])

print("All dataset visualized!")