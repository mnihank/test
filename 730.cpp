import turtle                   # 匯入小烏龜模組
from turtle import clear, goto 
import serial
import time
screen = turtle.Screen()        # 產生一個螢幕
screen.bgcolor('lightgreen')    # 設定螢幕背景
myTurtle = turtle.Turtle()      # 產生一個小烏龜物件

# turtle.Pen().screen.setworldcoordinates(0,0,500,400)  #設定螢幕寬高
turtle.Pen().screen.setworldcoordinates(0,0,900,700)  #設定螢幕寬高
myTurtle.color('blue')          # 設定小烏龜顏色
myTurtle.shape('turtle')        # 設定小烏龜形狀
myTurtle.left(90)               # 先將小烏龜方向調整向上

myTurtle.penup()                # 提筆
turtle.penup()                  # 畫筆提筆

# myTurtle.setx(250) #設置機器人初始位置
# myTurtle.sety(200) #設置機器人初始位置            
myTurtle.setx(450) #設置機器人初始位置
myTurtle.sety(250) #設置機器人初始位置
s=serial.Serial("COM11",115200)   #連結arduino序列埠   

lst=[]
lst1=[]
lst2=[]
lst3=[]
value_L=0
value_R=0
u=0
u1=1
u2=0
u3=1
j=0
p=0
k=30
while 1:    #無限迴圈
    data=s.readline().decode()   #讀arduino匯出值(一行)
    if(len(data)<=1):
        data="F200"
    data1=int(data[1:])
    str(data)                   ##英文+數字
    if(data1>70):
        data1=200
    print(data)
    ##################################################掃地機器人位置 
    x,y=myTurtle.position()      #現在機器人位置
    ##################################################第一個方向
    #data 大概是  Fxxx
               #LL   A
             ##方向  1:左方  2:右方
    if(data[0] == 'L'):
        myTurtle.stamp()
        myTurtle.left(90)
        p=p-1
        lst=[]
        lst1=[]
        lst2=[]
        lst3=[]
        u=0
        u1=1
        u2=0
        u3=1
        j=2
    elif(data[0] == 'R'):
        myTurtle.stamp()
        myTurtle.right(90)
        p=p+1
        lst=[]
        lst1=[]
        lst2=[]
        lst3=[]
        u=0
        u1=1
        u2=0
        u3=1
        j=1
    elif(data[0] == 'r'):
        myTurtle.stamp()
        myTurtle.right(90)
        p=p+1
        lst=[]
        lst1=[]
        lst2=[]
        lst3=[]
        u=0
        u1=1
        u2=0
        u3=1
        j=2
    elif(data[0] == 'l'):
        myTurtle.stamp()
        myTurtle.left(90)
        p=p-1
        lst=[]
        lst1=[]
        lst2=[]
        lst3=[]
        u=0
        u1=1
        u2=0
        u3=1
        j=1
    elif(data[0]=='F'):
        myTurtle.forward(6)
    if(p==4):
        p=0
    if(p==-1):
        p=3
    turtle.penup() 
    if(j == 1): #TF方向朝左
        if(data1!=200):
            if(p==0):  #N
                turtle.setpos(x-data1,y)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    if(abs(lst[u]-lst[u1])>k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
                    elif(abs(lst[u]-lst[u1])<=k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
            elif(p==1):  #E
                turtle.setpos(x, y+data1)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    if(abs(lst1[u]-lst1[u1])>k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
                    elif(abs(lst1[u]-lst1[u1])<=k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
            elif(p==2):  #S
                turtle.setpos(x+data1, y)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    if(abs(lst[u]-lst[u1])>k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
                    elif(abs(lst[u]-lst[u1])<=k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
            elif(p==3):  #W
                turtle.setpos(x, y-data1)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    if(abs(lst1[u]-lst1[u1])>k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u1])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
                    elif(abs(lst1[u]-lst1[u1])<=k):
                        turtle.setpos(lst[u],lst1[u])
                        turtle.pendown()
                        turtle.goto(lst[u1],lst1[u])
                        turtle.penup()
                        u=u+1
                        u1=u1+1
    turtle.penup()
    if(j==2):    #TF方向朝右
        if(data1!=200):
            if(p==0):  #N
                turtle.setpos(x+data1,y)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    if(abs(lst2[u2]-lst2[u3])>k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u3],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
                    elif(abs(lst2[u2]-lst2[u3])<=k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u2],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
            elif(p==1):  #E
                turtle.setpos(x, y-data1)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    if(abs(lst3[u2]-lst3[u3])>k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u3],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
                    elif(abs(lst3[u2]-lst3[u3])<=k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u3],lst3[u2])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
            elif(p==2):  #S
                turtle.setpos(x-data1, y)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    if(abs(lst2[u2]-lst2[u3])>k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u3],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
                    elif(abs(lst2[u2]-lst2[u3])<=k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u2],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
            elif(p==3):  #W
                turtle.setpos(x, y+data1)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    if(abs(lst3[u2]-lst3[u3])>k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()
                        turtle.goto(lst2[u3],lst3[u3])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1
                    elif(abs(lst3[u2]-lst3[u3])<=k):
                        turtle.setpos(lst2[u2],lst3[u2])
                        turtle.pendown()           
                        turtle.goto(lst2[u3],lst3[u2])
                        turtle.penup()
                        u2=u2+1
                        u3=u3+1


        
        

        
