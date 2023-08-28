
import os
import matplotlib.pyplot as plt
from PIL import Image
import random
import numpy as np
base_dir = 'IMAGE_DATA/IMAGE_DATA'
entries = os.listdir(base_dir)
class_counts = {}

for entry in entries:
  # value of entries  
  # this prints 
  # AIRPLANE
  # CARS
  # ELEPHANTS
  # RANDOM
  # ROBOTS
    folder_path = os.path.join(base_dir, entry)
    if os.path.isdir(folder_path):
        num_files = len(os.listdir(folder_path))
        class_counts[entry] = num_files
        print(f"Folder: {entry} - Number of files: {num_files}")
        # correct gives no of files in each  entry (class) 
        # find no of images in each entry using len function

        # Folder: AIRPLANE - Number of files: 20
        # Folder: CARS - Number of files: 20
        # Folder: ELEPHANTS - Number of files: 39
        # Folder: RANDOM - Number of files: 20
        # Folder: ROBOTS - Number of files: 21
selected_images = []

# Choose random folders and images
# given chose 4 images from any folder , 
# idea - choose any random folder then choose any random photo
# probability of any photo is same and is an iid event of prob in this case as
# 1/5 * (1/ number of pictures in that class)
# hence it's randomised
for _ in range(4):
    random_folder = random.choice(list(class_counts.keys()))
    num_files = class_counts[random_folder]
    
    if num_files > 0:
        random_image = random.randint(0, num_files - 1) #now it's in range in both extremes
        selected_images.append((random_folder, random_image)) 

# Create a list to store the paths of selected images
selected_image_paths = []

# Generate and store the image paths
for folder, image_idx in selected_images:
    folder_path = os.path.join(base_dir, folder)
    image_filename = os.listdir(folder_path)[image_idx]
    image_path = os.path.join(folder_path, image_filename)
    selected_image_paths.append((image_path, folder))  # Store both image path and folder name
# Standardize images and plot before and after
for image_path, folder in selected_image_paths:
  image = Image.open(image_path)
  image = image.convert('RGB')
  image = np.array(image)
    
    # Display before standardization
  plt.figure(figsize=(10, 4))
  plt.subplot(1, 2, 1)
  plt.imshow(image)
  plt.title('Before Standardization')
    
  # Standardize the image (subtract mean and divide by standard deviation)
  standardized_image = (image - np.mean(image)) / np.std(image)
    
    # Display after standardization
  plt.subplot(1, 2, 2)
  plt.imshow(standardized_image)
  plt.title('After Standardization')
  plt.tight_layout()
  plt.show()
  print(f"Class: {folder}")
  print("Before Standardization:")
  print("Mean:", np.mean(image))
  print("Standard Deviation:", np.std(image))
  print("\nAfter Standardization:")
  print("Mean:", np.mean(standardized_image))
  print("Standard Deviation:", np.std(standardized_image))
  print("="*40)
