import os
import matplotlib.pyplot as plt
from PIL import Image
import random
import numpy as np

base_dir = 'IMAGE_DATA/IMAGE_DATA'
entries = os.listdir(base_dir)
class_counts = {}

for entry in entries:
    folder_path = os.path.join(base_dir, entry)
    if os.path.isdir(folder_path):
        num_files = len(os.listdir(folder_path))
        class_counts[entry] = num_files
        print(f"Folder: {entry} - Number of files: {num_files}")

selected_images = []

# Choose random folders and images
for _ in range(8):
    random_folder = random.choice(list(class_counts.keys()))
    num_files = class_counts[random_folder]
    
    if num_files > 0:
        random_image = random.randint(0, num_files - 1)  # Corrected this line
        selected_images.append((random_folder, random_image))

# Create a list to store the paths of selected images
selected_image_paths = []

# Generate and store the image paths
for folder, image_idx in selected_images:
    folder_path = os.path.join(base_dir, folder)
    image_filename = os.listdir(folder_path)[image_idx]
    image_path = os.path.join(folder_path, image_filename)
    selected_image_paths.append((image_path, folder))  # Store both image path and folder name

# Initialize array to store grayscale values
grayscale_values = []

# Loop through selected images and convert to grayscale
for image_path, folder_name in selected_image_paths:
    print(image_path)
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    grayscale_values.extend(image_array.ravel())

# Plot grayscale histogram with class labels
plt.figure(figsize=(8, 6))

# Create a dictionary to store class-wise grayscale values
class_grayscale = {}
for image_path, folder_name in selected_image_paths:
    if folder_name not in class_grayscale:
        class_grayscale[folder_name] = []
    
    class_grayscale[folder_name].extend(np.array(Image.open(image_path).convert('L')).ravel())
  
# print(class_grayscale)
for folder_name, values in class_grayscale.items():
    plt.hist(values, bins=50, alpha=0.7, label=folder_name)

plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.ylim(0, 9000)

plt.tight_layout()
plt.show()
