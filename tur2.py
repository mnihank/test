import turtle                   # 匯入小烏龜模組

from turtle import TurtleScreen, goto
from pyasn1.type import namedtype 
#######################
import pygsheets
gc = pygsheets.authorize(service_file='turtle-30925104-5c223ec58120.json')
sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1-CIRwxIeSR2EidHgs6lhB8iqgx0dM_Icfl7V7g4vtMI/edit#gid=0'
)
#選擇哪一個工作表
wks1 = sht.worksheet_by_title("Turtle")
wks2 = sht.worksheet_by_title("Turtle2")

#######################
import serial
import os
if os.path.exists('/dev/ttyACM0') == True:
    s=serial.Serial("/dev/ttyACM0",115200)   #連結arduino序列埠 
if os.path.exists('/dev/ttyACM1') == True:
    s=serial.Serial("/dev/ttyACM1",115200)   #連結arduino序列埠 

screen = turtle.Screen()        # 產生一個螢幕
turtle.Pen().screen.setworldcoordinates(0,0,900,900)
screen.bgcolor('lightgreen')    # 設定螢幕背景

#從1開始，0為最上方名稱
u=1
A = wks1.get_values(start = 'A1',end = 'C1000',include_tailing_empty = False)
#引入function
import numpy
#q為幾列,w為幾行
q,w=numpy.shape(A)
#隱藏畫筆
turtle.hideturtle()
#設定起點
#A[0]為最上方名稱
n,x,y=A[1]
turtle.penup()
x=int(x)
y=int(y)
turtle.setx(x)
turtle.sety(y)
#起點顏色更改
turtle.color('blue')
turtle.dot()
turtle.color('black')
turtle.pendown()
#小烏龜設定
myTurtle = turtle.Turtle()  # 產生一個小烏龜物件
myTurtle2 = turtle.Turtle()  # 產生一個小烏龜物件
myTurtle.color('blue')  # 設定藍色
myTurtle.shape('turtle')
myTurtle.hideturtle()   # 隱藏烏龜
myTurtle.left(90) #初始設定為朝上

myTurtle2.color('blue')  # 設定藍色
myTurtle2.shape('turtle')
myTurtle2.hideturtle()   # 隱藏烏龜
myTurtle2.left(90) #初始設定為朝上

a,b=myTurtle.position()

#存取x,y值
X=[]
X1=[]
X2=[]
Y=[]
Y1=[]
Y2=[]
Ygap1=[]
Ygap2=[]
###################
while 1:
    if(u<q):   #u是從0開始算，q從1開始，如果此陣列僅有5列，那u會執行0,1,2,3,4，若沒有這行會出問題
        n,x,y=A[u]
        #轉成數值
        x=int(x)
        y=int(y)
        X.append(x)
        X1.append(x)
        X2.append(x)
        Y.append(y)
        Y1.append(y)
        Y2.append(y)
        #繪圖
        turtle.goto(x,y)
        u=u+1
        print(x,y)
    #全部外框畫完後跳出
    elif(u>=q-1):
        break
    
def sss(s0,ss):#s0決定上下 0:上 1:下  #ss決定左右 0:左 1:右
    if(ss==0):#左側
        x_index=X1.index(min(X1))
    elif(ss==1):#右側
        x_index=X1.index(max(X1))
    s=X1[x_index]
    while s in X1:
        Ygap1.append(Y1[x_index])
        X1.remove(X1[x_index])
        Y1.remove(Y1[x_index])
    if(s0==0): #上方
        s1=max(Ygap1)
        if(ss==0):
            myTurtle.left(180) #方向設定朝下
            s2=min(X)
        elif(ss==1):
            myTurtle.left(180) #方向設定朝下
            s2=max(X)
    elif(s0==1):#下方
        s1=min(Ygap1)
        if(ss==0):
            s2=min(X)
        elif(ss==1):
            s2=max(X)
    return s1,s2
def sss2(s0,ss):#s0決定上下 0:上 1:下  #ss決定左右 0:左 1:右
    if(ss==0):#左側
        x_index=X2.index(min(X2))
    elif(ss==1):#右側
        x_index=X2.index(max(X2))
    s=X2[x_index]
    while s in X2:
        Ygap2.append(Y2[x_index])
        X2.remove(X2[x_index])
        Y2.remove(Y2[x_index])
    if(s0==0): #上方
        s1=max(Ygap2)
        if(ss==0):
            myTurtle2.left(180) #方向設定朝下
            s2=min(X)
        elif(ss==1):
            myTurtle2.left(180) #方向設定朝下
            s2=max(X)
    elif(s0==1):#下方
        s1=min(Ygap2)
        if(ss==0):
            s2=min(X)
        elif(ss==1):
            s2=max(X)
    return s1,s2
