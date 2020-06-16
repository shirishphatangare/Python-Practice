#Using MatplotLib : Matplotlib is an amazing visualization library in Python for 2D
# plots of arrays. Matplotlib is a multi-platform data visualization
# library built on NumPy arrays and designed to work with the broader SciPy stack.

# Python program to read an image using matplotlib

# importing matplotlib modules
#Install the necessary library : pip install matplotlib

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Read Images
img = mpimg.imread('resources/corona.png')

# Output Images
plt.imshow(img)