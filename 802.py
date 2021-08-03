import turtle                   # 匯入小烏龜模組
from turtle import goto
from typing import MutableMapping 
import serial
import time
screen = turtle.Screen()        # 產生一個螢幕
turtle.Pen().screen.setworldcoordinates(0,0,900,700)
screen.bgcolor('lightgreen')    # 設定螢幕背景
myTurtle = turtle.Turtle()      # 產生一個小烏龜物件
myTurtle.color('blue')          # 設定小烏龜顏色
myTurtle.shape('turtle')        # 設定小烏龜形狀
myTurtle.penup()                # 提筆
myTurtle.setx(360) #設置機器人初始位置
myTurtle.sety(360) #設置機器人初始位置
myTurtle.pendown()
myTurtle.left(90)
s=serial.Serial("COM11",115200)   #連結arduino序列埠   


turtle.penup()                # 提筆
turtle.setpos(350,350)
turtle.pendown()                # 落筆
turtle.goto(350,500)
turtle.goto(500,500)
turtle.goto(500,350)
turtle.goto(350,350)

while 1:
    data=s.readline().decode()
    x,y=myTurtle.position()      #現在機器人位置
    if(x<=350 or x>=500 or y<=350 or y>=500):
        s.write(b'y\n')

    if(data[0] == 'L'):
        myTurtle.left(90)
    if(data[0] == 'R'):
        myTurtle.right(90)
    if(data[0]=='F'):
        myTurtle.forward(1)