#兩隻烏龜的方向性
s1,s2=sss(1,0)
#烏龜內縮(牆壁內)
s1=s1+20
s2=s2+20
myTurtle.penup()
myTurtle.setx(s2)
myTurtle.sety(s1)
myTurtle.pendown()
myTurtle.showturtle()
s3,s4=sss2(0,1)
#烏龜內縮(牆壁內)
s3=s3-20
s4=s4-20
myTurtle2.penup()
myTurtle2.setx(s4)
myTurtle2.sety(s3)
myTurtle2.pendown()
myTurtle2.showturtle()
#畫中心線
xmax=max(X)
xmin=min(X)
ymax=max(Y)
ymin=min(Y)
xmid=(xmax+xmin)/2
ymid=(ymax+ymin)/2
turtle.penup()
turtle.setpos(xmid,ymax)
turtle.color('red')
turtle.pendown()
turtle.setpos(xmid,ymin)
#
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from PIL import Image
Json = 'turtle-30925104-5c223ec58120.json'
Url = ['https://spreadsheets.google.com/feeds']
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key('1-CIRwxIeSR2EidHgs6lhB8iqgx0dM_Icfl7V7g4vtMI') # 這裡請輸入妳自己的試算表代號
Sheets = Sheet.sheet1

######################
import pyimgur
CLIENT_ID = "a2ec194e41e248c"
PATH = "work.jpg" #A Filepath to an image on your computer"
# PATH = "test.jpg" #A Filepath to an image on your computer"
title = "Uploaded with PyImgur"
def m():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="work.eps")
    im = Image.open("work.eps")
    im.save("work.jpg", "JPEG")
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=title)
    v="%s"%uploaded_image.link
    print(v)
    Sheets.update_acell('D1',v)
#
b=0
c=0
#預設第一隻烏龜起始位置
tur1x=s2
tur1y=s1
Sheets.update_acell('E1',"%d"%s2)
Sheets.update_acell('E2',"%d"%s1)
#時間
import time
t=time.time()
#set

def web():
    Turtle2_action = wks2.get_values(start = 'D1',end = 'E3000')
    q,w=numpy.shape(Turtle2_action)
    return Turtle2_action[q-1][1]
def blue():
    import bluetooth as bt
    server_socket=bt.BluetoothSocket(bt.RFCOMM)
    server_socket.bind(("", bt.PORT_ANY))
    server_socket.listen(1)
    print('等待行動中...')
    client_sock, address = server_socket.accept()
    print(f'前端連接藍芽位址：{address}')
    return client_sock
#車子開始動

