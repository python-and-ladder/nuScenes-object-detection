import numpy as np
import matplotlib.pyplot as plt
import os

# LIDAR folder
lidar_folder = r"C:\Users\v.priyadharshini\OneDrive\Desktop\Internship\v1.0-mini\v1.0-mini\samples\LIDAR_TOP"

# Output folder
output_folder = "lidar_images"
os.makedirs(output_folder, exist_ok=True)

files = os.listdir(lidar_folder)
files.sort()

print("Converting LiDAR files to images...")

count = 0

for file in files:

    if file.endswith(".bin"):

        file_path = os.path.join(lidar_folder,file)

        points = np.fromfile(file_path, dtype=np.float32)
        points = points.reshape(-1,5)

        x = points[:,0]
        y = points[:,1]

        plt.figure(figsize=(5,5))
        plt.scatter(x,y,s=1)
        plt.axis('off')

        save_path = os.path.join(output_folder,file.replace(".bin",".png"))

        plt.savefig(save_path,bbox_inches='tight',pad_inches=0)
        plt.close()

        print("Saved:",file)

        count +=1

print("Total Images:",count)