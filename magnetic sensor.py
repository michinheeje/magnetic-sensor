import pycurl, json
from StringIO import StringIO
import RPi.GPIO as GPIO

#브로드컴 SOC 채널 번호를 사용하여 GPIO 셋업
GPIO.setmode(GPIO.BCM)

# 풀업으로 설정 (일반적으로 닫힌 상태)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# InstaPush 변수를 셋업

# Instapush에서 응용 프로그램 ID로 설정
appID = "5755540a5659e3be72ffffef"

# Instapush에서 응용 프로그램 비밀로 설정
appSecret = "811cf06c9303ff9a36a968628dd4c54f"

# Instapush에서 pushEvent라는 이름을 DoorAlert로 설정
pushEvent = "DoorAlert"

# pushMessage를 Door Opened! 설정
pushMessage = "Door Opened!"

# StringIO 사용하여 push API호출의 응답을 수집
buffer = StringIO()

# Crul 사용하여 Instapush API에 보냄
c = pycurl.Curl()

# Instapush API URL 설정
c.setopt(c.URL, 'https://api.instapush.im/v1/post')

# 설치 인증 변수와 콘텐츠 형식에 대한 사용자 지정 헤더
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
'x-instapush-appsecret: ' + appSecret,
'Content-Type: application/json'])

# JSON데이터에 대한 사전 구조 Instapush 것을 슬래쉬닷에 만듬
json_fields = {}

# JSON 값 설정
json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage

postfields = json.dumps(json_fields)

# POSTFIELDS을 JSON 보냄
c.setopt(c.POSTFIELDS, postfields)

# 버퍼에 응답을 캡처 할 수 있는 설정
c.setopt(c.WRITEFUNCTION, buffer.write)

# 콘솔창을 이용한 무한 루프로 메시지 응답 opened / closed
while True:

# 문이 열릴 때 검출
GPIO.wait_for_edge(23, GPIO.RISING)
print("Door Opened!\n")

# 상기 도어가 개방 할때 푸시 요청을 보냄
c.perform()

# 서버로부터의 응답을 캡처
body= buffer.getvalue()

# 응답 프린트
print(body)

# 버퍼를 재설정
buffer.truncate(0)
buffer.seek(0)

# 문이 닫을 때 폐쇄
GPIO.wait_for_edge(23, GPIO.FALLING)
print("Door Closed!\n")

# 청소
c.close()
GPIO.cleanup()
