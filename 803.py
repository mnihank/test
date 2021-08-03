import turtle                   # 匯入小烏龜模組
######################
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
Json = 'turtle-321809-f6204b09cdfb.json'
Url = ['https://spreadsheets.google.com/feeds']
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key('1VzZ1TEGRZROAowt8t2-w2dV7iSAOAz_vYGfGT7Y_KRc') # 這裡請輸入妳自己的試算表代號
Sheets = Sheet.sheet1
######################
from turtle import clear, goto, write 
import serial
import time
screen = turtle.Screen()        # 產生一個螢幕
screen.bgcolor('lightgreen')    # 設定螢幕背景
myTurtle = turtle.Turtle()      # 產生一個小烏龜物件

turtle.Pen().screen.setworldcoordinates(0,0,900,900)  #設定螢幕寬高
myTurtle.color('blue')          # 設定小烏龜顏色
myTurtle.shape('classic')        # 設定小烏龜形狀
myTurtle.left(90)               # 先將小烏龜方向調整向上

myTurtle.penup()                # 提筆
turtle.penup()                  # 畫筆提筆
turtle.ht()                     #隱藏畫筆
        
myTurtle.setx(450) #設置機器人初始位置
myTurtle.sety(250) #設置機器人初始位置
myTurtle.pendown()                # 落筆
s=serial.Serial("COM11",115200)   #連結arduino序列埠   
########
lst=[]
lst1=[]
lst2=[]
lst3=[]
u=0
u1=1
u2=0
u3=1
a=0
########
j=0  #TF方向  1:左  2:右
p=0  #北東南西
g=0  #傳值給excel
v=[] #傳值給excel
while 1:    #無限迴圈
    data=s.readline().decode()   #讀arduino匯出值(一行)
    if(len(data)<=1):
        data="F200"
    if(int(data[1:])<=70):
        data1=int(data[1:])
    else:
        data1=200
    str(data)                   ##英文+數字
    if(data1>70):
        data1=200
    elif(0<=data1<=10):
        data1=5
    elif(10<data1<=20):
        data1=15
    elif(20<data1<=30):
        data1=25
    elif(30<data1<=40):
        data1=35
    elif(40<data1<=50):
        data1=45
    elif(50<data1<=60):
        data1=55
    elif(60<data1<=70):
        data1=65

    print(data)
    ##################################################掃地機器人位置 
    x,y=myTurtle.position()      #現在機器人位置
    ##################################################第一個方向
    #data 大概是  Fxxx
               #LL   A
             ##方向  1:左方  2:右方
    if(data[0] == 'L'):
        myTurtle.shapesize(0.5, 0.5, 1)
        myTurtle.color('red')          # 設定小烏龜顏色
        myTurtle.shape('square')        # 設定小烏龜形狀
        myTurtle.stamp()
        myTurtle.resizemode("auto")
        myTurtle.color('blue')          # 設定小烏龜顏色
        myTurtle.shape('classic')        # 設定小烏龜形狀
        #####################################################
        excelx,excely=myTurtle.position()
        v.append(g)
        v.append(excelx)
        v.append(excely)
        Sheets.append_row(v)
        print(v)      #這邊放輸入excel的程式
        v=[]
        g=g+1
        #####################################################
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
        myTurtle.shapesize(0.5, 0.5, 1)
        myTurtle.color('red')          # 設定小烏龜顏色
        myTurtle.shape('square')        # 設定小烏龜形狀
        myTurtle.stamp()
        myTurtle.resizemode("auto")
        myTurtle.color('blue')          # 設定小烏龜顏色
        myTurtle.shape('classic')        # 設定小烏龜形狀
        #####################################################
        excelx,excely=myTurtle.position()
        v.append(g)
        v.append(excelx)
        v.append(excely)
        Sheets.append_row(v)
        print(v)      #這邊放輸入excel的程式
        v=[]
        g=g+1
        #####################################################
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
        myTurtle.shapesize(0.5, 0.5, 1)
        myTurtle.color('red')          # 設定小烏龜顏色
        myTurtle.shape('square')        # 設定小烏龜形狀
        myTurtle.stamp()
        myTurtle.resizemode("auto")
        myTurtle.color('blue')          # 設定小烏龜顏色
        myTurtle.shape('classic')        # 設定小烏龜形狀
        #####################################################
        excelx,excely=myTurtle.position()
        v.append(g)
        v.append(excelx)
        v.append(excely)
        Sheets.append_row(v)
        print(v)      #這邊放輸入excel的程式
        v=[]
        g=g+1
        #####################################################
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
        myTurtle.shapesize(0.5, 0.5, 1)
        myTurtle.color('red')          # 設定小烏龜顏色
        myTurtle.shape('square')        # 設定小烏龜形狀
        myTurtle.stamp()
        myTurtle.resizemode("auto")
        myTurtle.color('blue')          # 設定小烏龜顏色
        myTurtle.shape('classic')        # 設定小烏龜形狀
        #####################################################
        excelx,excely=myTurtle.position()
        v.append(g)
        v.append(excelx)
        v.append(excely)
        Sheets.append_row(v)
        print(v)      #這邊放輸入excel的程式
        v=[]
        g=g+1
        #####################################################
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
    elif(data[0]=='F'):            #依照arduino程式比例 f=14F
        myTurtle.forward(3)
        a=0
    elif(data[0]=='f'):
        if(a==0):
            myTurtle.forward(42)
            a=1        
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
                    turtle.setpos(lst[u],lst1[u])
                    turtle.pendown()
                    turtle.goto(lst[u1],lst1[u1])
                    turtle.penup()
                    u=u+1
                    u1=u1+1
            elif(p==1):  #E
                turtle.setpos(x, y+data1)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    turtle.setpos(lst[u],lst1[u])
                    turtle.pendown()
                    turtle.goto(lst[u1],lst1[u1])
                    turtle.penup()
                    u=u+1
                    u1=u1+1
            elif(p==2):  #S
                turtle.setpos(x+data1, y)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    turtle.setpos(lst[u],lst1[u])
                    turtle.pendown()
                    turtle.goto(lst[u1],lst1[u1])
                    turtle.penup()
                    u=u+1
                    u1=u1+1
            elif(p==3):  #W
                turtle.setpos(x, y-data1)
                x1,y1=turtle.position()
                lst.append(x1)
                lst1.append(y1)
                if(len(lst)>1):
                    turtle.setpos(lst[u],lst1[u])
                    turtle.pendown()
                    turtle.goto(lst[u1],lst1[u1])
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
                    turtle.setpos(lst2[u2],lst3[u2])
                    turtle.pendown()
                    turtle.goto(lst2[u3],lst3[u3])
                    turtle.penup()
                    u2=u2+1
                    u3=u3+1
            elif(p==1):  #E
                turtle.setpos(x, y-data1)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    turtle.setpos(lst2[u2],lst3[u2])
                    turtle.pendown()
                    turtle.goto(lst2[u3],lst3[u3])
                    turtle.penup()
                    u2=u2+1
                    u3=u3+1
            elif(p==2):  #S
                turtle.setpos(x-data1, y)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    turtle.setpos(lst2[u2],lst3[u2])
                    turtle.pendown()
                    turtle.goto(lst2[u3],lst3[u3])
                    turtle.penup()
                    u2=u2+1
                    u3=u3+1
            elif(p==3):  #W
                turtle.setpos(x, y+data1)
                x1,y1=turtle.position()
                lst2.append(x1)
                lst3.append(y1)
                if(len(lst2)>1):
                    turtle.setpos(lst2[u2],lst3[u2])
                    turtle.pendown()
                    turtle.goto(lst2[u3],lst3[u3])
                    turtle.penup()
                    u2=u2+1
                    u3=u3+1


        
        

        
