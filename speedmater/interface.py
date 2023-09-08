from machine import Pin, UART, I2C
import utime, time
from ssd1306 import SSD1306_I2C
import writer
#https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/writer.py

i2c=I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

#######################################################
def interface0():
    #display.text("N",0,0) #방향
    #display.text("gps",0,-2)
    
    #display.fill_rect(117, 2, 2, 2, 1) # 연결완료
    #display.text(")",117,0)
    #display.text(")",121,0)
    #display.text("  x",105,0)


    display.text("O",14,34)
    display.text("25",16,12)
    display.text("50",55,0)
    display.text("100",94,12)
    display.text("150",102,34)

    #display.text("168.1",-1,48,1)
    #display.text("125.3",-1,57,1)
    #display.text("NONE",0,51,1) #위치

    #display.text(" TIME",89,51) #시간

    #font_writer.set_textpos(54, 44)
    #font_writer.printstring("00")
    #font_writer.set_textpos(49, 44)
    #font_writer.printstring("150")

    display.fill_rect(58, 38, 12, 3, 1) #중앙 속도계
    display.fill_rect(61, 35, 6, 3, 1)
    display.line(69, 38, 65, 35, 1)
    display.line(58, 38, 62, 35, 1)
    display.fill_rect(60, 37, 2, 2, 1)
    display.fill_rect(67, 37, 2, 2, 1)

    display.text("km",55,22)

    #display.line(56, 39, 29, 39, 1) #바늘 0

    #display.fill_rect(125, 0, 2, 2, 1) # 2
    #display.fill_rect(0, 60, 2, 2, 1) # 3
    #display.fill_rect(125, 60, 2, 2, 1) # 4
    #display.fill_rect(62, 30, 2, 2, 1) # 중앙

    #display.fill_rect(24, 35, 2, 2, 1)# 왼 시작

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


    #display.fill_rect(100, 43, 2, 2, 1) # 오른시작점
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
    #############################################

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


    #display.fill_rect(100, 43, 2, 2, 1) # 오른시작점2
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
    

###################################################
    
def interface1():
    latitude = convert(my_gps.latitude)
    longitude = convert(my_gps.longitude)
    gpsTime = '{:02d}:{:02d}'.format(t[0], t[1])
    gpsdate = my_gps.date_string('long')
    speed = my_gps.speed_string('kph') #'kph' or 'mph' or 'knot'
    direction = my_gps.compass_direction
    
    
    display.fill(0)

    display.text(direction,0,0) #방향
    #display.text("gps",0,-2)
    
    display.fill_rect(117, 2, 2, 2, 1) # 연결완료
    display.text(")",117,0)
    display.text(")",121,0)
    #display.text("CNT",105,0)
    #display.text(".",91,0)
    #display.text(".",94,0)
    #display.text(".",97,0)
    #display.text(".",100,0) # 연결 중

    display.text("O",14,34)
    display.text("25",16,12)
    display.text("50",55,0)
    display.text("100",94,12)
    display.text("150",102,34)

    display.text(latitude,1,-1,48,1)
    display.text(longitude,1,-1,57,1)
    #display.text("NONE",0,51,1) #위치

    display.text(gpsTime,89,51) #시간

    font_writer.set_textpos(54, 44)
    font_writer.printstring("0"+speed,0)
    #font_writer.set_textpos(49, 44)
    #font_writer.printstring("150")

    display.fill_rect(58, 38, 12, 3, 1) #중앙 속도계
    display.fill_rect(61, 35, 6, 3, 1)
    display.line(69, 38, 65, 35, 1)
    display.line(58, 38, 62, 35, 1)
    display.fill_rect(60, 37, 2, 2, 1)
    display.fill_rect(67, 37, 2, 2, 1)

    display.text("km",55,22)

    display.line(56, 39, 29, 39, 1) #바늘 0

    #display.fill_rect(125, 0, 2, 2, 1) # 2
    #display.fill_rect(0, 60, 2, 2, 1) # 3
    #display.fill_rect(125, 60, 2, 2, 1) # 4
    #display.fill_rect(62, 30, 2, 2, 1) # 중앙

    #display.fill_rect(24, 35, 2, 2, 1)# 왼 시작

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


    #display.fill_rect(100, 43, 2, 2, 1) # 오른시작점
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
    #############################################

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


    #display.fill_rect(100, 43, 2, 2, 1) # 오른시작점2
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


    display.show()
