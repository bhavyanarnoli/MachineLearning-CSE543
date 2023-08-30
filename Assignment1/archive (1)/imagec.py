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
    image = image.resize(image_size)  # Resize the image for same matrix
    image = np.array(image)  # Convert to NumPy array # convert image size matrix intensities
    image = image.astype(np.float32) / 255.0  # Normalize pixel values to [0, 1]
    return image

for entry in entries:
    folder_path = os.path.join(base_dir, entry) # specific class
    # just check if it's a directory although it;s not necessary
    if os.path.isdir(folder_path):
        classimagematrices = []
        # all the files in that directory which is photos in that class
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            # preprocess that image in folder  make it's matrice
            image = load_and_preprocess_image(image_path)
            # preprocess all the images of specefic class
            classimagematrices.append(image)
            # convert image into a  matrices of dimension 256 x 256
            # append all the matrices(of all the images in that class)
          # 
        classimagematriceslist = np.array(classimagematrices) # all images of that folder (specefic class)
        classimagematricesmean = np.mean(classimagematriceslist) #  mean of all the matrices of that class
        classimagematricevariance = np.var(classimagematriceslist) # variance of matrices of that class
        
        class_stats[entry] = {'mean': classimagematricesmean, 'variance': classimagematricevariance}
        print(f"Class: {entry} - Mean: {classimagematricesmean}, Variance: {classimagematricevariance}")

# Analyze the results and draw conclusions based on mean and variance values
# For instance, you can compare means and variances between different classes.
#output
# Class: AIRPLANE - Mean: 0.5444371700286865, Variance: 0.08080846816301346
# Class: CARS - Mean: 0.4276656210422516, Variance: 0.10919812321662903
# Class: ELEPHANTS - Mean: 0.49545565247535706, Variance: 0.0756186917424202
# Class: RANDOM - Mean: 0.707990288734436, Variance: 0.16660833358764648
# Class: ROBOTS - Mean: 0.6151620745658875, Variance: 0.10408671200275421

# Mean Comparison:

# The mean pixel values indicate the average brightness or intensity of the images in each class.
# The "RANDOM" class has the highest mean value (0.7079), suggesting that the images in this class might be generally brighter or more intense compared to other classes.
# The "CARS" class has the lowest mean value (0.4276), indicating that its images might be darker or less intense on average.
# Variance Comparison:

# The variance of pixel values represents the spread or variability of intensities within the images.
# The "RANDOM" class again has the highest variance (0.1666), implying that the pixel intensities vary more widely within this class's images.
# The "ELEPHANTS" class has the lowest variance (0.0756), indicating relatively consistent pixel intensities.

# Overall Assessment:
# Variations in mean and variance between classes might suggest different lighting conditions, image quality, or content characteristics.
# Classes with similar mean and variance values might have similar distributions of pixel intensities.
