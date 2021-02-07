import cv2
 
cap = cv2.VideoCapture(0); 
 
## 본인이 사용한 카메라의 해상도를 높이와 너비로 지정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size: {0} x {1}".format(width, height))
 
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 지정

# 저장할 이름, 코덱, 프레임, (너비, 높이)
writer = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))

 
while cap.isOpened():
    success, frame = cap.read()
    if success:
        writer.write(frame)  # 프레임 저장
        cv2.imshow('Video Window', frame)
 
        # q 를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break
 
cap.release()
writer.release()  # 저장 종료
cv2.destroyAllWindows()