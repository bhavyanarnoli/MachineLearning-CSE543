# 2. ⟨ 2 Marks ⟩ Randomly take 8 images from entire dataset and plot there respective histograms and label the class.
import os
import matplotlib.pyplot as plt
from PIL import Image
import random
import numpy as np
import time
base_dir = 'IMAGE_DATA/IMAGE_DATA'
entries = os.listdir(base_dir)
class_counts = {}

for entry in entries:
    folder_path = os.path.join(base_dir, entry)
    if os.path.isdir(folder_path):
        num_files = len(os.listdir(folder_path))
        class_counts[entry] = num_files
        print(f"Folder: {entry} - Number of files: {num_files}")
# Folder: AIRPLANE - Number of files: 20
# Folder: CARS - Number of files: 20
# Folder: ELEPHANTS - Number of files: 39
# Folder: RANDOM - Number of files: 20
# Folder: ROBOTS - Number of files: 21
selected_images = []

# Choose random folders and images
# given chose 8 images from any folder , 
# Constraint of below function is that it's deciding on the basis of current time which can be 
# predictive for given time but for different time it's difficult to determine the value

def linearcongruentialgenerator(seed):
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed
current_time = int(time.time())

    # Use the current time as a seed for the random number generator
seed = current_time

for randomchosenimage in range(8):
    
    random_folder = list(class_counts.keys())[linearcongruentialgenerator(seed) % len(class_counts)]
    num_files = class_counts[random_folder]
    
    if num_files > 0:
        random_image = linearcongruentialgenerator(seed) % num_files
        selected_images.append((random_folder, random_image))
        seed = linearcongruentialgenerator(seed)  # Update the seed for the next iteration

print(selected_images)

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

# Create a dictionary to store class-wise grayscale values
class_grayscale = {}

# printing  Loop through selected images and convert to grayscale
for image_path, folder_name in selected_image_paths:
    print(image_path)
    # gives intensity of that image 
    image = Image.open(image_path).convert('L') # convert image to grayscale matrices
    image_array = np.array(image)
    grayscale_values.extend(image_array.ravel())
    if folder_name not in class_grayscale:
        class_grayscale[folder_name] = []
    # creating a folder of grey scale of that class if doesn't exist and then add value of pixel grayscale of each image of given grayscale bin at each of it 
    class_grayscale[folder_name].extend(np.array(Image.open(image_path).convert('L')).ravel())

# Plot grayscale histogram with class labels
plt.figure(figsize=(8, 6))

# print(class_grayscale)
for folder_name, values in class_grayscale.items():
    # x axis has bins of grayscale , and y axis has frequency of it
    plt.hist(values, bins=256, alpha=0.7, label=folder_name)

plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
#  for clearer frequencies at lower 
plt.ylim(0, 1000) # can change to see outliers at top has what values

plt.tight_layout()
plt.show()
