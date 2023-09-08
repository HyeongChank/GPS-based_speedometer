from machine import Pin, UART, I2C
import utime, time

from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS
import freesans20
import writer

i2c=I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

TIMEZONE = 9
my_gps = MicropyGPS(TIMEZONE)
speed1 = 0

def convert(parts):
    if (parts[0] == 0):
        return None
        
    data = parts[0]+(parts[1]/60.0)
    if (parts[2] == 'S'):
        data = -data
    if (parts[2] == 'W'):
        data = -data

    data = '{0:.1f}'.format(data) # to 6 decimal places
    return str(data)

def interface():
    display.text("O",14,34)
    display.text("25",16,12)
    display.text("50",55,0)
    display.text("100",94,12)
    display.text("150",102,34)

    display.fill_rect(112, 1, 5, 5, 1) # 커넥팅 
    display.line(117, 1, 119, 3, 1)
    display.line(117, 5, 119, 3, 1)
    
    display.fill_rect(58, 38, 12, 3, 1) #중앙 속도계
    display.fill_rect(61, 35, 6, 3, 1)
    display.line(69, 38, 65, 35, 1)
    display.line(58, 38, 62, 35, 1)
    display.fill_rect(60, 37, 2, 2, 1)
    display.fill_rect(67, 37, 2, 2, 1)

    display.text("km",55,22)

    display.line(24, 39, 24, 36, 1) # 여기부터 왼 반원
    display.line(25, 35, 25, 33, 1)
    display.line(26, 32, 26, 30, 1)
    display.line(27, 29, 27, 28, 1)
    display.line(28, 27, 28, 26, 1)
    display.line(29, 25, 29, 25, 1)

    display.line(30, 24, 36, 18, 1)

    display.line(37, 17, 38, 17, 1)
    display.line(39, 16, 40, 16, 1)
    display.line(41, 15, 42, 15, 1)
    display.line(43, 14, 44, 14, 1)
    display.line(45, 13, 46, 13, 1)

    display.line(47, 12, 48, 12, 1)
    display.line(49, 11, 50, 11, 1)
    display.line(51, 10, 53, 10, 1)

    display.line(54, 9, 70, 9, 1)

    display.line(100, 39, 100, 36, 1) # 여기부터 오른 반원
    display.line(99, 35, 99, 33, 1)
    display.line(98, 32, 98, 30, 1)
    display.line(97, 29, 97, 28, 1)
    display.line(96, 27, 96, 26, 1)
    display.line(95, 25, 95, 25, 1)

    display.line(94, 24, 88, 18, 1)

    display.line(87, 17, 86, 17, 1)
    display.line(85, 16, 84, 16, 1)
    display.line(83, 15, 82, 15, 1)
    display.line(81, 14, 80, 14, 1)
    display.line(79, 13, 78, 13, 1)

    display.line(77, 12, 76, 12, 1)
    display.line(75, 11, 74, 11, 1)
    display.line(73, 10, 71, 10, 1)
    #########################################################

    display.line(26, 39, 26, 36, 1) # 여기부터 왼 반원2
    display.line(27, 35, 27, 33, 1)
    display.line(28, 32, 28, 30, 1)
    display.line(29, 29, 29, 28, 1)
    display.line(30, 27, 30, 26, 1)
    display.line(31, 25, 31, 25, 1)

    display.line(32, 24, 38, 18, 1)

    display.line(39, 18, 40, 18, 1)
    display.line(41, 17, 42, 17, 1)
    display.line(43, 16, 44, 16, 1)
    display.line(45, 15, 46, 15, 1)
    display.line(47, 14, 48, 14, 1)

    display.line(49, 13, 50, 13, 1)
    display.line(51, 12, 52, 12, 1)
    display.line(53, 11, 54, 11, 1)

    display.line(54, 11, 70, 11, 1)

    display.line(98, 39, 98, 36, 1) # 여기부터 오른 반원2
    display.line(97, 35, 97, 33, 1)
    display.line(96, 32, 96, 30, 1)
    display.line(95, 29, 95, 28, 1)
    display.line(94, 27, 94, 26, 1)
    display.line(93, 25, 93, 25, 1)

    display.line(92, 24, 86, 18, 1)

    display.line(85, 18, 84, 18, 1)
    display.line(83, 17, 82, 17, 1)
    display.line(81, 16, 80, 16, 1)
    display.line(79, 15, 78, 15, 1)
    display.line(77, 14, 76, 14, 1)

    display.line(75, 13, 74, 13, 1)
    display.line(73, 12, 72, 12, 1)
    display.line(71, 11, 70, 11, 1)
    
