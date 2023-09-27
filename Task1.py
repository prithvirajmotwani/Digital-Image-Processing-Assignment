import cv2

image = cv2.imread('image2.png')
cv2.imshow("Original Image", image)

resized_image = cv2.resize(image, (256, 256), interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

