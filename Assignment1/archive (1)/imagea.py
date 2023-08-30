#part question 1 part a
# ⟨ 2 Marks ⟩ Find out whether the given dataset is imbalanced, if found plot a bar plot for the number of images per class vs classes and mention the imbalanced class, and suggest methods to balance the dataset.
import os
import matplotlib.pyplot as plt
from statistics import mode
# part a done

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

# Identifying the mode (most common no of images in each class)
modeofnumberofimageineachclass = mode(class_counts.values())

# classes which dont have most occuring amount of images as in other classes
imbalanced_classes = [cls for cls, count in class_counts.items() if count != modeofnumberofimageineachclass ]
print("Imbalanced classes:", imbalanced_classes)

# Plotting the bar plot
plt.figure(figsize=(10,6))
plt.bar(class_counts.keys(), class_counts.values())
plt.xlabel('Classes')
plt.ylabel('Number of Images')
plt.title('Number of Images per Class')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# this comes as the output
# Folder: AIRPLANE - Number of files: 20
# Folder: CARS - Number of files: 20
# Folder: ELEPHANTS - Number of files: 39
# Folder: RANDOM - Number of files: 20
# Folder: ROBOTS - Number of files: 21
# Imbalanced classes: ['ELEPHANTS', 'ROBOTS']