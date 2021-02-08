import cv2

src = cv2.imread("JSY8869/EXAMPLE/test.png", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)

cv2.imshow("src", src) # 원본 이미지로 사용할 src를 선언, 이미지를 불러옴
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
