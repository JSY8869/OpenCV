# EX1 이미지 읽기, 보여주기, 저장하기
import cv2
 
# 이미지 읽기
img = cv2.imread('C:/Users/Jason/Desktop/github/OpenCV/JSY8869/EXAMPLE/test.jpg', 1)
 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)

# 아무 키나 입력시까지 대기
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
cv2.imwrite('test2.png', img)