import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("Mouse moved at (x={}, y={})".format(x, y))

image = cv2.imread("2.jpg")
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press Esc to exit
        break

cv2.destroyAllWindows()
