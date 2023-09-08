import machine
import time

# Pico의 내장 LED는 GP25 핀에 연결되어 있습니다.
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)  # LED 켜기
    time.sleep(1) # 1초 대기
    led.value(0)  # LED 끄기
    time.sleep(1) # 1초 대기
## MicroPython 다운받아서 pico 드라이버에 드래그 앤 드롭 하기
    