font_writer = writer.Writer(display, freesans20)
speed1 = 0
zeroo = 1
font_writer.set_textpos(54, 44)
font_writer.printstring('00')
display.line(56, 39, 29, 39, 1)
display.text('LON',-1,48,1) #위도
display.text('LAT',-1,57,1) # 경도
display.text("TIME",95,57) #시간
display.text("CP",0,0)

while True:
    interface()
    length = gps_module.any()
    if length>0:
        b = gps_module.read(length)
        for x in b:
            msg = my_gps.update(chr(x))
    #_________________________________________________   
    latitude = convert(my_gps.latitude)
    longitude = convert(my_gps.longitude)
    #_________________________________________________
    
    if (latitude == None and latitude == None):
        #display.text('LON',-1,48,1) #위도
        #display.text('LAT',-1,57,1) # 경도
        #display.text("TIME",95,57) #시간
        #display.line(56, 39, 29, 39, 1)
        display.text("x",100,-1)
        display.line(108, 3, 130, 3, 1)
        display.text(")",118,0)
        display.text(")",122,0)
        #display.text("gps",0,-2)
        display.show()
        continue
    
    t = my_gps.timestamp
    gpsTime = '{:02d}:{:02d}'.format(t[0], t[1])
    gpsbh = my_gps.compass_direction()
    gpsdate = my_gps.date_string('long')
    speed = my_gps.speed_string('kph') #'kph' or 'mph' or 'knot'
    speed1 = "%0.0f" % float(speed)
    speed2 = int(speed1) 
    #_________________________________________________
    display.fill(0)
    interface()
    display.fill_rect(117, 2, 2, 2, 1) # 연결완료
    display.text(")",118,0)
    display.text(")",122,0)
    display.text(longitude,-1,48,1) #위도
    display.text(latitude,-1,57,1) # 경도
    display.text(gpsTime,87,57) #시간
    display.text(gpsbh,0,0) # 방향
    
    if speed2 <= 9:
        font_writer.set_textpos(54, 44)
        font_writer.printstring('0'+speed1)
    elif speed2 <= 99:
        font_writer.set_textpos(54, 44)
        font_writer.printstring(speed1)
    else:
        font_writer.set_textpos(49, 44)
        font_writer.printstring(speed1)
        
    if speed2 == 0:
        display.line(56, 39, 29, 39, 1)
    elif speed2 == 1 or speed2 == 2 :
        display.line(56, 39, 29, 38, 1)     
    elif speed2 == 3 or speed2 == 4 :
        display.line(56, 39, 29, 37, 1)    
    elif speed2 == 5 or speed2 == 6 :
        display.line(56, 39, 29, 36, 1)  
    elif speed2 == 7 or speed2 == 8 :
        display.line(56, 39, 29, 35, 1)
    elif speed2 == 9 or speed2 == 10 :
        display.line(56, 39, 29, 34, 1)
    elif speed2 == 11 or speed2 == 12 :
        display.line(56, 38, 30, 33, 1)
    elif speed2 == 13 or speed2 == 14 :
        display.line(56, 37, 31, 32, 1)
    elif speed2 == 15 or speed2 == 16 :
        display.line(56, 37, 32, 31, 1)
    elif speed2 == 17 or speed2 == 18 :
        display.line(56, 36, 32, 30, 1)
    elif speed2 == 19 or speed2 == 20 :
        display.line(56, 36, 33, 29, 1)
    elif speed2 == 21 or speed2 == 22 :
        display.line(56, 36, 33, 28, 1)
    elif speed2 == 23 or speed2 == 24 :
        display.line(57, 35, 34, 27, 1)
    elif speed2 == 25 :
        display.line(58, 35, 37, 23, 1)    
    elif speed2 == 26 or speed2 == 27 :
        display.line(58, 35, 38, 21, 1)
    elif speed2 == 28 or speed2 == 29 :
        display.line(58, 35, 40, 20, 1)
    elif speed2 == 30 or speed2 == 31 :
        display.line(58, 35, 42, 19, 1)
    elif speed2 == 32 or speed2 == 33 :
        display.line(59, 34, 44, 18, 1)
    elif speed2 == 34 or speed2 == 35 :
        display.line(60, 33, 46, 17, 1)
    elif speed2 == 36 or speed2 == 37 :
        display.line(60, 32, 48, 16, 1)
    elif speed2 == 38 or speed2 == 39 :
        display.line(60, 32, 50, 15, 1)
    elif speed2 == 40 or speed2 == 41 :
        display.line(60, 32, 52, 14, 1)
    elif speed2 == 42 or speed2 == 43 :
        display.line(60, 32, 54, 13, 1)
    elif speed2 == 44 or speed2 == 45 :
        display.line(61, 32, 56, 12, 1)
    elif speed2 == 46 or speed2 == 47 :
        display.line(62, 32, 57, 11, 1)
    elif speed2 == 48 or speed2 == 49 :
        display.line(62, 32, 59, 11, 1)
    elif speed2 == 50 :
        display.line(63, 32, 63, 13, 1)
    elif 51 <= speed2 or speed2 >= 54  :
        display.line(63, 32, 66, 13, 1)
    elif 55 <= speed2 or speed2 >= 58  :
        display.line(63, 32, 68, 13, 1)
    elif 59 <= speed2 or speed2 >= 62  :
        display.line(64, 32, 70, 13, 1)
    elif 63 <= speed2 or speed2 >= 66  :
        display.line(64, 32, 72, 14, 1)
    elif 67 <= speed2 or speed2 >= 70  :
        display.line(64, 32, 74, 14, 1)
    elif 71 <= speed2 or speed2 >= 74  :
        display.line(64, 32, 76, 15, 1)
    elif 75 <= speed2 or speed2 >= 78  :
        display.line(66, 32, 78, 15, 1)
    elif 79 <= speed2 or speed2 >= 82  :
        display.line(66, 32, 80, 16, 1)
    elif 83 <= speed2 or speed2 >= 86  :
        display.line(68, 32, 82, 18, 1)
    elif 87 <= speed2 or speed2 >= 90  :
        display.line(68, 32, 86, 20, 1)
    elif 91 <= speed2 or speed2 >= 95  :
        display.line(68, 32, 86, 21, 1)
    elif 96 <= speed2 or speed2 >= 99  :
        display.line(69, 35, 86, 22, 1)
    elif speed2 == 100 :
        display.line(69, 35, 88, 23, 1)
    elif 101 <= speed2 or speed2 >= 104  :
        display.line(69, 35, 89, 24, 1)
    elif 105 <= speed2 or speed2 >= 108  :
        display.line(69, 35, 90, 25, 1)
    elif 109 <= speed2 or speed2 >= 112  :
        display.line(69, 35, 91, 26, 1)
    elif 113 <= speed2 or speed2 >= 116  :
        display.line(69, 35, 92, 27, 1)
    elif 117 <= speed2 or speed2 >= 120  :
        display.line(70, 36, 93, 28, 1)
    elif 121 <= speed2 or speed2 >= 124  :
        display.line(70, 36, 93, 29, 1)
    elif 125 <= speed2 or speed2 >= 128  :
        display.line(70, 36, 93, 30, 1)
    elif 129 <= speed2 or speed2 >= 132  :
        display.line(70, 36, 94, 31, 1)
    elif 133 <= speed2 or speed2 >= 137  :
        display.line(70, 36, 94, 32, 1)
    elif 138 <= speed2 or speed2 >= 141  :
        display.line(70, 36, 94, 33, 1)
    elif 142 <= speed2 or speed2 >= 145  :
        display.line(71, 37, 95, 34, 1)
    elif 146 <= speed2 or speed2 >= 149  :
        display.line(71, 38, 95, 35, 1)
    elif speed2 >= 150 :
        display.line(71, 39, 95, 39, 1)
    display.show()
    
##########################################################
