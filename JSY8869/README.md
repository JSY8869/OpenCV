# OpenCV
## OpenCV 소개

- OpenCV (Open source Computer Vision)는 실시간 컴퓨터 비젼을 처리하는 목적으로 만들어진 라이브러리이다. 

- OpenCV는 기본적으로 C++로 쓰여져 있는데, 이 라이브러리는 C/C++, Python, Java, C#, Ruby 등 여러 언어에서 사용할 수 있다. 

- OpenCV는 이미지, 영상처리, Object Detection, Motion Detecton 등 매우 다양한 기능들을 제공한다.

- 파이썬에서 OpenCV는 pip을 통해 아래와 같이 설치할 수 있다.
    
`pip install opencv-python`

## [이미지 파일 읽고 쓰기](EXAMPLE/EX1.py)
### 이미지 읽기
`변수 = cv2.imread(이름, 몇 장)`
### 이미지 저장
`cv2.imwrite(저장할 이름, 변수명)`
### 이미지 보여주기
`cv2.imshow(이미지 이름, 변수명)`

## [카메라 영상 처리](EXAMPLE/EX2.py)
- OpenCV에서 카메라(웹캠)로부터 영상을 전달받아 처리하기 위해서는 VideoCapture 클래스를 사용한다. 

- VideoCapture 클래스의 인스턴스를 생성할 때, 컴퓨터에 카메라가 여러 개 있을 수 있으므로, 어떤 카메라를 사용할 지를 카메라 아이디로 전달하는데, 일반적으로 0 을 쓰면 첫번째 카메라(디폴트 카메라)를 사용하게 된다. 

- 만약 두번째 카메라를 사용하려면 1을, 세번째 카메라를 사용하려면 2를 사용한다.

- VideoCapture 클래스 인스턴스를 생성한 후, VideoCapture 클래스의 read() 메서드를 호출하여 카메라 이미지(프레임)을 가져올 수 있다. 

- **read() 메서드는 2개의 값을 리턴하는데, 첫번째는 프레임을 성공적으로 읽었는지를 표시하고, 두번째는 프레임 자체를 리턴한다.** 

- **프레임을 화면에 출력하기 위해서는 cv2.imshow() 함수를 사용하면 되는데, 이 함수의 첫번째 파라미터로 윈도우 창제목을 적고, 두번째 파라미터에 카메라에서 전달받을 프레임을 넣으면 된다.**

- **VideoCapture 클래스의 isOpened() 메서드는 카메라 영상 캡쳐가 초기화되었는지 여부를 리턴하며, 카메라 사용을 종료하기 위해서는 release() 메서드를 사용하면 된다.**

- 만약 카메라가 아니라 동영상 파일에서 영상 데이타를 가져오기 위해서는 VideoCapture 인스턴스를 생성할 때 카메라 Device Id 대신 동영상 파일명을 지정하면 된다. 
예를 들어, `cap = cv2.VideoCapture("test.mp4")` 와 같이 사용한다.

## [카메라 영상 저장하기](EXAMPLE/EX3.py)
- OpenCV에서 카메라(웹캠)로부터 전달받은 영상을 저장하기 위해서는 VideoWriter 클래스를 사용한다. 
- VideoWriter 클래스의 인스턴스를 생성할 때, 영상 저장과 관련된 몇 개의 파라미터를 전달해야 하는데, **첫번째로 영상을 저장할 파일명을 지정하고, 두번째로 영상을 어떤 포맷으로 저장할 지를 표시하는 fourcc ID를 지정한다.** 
- fourcc는 four character code의 약자로서, 비디오 코덱(Codec)을 지정하는 4 바이트 코드이다. 
- VideoWriter() 의 **세번째 파라미터로 프레임수를 지정한다.**
- **네번째 파라미터로 영상 크기 즉 프레임의 너비와 높이를 튜플로 지정한다.**
- 영상 크기는 VideoCapture 클래스의 get() 메서드를 사용하여 프레임 너비와 높이를 가져올 수 있다. EX) `cap.get(cv2.CAP_PROP_FRAME_WIDTH)`

