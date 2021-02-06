# OpenCV
## OpenCV 소개

- OpenCV (Open source Computer Vision)는 실시간 컴퓨터 비젼을 처리하는 목적으로 만들어진 라이브러리이다. 

- OpenCV는 기본적으로 C++로 쓰여져 있는데, 이 라이브러리는 C/C++, Python, Java, C#, Ruby 등 여러 언어에서 사용할 수 있다. 

- OpenCV는 이미지, 영상처리, Object Detection, Motion Detecton 등 매우 다양한 기능들을 제공한다.

- 파이썬에서 OpenCV는 pip을 통해 아래와 같이 설치할 수 있다.
    
`pip install opencv-python`

## [이미지 파일 읽고 쓰기](EX1.py)
### 이미지 읽기
`변수 = cv2.imread(이름, 몇 장)`
### 이미지 저장
`cv2.imwrite(저장할 이름, 변수명)`
### 이미지 보여주기
`cv2.imshow(이미지 이름, 변수명)`

## [카메라 영상 처리](EX2.py)
- OpenCV에서 카메라(웹캠)로부터 영상을 전달받아 처리하기 위해서는 VideoCapture 클래스를 사용한다. 

- VideoCapture 클래스의 인스턴스를 생성할 때, 컴퓨터에 카메라가 여러 개 있을 수 있으므로, 어떤 카메라를 사용할 지를 카메라 아이디로 전달하는데, 일반적으로 0 을 쓰면 첫번째 카메라(디폴트 카메라)를 사용하게 된다. 

- 만약 두번째 카메라를 사용하려면 1을, 세번째 카메라를 사용하려면 2를 사용한다.

- VideoCapture 클래스 인스턴스를 생성한 후, VideoCapture 클래스의 read() 메서드를 호출하여 카메라 이미지(프레임)을 가져올 수 있다. 

- **read() 메서드는 2개의 값을 리턴하는데, 첫번째는 프레임을 성공적으로 읽었는지를 표시하고, 두번째는 프레임 자체를 리턴한다.** 

- **프레임을 화면에 출력하기 위해서는 cv2.imshow() 함수를 사용하면 되는데, 이 함수의 첫번째 파라미터로 윈도우 창제목을 적고, 두번째 파라미터에 카메라에서 전달받을 프레임을 넣으면 된다.**

- **VideoCapture 클래스의 isOpened() 메서드는 카메라 영상 캡쳐가 초기화되었는지 여부를 리턴하며, 카메라 사용을 종료하기 위해서는 release() 메서드를 사용하면 된다.**

- 만약 카메라가 아니라 동영상 파일에서 영상 데이타를 가져오기 위해서는 VideoCapture 인스턴스를 생성할 때 카메라 Device Id 대신 동영상 파일명을 지정하면 된다. 
예를 들어, `cap = cv2.VideoCapture("test.mp4")` 와 같이 사용한다.

## [카메라 영상 저장하기](EX3.py)
- OpenCV에서 카메라(웹캠)로부터 전달받은 영상을 저장하기 위해서는 VideoWriter 클래스를 사용한다. 
- VideoWriter 클래스의 인스턴스를 생성할 때, 영상 저장과 관련된 몇 개의 파라미터를 전달해야 하는데, **첫번째로 영상을 저장할 파일명을 지정하고, 두번째로 영상을 어떤 포맷으로 저장할 지를 표시하는 fourcc ID를 지정한다.** 
- fourcc는 four character code의 약자로서, 비디오 코덱(Codec)을 지정하는 4 바이트 코드이다. 
- VideoWriter() 의 **세번째 파라미터로 프레임수를 지정한다.**
- **네번째 파라미터로 영상 크기 즉 프레임의 너비와 높이를 튜플로 지정한다.**
- 영상 크기는 VideoCapture 클래스의 get() 메서드를 사용하여 프레임 너비와 높이를 가져올 수 있다. EX) `cap.get(cv2.CAP_PROP_FRAME_WIDTH)`

- 실제 프레임 저장은 VideoWriter 클래스의 write() 메서드를 사용하며, 저장이 모두 끝나면 release() 메서드를 호출하여 파일을 닫아 준다.

## [OpenCV와 Matplotlib 활용](EX4.py)
- Matplotlib는 파이썬에서 데이터를 차트나 플롯(Plot)으로 그려주는 2D 라이브러리 패키지이다.
- OpenCV에서 img = cv2.imread()를 통해 이미지를 읽어 들인 후, 이어 Matplotlib의 pyplot.imshow(img)로 호출하면 이미지를 pyplot으로 그릴 준비를 하게 된다.
- pyplot.show() 를 호출하면 이미지를 화면에 출력하게 된다. 
- **OpenCV 의 imread()는 `BGR` 포맷으로 이미지를 읽어들이고, pyplot은 `RGB` 포맷을 사용하므로 원래의 이미지 색을 표현하기 위해서는 cv2.cvtColor() 를 사용하여 `BGR` 포맷을 `RGB` 포맷으로 변환해 주는 작업이 필요하다.**
EX) `img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`
- matplotlib에서 생성한 윈도우에서는 이미지를 파일로 저장하거나 이미지 좌표를 체크할 수도 있으며, 이미지를 확대 축소하는 등의 기능들을 사용할 수도 있다.