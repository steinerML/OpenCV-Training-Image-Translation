import cv2
import numpy as np #We are going to need this as we'll work with matrices/arrays.

#We read the image
image = cv2.imread('image-15.png')

#We get the width and height from image.shape()
height, width = image.shape[:2]
print("Width:",width, "Height:",height)

#Now we can create the Translation Matrix by getting tx and ty values
# get tx and ty values for translation
# we can play with the translation values a bit, here we chose 4
#tx > 0 shifts image to the right. tx < 0 will shift the image to the left.
tx, ty = width / 4, height / -4
 
# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

#Apply warpAffine()
translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))

# display the original and the Translated images
cv2.imshow('Translated image', translated_image)
cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
# save the translated image to disk
cv2.imwrite('translated_image.jpg', translated_image)