- 실제 프레임 저장은 VideoWriter 클래스의 write() 메서드를 사용하며, 저장이 모두 끝나면 release() 메서드를 호출하여 파일을 닫아 준다.

## [OpenCV와 Matplotlib 활용](EXAMPLE/EX4.py)
- Matplotlib는 파이썬에서 데이터를 차트나 플롯(Plot)으로 그려주는 2D 라이브러리 패키지이다.
- OpenCV에서 img = cv2.imread()를 통해 이미지를 읽어 들인 후, 이어 Matplotlib의 pyplot.imshow(img)로 호출하면 이미지를 pyplot으로 그릴 준비를 하게 된다.
- pyplot.show() 를 호출하면 이미지를 화면에 출력하게 된다. 
- **OpenCV 의 imread()는 `BGR` 포맷으로 이미지를 읽어들이고, pyplot은 `RGB` 포맷을 사용하므로 원래의 이미지 색을 표현하기 위해서는 cv2.cvtColor() 를 사용하여 `BGR` 포맷을 `RGB` 포맷으로 변환해 주는 작업이 필요하다.**
EX) `img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`
- matplotlib에서 생성한 윈도우에서는 이미지를 파일로 저장하거나 이미지 좌표를 체크할 수도 있으며, 이미지를 확대 축소하는 등의 기능들을 사용할 수도 있다.

## [대칭](EXAMPLE/EX5.py)
- 영상이나 이미지를 대칭시켜 띄울 수 있다. 상하 또는 좌우방향으로 대칭할 수 있다.
- `cv2.flip(원본 이미지, 대칭 방법)`
- 0일 경우, 상하방향으로 대칭
- 1일 경우, 좌우방향으로 대칭

## [회전](EXAMPLE/EX6.py)
- 영상이나 이미지를 회전시켜 띄울 수 있다. 90°, 45°, -45° 등 다양한 각도로 회전이 가능하다.
### `height, width, channel = src.shape`
- 높이, 너비, 채널 값 저장
- **높이**와 **너비**를 회전 중심점으로 설정함
### `matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)`
- cv2.getRotationMatrix2D((중심점 X좌표, 중심점 Y좌표), 각도, 스케일)을 설정합니다.
- 중심점은 Tuple형태로 사용하며 회전할 기준점을 설정
- 각도는 회전할 각도를 설정
- 스케일은 이미지의 확대 비율을 설정
### `dst = cv2.warpAffine(src, matrix, (width, height))`
- cv2.warpAffine(원본 이미지, 배열, (결과 이미지 너비, 결과 이미지 높이))
- 결과 이미지의 너비와 높이로 크기가 선언되며 배열에 따라 이미지가 회전
- **matrix를 numpy형식으로 선언하여 warpAffine을 적용하여 변환가능**

