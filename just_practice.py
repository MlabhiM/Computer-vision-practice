import cv2

# Load the image
image = cv2.imread("2.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the pixel value at a specific coordinate (x, y)
x = 100
y = 50
gray_value = gray_image[y, x]

print("Gray value at coordinates (", x, ",", y, "):", gray_value)
