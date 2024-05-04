import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/ADITYA/Desktop/photo.jpg")
width, height = img.size

print(width, "x", height)
