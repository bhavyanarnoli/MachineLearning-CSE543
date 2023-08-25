# 2. ⟨ 2 Marks ⟩ Randomly take 8 images from entire dataset and plot there respective histograms and label the class.
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
# Folder: AIRPLANE - Number of files: 20
# Folder: CARS - Number of files: 20
# Folder: ELEPHANTS - Number of files: 39
# Folder: RANDOM - Number of files: 20
# Folder: ROBOTS - Number of files: 21
selected_images = []

# Choose random folders and images
# given chose 8 images from any folder , 
# idea - choose any random folder then choose any random photo
# probability of any photo is same and is an iid event of prob in this case as
# 1/5 * (1/ number of pictures in that class)
# hence it's randomised
for _ in range(8):
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

# Initialize array to store grayscale values
grayscale_values = []
# printing  Loop through selected images and convert to grayscale
for image_path, folder_name in selected_image_paths:
    print(image_path)
    # gives intensity of that image 
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
    # creating a folder of grey scale of that class if doesn't exist and then add value of pixel grayscale of each image of given grayscale bin at each of it 
    class_grayscale[folder_name].extend(np.array(Image.open(image_path).convert('L')).ravel())
  
# print(class_grayscale)
for folder_name, values in class_grayscale.items():
    # x axis has bins of grayscale , and y axis has frequency of it
    plt.hist(values, bins=256, alpha=0.7, label=folder_name)

plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
#  for clearer frequencies at lower 
plt.ylim(0, 2000) # can change to see outliers at top has what values

plt.tight_layout()
plt.show()
