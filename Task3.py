import cv2

image = cv2.imread('image2.png')
cv2.imshow("Original Image", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)

thresh, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