while 1:
    Turtle2_mode = wks2.get_values(start = 'C1',end = 'D3000')
    Q,W=numpy.shape(Turtle2_mode)
    if(Q>=3):
        wks2.delete_rows(3, number=3000)
    EEE=['EEE','EEE','EEE','EEE','EEE']
    wks2.update_row(2,EEE)
    
    z=0
    select_value=None
    tt=time.time()
    try:
        while 1 : 
            while 1:
                while time.time()-tt>3:  
                    print("!!!!!!!!!!!!!!!!!!!")
                    
                    tt=time.time()
                Turtle2_mode = wks2.get_values(start = 'C1',end = 'D3000')
                Q,W=numpy.shape(Turtle2_mode)
                if  Turtle2_mode[Q-1][1]=='EEE':
                    z=0
                    print("未連線")
                if  Turtle2_mode[Q-1][1]=='EE':
                    select_value=web()
                    z=0
                    break
                if(z==0 and Turtle2_mode[Q-1][1]=='E'):
                    z1=blue()
                    read_data = z1.recv(1024).decode('utf-8')
                    select_value = read_data
                    z=1
                    break
                elif(z==1 and Turtle2_mode[Q-1][1]=='E'):
                    read_data = z1.recv(1024).decode('utf-8')
                    select_value = read_data
                    break
                print("最新一筆 = ",select_value)
            while 1:
                print("select_value = ",select_value)
                if select_value=='M':
                    s.write(b'M\n')
                    while select_value != 'A':
                        if  Turtle2_mode[Q-1][1]=='EE':
                            select_value=web()
                        elif(z==1 and Turtle2_mode[Q-1][1]=='E'):
                            read_data = z1.recv(1024).decode('utf-8')
                            select_value = read_data
                        print("最新一筆 = ",select_value)
                        if(select_value=='EEE'):
                            break 
                        if(select_value=='S'):
                            s.write(b'STOP\n')
                        elif(select_value=='F'):
                            s.write(b'FORWARD\n')
                        elif(select_value=='L'):  
                            s.write(b'LEFT\n')
                        elif(select_value=='R'):
                            s.write(b'RIGHT\n')
                        elif(select_value=='B'):
                            s.write(b'BACKWARD\n')
                                        
                if select_value=='A1': 
                    while 1 :
                        s.write(b'start\n')     
                        ##################
                        # if  Turtle2_mode[Q-1][1]=='EE':
                        #     select_value=web()
                        # elif(Turtle2_mode[Q-1][1]=='E'):
                        #     read_data = z1.recv(1024).decode('utf-8')
                        #     select_value = read_data
                        # print("最新一筆 = ",select_value)
                        # if select_value=='M' or select_value=='EEE':
                        #     s.write(b'M\n') #在arduino那邊設定停止(無限迴圈內)
                        #     break
                        #上傳&下載區
                        #m()
                        #抓取turtle1位置 
                        if(int(time.time()-t)%3==0):
                            B = wks1.get_values(start = 'E1',end = 'F2')
                            tur1x=int(B[0][0])
                            tur1y=int(B[1][0])
                        myTurtle.setpos(tur1x,tur1y)
                        x,y=myTurtle2.position()
                        #上傳試算表turtle2位置
                        if(int(time.time()-t)%3==0):
                            Sheets.update_acell('F1',"%d"%x)
                            Sheets.update_acell('F2',"%d"%y)
                        ##################
                        data=s.readline().decode()   #讀arduino匯出值(一行)
                        print(data)
                        n3=[]
                        n4=[]
                        #烏龜轉
                        if(data[0]=='G'):#前進
                            G1=int(data[1:])
                            G=G1/10.5
                            myTurtle2.forward(G) 
                        elif(data[0]=='H'):#左轉
                            H1=int(data[1:])               
                            H=H1/8.88888888888888 #建立在arduino轉90度需要800
                            myTurtle2.left(H)
                        elif(data[0]=='J'):#右轉
                            J1=int(data[1:])
                            J=J1/8.88888888888888
                            myTurtle2.right(J)
                        x1=[]
                        y1=[]
                        if(tur1x>=xmid):
                            if(b==0):
                                g=0
                                print("A區已掃完")
                                for i in range(1,q):
                                    if(int(A[i][1])-xmid<0):
                                        print("i = ",i)            
                                    else:
                                        x1.append(A[i][1])
                                        y1.append(A[i][2])      
                                b=1
                            x1.insert(0,'%s'%int(xmid))
                            y1.insert(0,'%s'%ymax)
                            x1.insert(0,'%s'%int(xmid))
                            y1.insert(0,'%s'%ymin)
                            print(x1)
                            print(y1)
                            turtle.penup()
                            xi=int(x1[0])
                            yi=int(y1[0])
                            s.write(b'stopcar\n')
                            if(c==0):
                                #再次畫中心線
                                xmin=tur1x
                                xmax=x
                                ymax=int(max(y1))
                                ymin=int(min(y1))
                                xmid=int((xmax+xmin)/2)
                                ymid=int((ymax+ymin)/2)
                                turtle.setpos(xmid,ymax)
                                turtle.pendown()
                                turtle.setpos(xmid,ymin)
                                c=1
                            s.write(b'cancelstopcar\n')
                            if(tur1x>=xmid):
                                s.write(b'stop\n') 
                                break
                        elif(x<=xmid):
                            if(b==0):
                                g=0
                                print("B區已掃完")
                                for i in range(1,q):
                                    if(int(A[i][1])-xmid>0):
                                        print("i = ",i)            
                                    else:
                                        x1.append(A[i][1])
                                        y1.append(A[i][2])      
                                b=1
                            x1.insert(0,'%s'%int(xmid))
                            y1.insert(0,'%s'%ymax)
                            x1.insert(0,'%s'%int(xmid))
                            y1.insert(0,'%s'%ymin)
                            print(x1)
                            print(y1)
                            turtle.penup()
                            xi=int(x1[0])
                            yi=int(y1[0])
                            s.write(b'stopcar\n')
                            if(c==0):
                                #再次畫中心線
                                xmin=tur1x
                                xmax=x
                                ymax=int(max(y1))
                                ymin=int(min(y1))
                                xmid=int((xmax+xmin)/2)
                                ymid=int((ymax+ymin)/2)
                                turtle.setpos(xmid,ymax)
                                turtle.pendown()
                                turtle.setpos(xmid,ymin)
                                c=1
                            s.write(b'cancelstopcar\n')
                            if(x<=xmid):
                                s.write(b'stop\n') 
                                break
                        if(abs(tur1x-x)<10):
                            s.write(b'stop\n') 
                            break
    except :
        z1.close()

