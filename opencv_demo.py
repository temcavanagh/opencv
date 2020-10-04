import cv2

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("mountain.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Mountain", img)
cv2.imshow("Mountain - gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


# $ python -m venv work
# $ source work/bin/activate
# $ cd desktop
# $ python opencv_demo.py