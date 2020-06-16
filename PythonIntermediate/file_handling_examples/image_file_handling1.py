#Reading images in Python
#process the images using different libraries like OpenCV, Matplotlib, PIL etc.

#Example1: Python program to read image using OpenCV

# importing OpenCV(cv2) module
#pip install opencv-python
import cv2

# Save image in set directory
# Read RGB image
img = cv2.imread('resources/corona.png')

# Output img with window name as 'image'
cv2.imshow('image', img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()