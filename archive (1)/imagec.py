import os
from PIL import Image
import numpy as np

base_dir = 'IMAGE_DATA/IMAGE_DATA'
entries = os.listdir(base_dir)
class_stats = {}  # To store mean and variance for each class

image_size = (256, 256)  # Define a common image size [resize all images to same matrix size and 256x256 pxels]

def load_and_preprocess_image(image_path):
    image = Image.open(image_path)  # Load image using PIL
    image = image.convert('RGB')  # Convert to RGB format
    image = image.resize(image_size, Image.ANTIALIAS)  # Resize the image for same matrix
    image = np.array(image)  # Convert to NumPy array # convert image size matrix intensities
    image = image.astype(np.float32) / 255.0  # Normalize pixel values to [0, 1]
    return image

for entry in entries:
    folder_path = os.path.join(base_dir, entry) # specefic class
    if os.path.isdir(folder_path):
        class_images = []
        
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            image = load_and_preprocess_image(image_path) # preprocess all the images of specefic class
            class_images.append(image)
        
        class_images_array = np.array(class_images) # all images of that folder (specefic class)
        class_mean = np.mean(class_images_array) #  mean of all the matrices of that class
        class_variance = np.var(class_images_array) # variance of matrices of that class
        
        class_stats[entry] = {'mean': class_mean, 'variance': class_variance}
        print(f"Class: {entry} - Mean: {class_mean}, Variance: {class_variance}")

# Analyze the results and draw conclusions based on mean and variance values
# For instance, you can compare means and variances between different classes.
#output
# Class: AIRPLANE - Mean: 0.5444138646125793, Variance: 0.08124949038028717
# Class: CARS - Mean: 0.42772167921066284, Variance: 0.10981985181570053
# Class: ELEPHANTS - Mean: 0.4954516291618347, Variance: 0.07608890533447266
# Class: RANDOM - Mean: 0.7076295018196106, Variance: 0.1668040156364441
# Class: ROBOTS - Mean: 0.6151171922683716, Variance: 0.10478784143924713
# Mean Comparison:

# The mean pixel values indicate the average brightness or intensity of the images in each class.
# The "RANDOM" class has the highest mean value (0.7076), suggesting that the images in this class might be generally brighter or more intense compared to other classes.
# The "CARS" class has the lowest mean value (0.4277), indicating that its images might be darker or less intense on average.
# Variance Comparison:

# The variance of pixel values represents the spread or variability of intensities within the images.
# The "RANDOM" class again has the highest variance (0.1668), implying that the pixel intensities vary more widely within this class's images.
# The "ELEPHANTS" class has the lowest variance (0.0761), indicating relatively consistent pixel intensities.

# Overall Assessment:
# Variations in mean and variance between classes might suggest different lighting conditions, image quality, or content characteristics.
# Classes with similar mean and variance values might have similar distributions of pixel intensities.