## [확대](EXAMPLE/EX7.py)
### 이미지 피라미드
- 이미지 피라미드란 이미지의 크기를 변화시켜 원하는 단계까지 샘플링하는 작업
### `dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT);`
- cv2.pyrUp(원본이미지) -> 이미지 2배 확대
- cv2.pyrUp(원본 이미지, 결과 이미지 크기, 픽셀 외삽법)
- 결과 이미지 크기, 픽셀 외삽법은 고정이므로 생략 가능
- pyrDown() 함수는 2배 축소, 인자는 같음
## [크기 조절](EXAMPLE/EX8.py)
- 영상이나 이미지의 크기를 원하는 크기로 조절할 수 있다.
### `dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)`
- cv2.resize(원본 이미지, 결과 이미지 크기, 보간법)
- 결과 이미지 크기는 (너비, 높이)를 의미
- 보간법은 이미지의 크기를 변경하는 경우, 변형된 이미지의 픽셀은 추정해서 값을 할당해야 함
- 보간법을 이용하여 픽셀들의 값을 할당합니다.
### `1dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7,interpolation=cv2.INTER_LINEAR)`
- cv2.resize(원본 이미지, dsize=(0, 0), 가로비, 세로비, 보간법)
- 결과 이미지 크기가 (0, 0)으로 크기를 설정하지 않은 경우, fx와 fy를 이용하여 이미지의 비율을 조절
- fx가 0.3인 경우, 원본 이미지 너비의 0.3배
- fy가 0.7인 경우, 원본 이미지 높이의 0.7배
- Tip : 결과 이미지 크기와 가로비, 세로비가 모두 설정된 경우, 결과 이미지 크기의 값으로 이미지의 크기가 조절됨
### 보간법이란?
주어진 데이터점을 모두 지나는 유일한 다항식을 구하고, 이 다항식을 이용하여 주변 미지점을 찾아가는(추정하는) 기법
### interpolation 속성
|속성|의미|
|-----------------|-----------|
|cv2.INTER_NEAREST|이웃 보간법|
|cv2.INTER_LINEAR|쌍 선형 보간법|
|cv2.INTER_LINEAR_EXACT|비트 쌍 선형 보간법|
|cv2.INTER_CUBIC|바이큐빅 보간법|
|cv2.INTER_AREA|영역 보간법|
|cv2.INTER_LANCZOS4|Lanczos 보간법|
- 기본적으로 쌍 선형 보간법이 가장 많이 사용됨
- 이미지를 확대하는 경우, 바이큐빅 보간법이나 쌍 선형 보간법을 가장 많이 사용
- 이미지를 축소하는 경우, 영역 보간법을 가장 많이 사용
- 영역 보간법에서 이미지를 확대하는 경우, 이웃 보간법과 비슷한 결과를 반환함
## 자르기
### [EX9-1](EXAMPLE/EX9_1.py)
`dst = src.copy()` 

- 이미지를 복제할 때, dst=src로 사용할 경우, 원본에도 영향을 미치기 때문에 복사해서 사용

`dst = src[100:600, 200:700]`
- dst 이미지에 src[높이, 너비]에서 잘라낼 영역을 설정

### [EX9-2](EXAMPLE/EX9_2.py)
```py
roi = src[100:600, 200:700]
dst[0:380, 0:440] = roi
```
roi를 생성하여 src[높이, 너비]에서 잘라낼 영역을 설정

이후, dst[높이, 너비] = roi를 이용하여 dst 이미지에 해당 영역을 붙여넣음

## [그레이스케일](EXAMPLE/EX10.py)
### `dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)`
- cv2.cvtcolor(원본 이미지, 색상 변환 코드)
- 색상 변환 코드는 원본색상**2**결과색상을 의미함
- 원본 이미지 색상 공간은 원본 이미지와 일치해야 함
### 채널 범위
- CV_8U 이미지 값 범위 : 0 ~ 255
- CV_16U 이미지의 값 범위 : 0 ~ 65535
- CV_32F 이미지의 값 범위 : 0 ~ 1
### 색상 공간 코드
|속성|의미|비고|
|---|---|----|
|BGR|Blue, Green, Red 채널|-|
|BGRA|Blue, Green, Red, Alpha 채널|-|
|RGB|Red, Green, Blue 채널|-|
|RGBA|Red, Green, Blue, Alpha 채널|-|
|GRAY|단일 채널|그레이스케일|
|BGR565|Blue, Green, Red 채널|16 비트 이미지|
|XYZ|X, Y, Z 채널|CIE 1931 색 공간|
|YCrCb|Y, Cr, Cb 채널|YCC (크로마)|
|HSV|Hue, Saturation, Value 채널|색상, 채도, 명도|
|Lab|L, a, b 채널|반사율, 색도1, 색도2|
|Luv|L, u, v 채널|CIE Luv|
|HLS|Hue, Lightness, Saturation 채널|색상, 밝기, 채도|
|YUV|Y, U, V 채널|밝기, 색상1, 색상2|
|BG, GB, RG|디모자이킹|단일 색상 공간으로 변경|
|_EA|디모자이킹|가장자리 인식|
|_VNG|디모자이킹|그라데이션 사용|
