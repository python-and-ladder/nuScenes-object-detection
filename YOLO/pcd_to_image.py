import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

folder = "D:\\AI Intern Projects\\dataset"
output = "radar_images"

os.makedirs(output, exist_ok=True)

# Create output folder
os.makedirs("sample_output", exist_ok=True)

for file in os.listdir(folder):

    if file.endswith(".pcd"):

        path = os.path.join(folder,file)

        pcd = o3d.io.read_point_cloud(path)

        points = np.asarray(pcd.points)

        x = points[:,0]
        y = points[:,1]

        plt.figure(figsize=(5,5))

        plt.scatter(x,y,s=2)

        plt.axis("off")

        name = file.replace(".pcd",".png")

        plt.savefig(
            os.path.join(output,name),
            dpi=300
        )

        plt.close()

print("Conversion Done")