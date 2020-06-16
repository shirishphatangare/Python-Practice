# Using PIL : PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities
# Python program to read image using PIL module
# importing PIL - pip install Pillow

from PIL import Image
# Read image
img = Image.open('resources/corona.png')
# Output Images
img.show()
# prints format of image
print("Image Format: ",img.format)
# prints mode of image
print("Image Mode: ", img.mode)
#Get the size of Image
width, height = img.size
print("Image Size:",width, height)

print("Rotating an Image and storing")
#Rotate the Image and Save Image
img = img.rotate(180)
# Saved in the same relative location
img.save("resources/rotated_corona.png")

#Resizing an Image: Image.resize(size)
#Cropping an Image: Image.crop(box)
#Getting a Histogram of an Image: Image.histogram

print("Transposing an Image and storing")
#Transposing an Image: This feature gives us the mirror image of an image
# transposing image
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# Save transposed image
transposed_img.save("resources/transposed_corona.png")

print("Creating a thumbnail of an Image and storing")
#Creating a thumbnail:  In-place modification
img.thumbnail((200, 200))
img.save("resources/thumb_corona.png")