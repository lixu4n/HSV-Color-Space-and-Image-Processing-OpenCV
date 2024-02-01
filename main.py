#lab 1!


import cv2

# my image
my_image = 'img2.jpeg'

#BGR Format
#cv2.imread(imgpath) is how you read images with opencv
image_bgr = cv2.imread(my_image)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

#Display original version
cv2.imshow('This my original imgage', image_bgr)
print("Press any key to see next image...")
cv2.waitKey(0)
#will show next image

# Display RBG version
cv2.imshow('This is my rbg image', image_rgb)
print("Press any key to see final result...")
cv2.waitKey(0)


# Conversion from RBG to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# V channel to 255 for all pixels
image_hsv[:,:,2] = 255

# All pixels will have the brightness set to the maximum!

# We need to show the converted HSV result into an RBG
image_result_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

#Display result of RBG
cv2.imshow('My final result of RGB image', image_result_rgb)
cv2.waitKey(0)

cv2.destroyAllWindows()
