import os
import random
import matplotlib.pyplot as plt
from PIL import Image

base_dir = 'IMAGE_DATA/IMAGE_DATA'
entries = os.listdir(base_dir)
# Select 8 random images
random_images = random.sample(entries, 8)
plt.figure(figsize=(15, 10))
for idx, image_name in enumerate(random_images, 1):
  image_path = os.path.join(base_dir, image_name, os.listdir(os.path.join(base_dir, image_name))[0])
   # Load and display the image
  img = Image.open(image_path)
  plt.subplot(2, 4, idx)
  plt.imshow(img)
  plt.title(image_name)
  plt.axis('off')

  plt.tight_layout()
  plt.show()
