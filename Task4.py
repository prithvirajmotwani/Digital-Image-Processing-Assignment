import cv2
import numpy as np

# Load and resize the image
image = cv2.imread("8coins.jpg")
image = cv2.resize(image, (256, 256))
image_copy = image.copy()

# Preprocess the image to reduce noise
image_blurred = cv2.GaussianBlur(image_copy, (7, 7), 3)
gray_image = cv2.cvtColor(image_blurred, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary image
thresh, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Segmented Coins", binary_image)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Create a dictionary to store contour areas
area = {i: cv2.contourArea(contours[i]) for i in range(len(contours))}

# Sort contours by area in descending order
sorted_contours = sorted(area.items(), key=lambda x: x[1], reverse=True)

# Count the number of coins based on a minimum area threshold
min_coin_area = 500
num_coins = 0

# Draw contours of coins on the original image
for i in range(1, len(sorted_contours)):
    if sorted_contours[i][1] > min_coin_area:
        num_coins += 1
        cv2.drawContours(image_copy, contours, sorted_contours[i][0], (0, 255, 0), 3)

print("Number of coins:", num_coins)

# Display the image with drawn contours
cv2.imshow("Coins", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
