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
        # Folder: AIRPLANE - Number of files: 20
        # Folder: CARS - Number of files: 20
        # Folder: ELEPHANTS - Number of files: 39
        # Folder: RANDOM - Number of files: 20
        # Folder: ROBOTS - Number of files: 21
# Identifying the mode (most common class)
modeofnumberofimageineachclass = mode(class_counts.values())

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
# Folder: AIRPLANE - Number of files: 20
# Folder: CARS - Number of files: 20
# Folder: ELEPHANTS - Number of files: 39
# Folder: RANDOM - Number of files: 20
# Folder: ROBOTS - Number of files: 21
# Imbalanced classes: ['ELEPHANTS', 'ROBOTS']