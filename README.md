# magnetic-sensor
## 준비물
Raspberry Pi, SD Card, Magnetic sensor, Smartphone, Instapush 계정,

## 사용법
1. Raspberry Pi OS 설치</br>
<https://www.raspberrypi.org/downloads/raspbian/></br>
SD Card로 iso 이미지 파일을 구워야 됩니다.

2. instapush 접속하여 가입하기</br>
<https://instapush.im/>
해당 URL 들어가서 가입하세요.

3. Add Application 버튼을 클릭합니다.</br>

4. Application Title에 Door Push라고 작성합니다.

5. Add event 버튼을 클릭합니다.

6. Event Title, Trackers, Push Message 정보를 입력합니다.</br>
Event Title: `DoorAlert`</br>
Trackers: `message`</br>
Push Message: `{message}`

7. Add Event를 클릭합니다.

8. Basic Info tab를 클릭하여 Application ID와 Application Secret 자동적으로 생성하여 Python 코드에 필요합니다.

9. Raspberry Pi와 Magnetic sensor 하드웨어를 설계합니다.
빨간줄: 23 Pin
검정줄: GPN Pin

10. python와 pycurl 설치</br>
`sudo apt-get install python-pycurl`

11. git clone 하기</br>
`git clone https://github.com/michinheeje/magnetic-sensor.git`

## 결과
Magnetic sensor가 서로 떨어져 있으면 Smartphone에 경고 창이 뜨면서 'Dooropen' 이라고 경고창이 뜸

## Copyright
<https://videos.cctvcamerapros.com/digital-io-alarm-in-out/send-push-notifications-from-raspberry-pi.html>
