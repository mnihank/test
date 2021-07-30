#include <Servo.h>
#include <SoftwareSerial.h>
#include <LiquidCrystal_PCF8574.h>
#include <Wire.h>
#include "LIDARLite.h"
Servo servoRight; //車馬達右
Servo servoLeft;  //車馬達左
Servo myservo; // 建立Servo物件，控制伺服馬達
//TFmini測距宣告
SoftwareSerial mySerial(A2, A1);      // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
LIDARLite myLidarLite;
//TF回傳參數宣告
uint16_t dist;
//TF伺服馬達時間參數
int INTERVAL_MESSAGE1 = 700;
int INTERVAL_MESSAGE2 , INTERVAL_MESSAGE3 = 0;
unsigned long time_1 = 0;
//超音波
const int pingPinL = 7;   //左
const int pingPinR = 10;   //右
const int pingPinLC = 5;   //左
const int pingPinRC = 6;   //右
unsigned int durationL, inchesL;
unsigned int durationR, inchesR;
unsigned int durationLC, inchesLC, oldLC;
unsigned int durationRC, inchesRC, oldRC;
//超音波距離
int k1 = 31;
int k = 15;
//除錯參數
int gap = 5;
int Lneed = 0;
int Rneed = 0;
byte a = 0 , lst[3];//前左超音波,用來判斷距離精準度(在判斷前左超音波底下讓a=0,,可重新執行動作);相互比較參數值
byte a1 = 0 , lst1[3];//前右超音波,用來判斷距離精準度(在判斷前右超音波底下讓a=0,,可重新執行動作);相互比較參數
byte a2 = 0 , lst2[3];//前左中超音波,用來判斷距離精準度(在判斷前左中超音波底下讓a=0,,可重新執行動作);相互比較參數值
byte a3 = 0 , lst3[3];//前右中超音波,用來判斷距離精準度(在判斷前右中超音波底下讓a=0,,可重新執行動作);相互比較參數值
byte a4 = 0 , lst4[3];//TF,用來判斷距離精準度(在判斷TF讓a=0,,可重新執行動作);相互比較參數值
//基本參數
byte b = 0;
byte b1 = 0;
byte c = 0;
byte g = 0;
//LCD
LiquidCrystal_PCF8574 lcd(0x27);  // 設定i2c位址，一般情況就是0x27和0x3F兩種
void setup() {
  servoRight.attach(12);
  servoLeft.attach(13);
  Serial.begin(115200);
  ////////////////////////////////////Tf
  myLidarLite.begin(0, true);
  myLidarLite.configure(0);
  myservo.attach(8); // 連接數位腳位9，伺服馬達的訊號線
  lcd.begin(16, 2); // 初始化LCD
  //lcd.begin(20, 4);
  lcd.setBacklight(255);
  lcd.clear();
}
void loop() {
  lcd.setCursor(0, 0);  //設定游標位置 (字,行)
  TF();
  UI();

  ////////////////////////////////////////////////////////////////////////////////////////////////////
  TF();
  UI();
  if (inchesL <= k1 && inchesR <= k1) {
    myservo.write(135);
    TF();
    if (dist <= k1) { //判斷左右轉
      stopcar(1);
      UI();
      if (inchesRC < inchesLC) {   //左轉
        b = 1;
        b1 = 1;
      }
      else if (inchesLC < inchesRC) {  //右轉
        b = 2;
        b1 = 2;
      }
      else if (inchesR < inchesL) {  //左轉
        b = 1;
        b1 = 1;
      }
      else if (inchesR > inchesL) {  //右轉
        b = 2;
        b1 = 2;
      }
      else {
        b = 0;
        b1 = 0;
      }
      if (b == 1) { //左轉
        myservo.write(55);
        while (inchesR < (k1 + 10)) {
          UI();
          turnLeft(1);
        }
        turnLeft(250);
        stopcar(1);
        UI();
        c = 1;
      }
      else if (b == 2) { //右轉
        myservo.write(180);
        while (inchesL < (k1 + 10)) {
          UI();
          turnRight(1);
        }
        turnRight(250);
        stopcar(1);
        UI();
        c = 2;
      }
      b = 0;
    }
    if (c == 1) {
      lcd.clear();
      lcd.print("L");
      lcd.print("   dist = ");
      lcd.print(dist);
      Serial_port();
    }
    else if (c == 2) {
      lcd.clear();
      lcd.print("R");
      lcd.print("   dist = ");
      lcd.print(dist);
      Serial_port();
    }
  }
  else if (inchesR > k1 && inchesL > k1)  { //前進
    UI();
    TF();
    while (inchesR > k1 && inchesL > k1 && b1 == 1) {
      TF();
      if (inchesRC > (k1 + 10)) {
        lcd.clear();
        lcd.print("r");
        lcd.print("   dist = ");
        lcd.print(dist);
        forward(100);
        turnRight(650);
        myservo.write(55);
        c = 5;
        Serial_port();

        while (inchesRC > k) {
          TF();
          UI();
          forward(1);
          c = 3;
          Serial_port();
          lcd.clear();
          lcd.print("F");
          lcd.print("   dist = ");
          lcd.print(dist);
        }
      }
      oldRC = inchesRC;
      forward(200);
      c = 3;
      Serial_port();
      lcd.clear();
      lcd.print("F");
      lcd.print("   dist = ");
      lcd.print(dist);
      UI();
      if (inchesRC > oldRC) {
        turnRight(10);
      }
      if (inchesRC < oldRC) {
        turnLeft(10);
      }
    }
    while (inchesR > k1 && inchesL > k1 && b1 == 2) {
      TF();
      if (inchesLC > (k1 + 10)) {
        lcd.clear();
        lcd.print("l");
        lcd.print("   dist = ");
        lcd.print(dist);
        forward(100);
        turnLeft(750);
        myservo.write(180);
        c = 4;
        Serial_port();

        while (inchesLC > k) {
          TF();
          UI();
          forward(1);
          c = 3;
          Serial_port();
          lcd.clear();
          lcd.print("F");
          lcd.print("   dist = ");
          lcd.print(dist);
        }
      }
      oldLC = inchesLC;
      forward(200);
      c = 3;
      Serial_port();
      lcd.clear();
      lcd.print("F");
      lcd.print("   dist = ");
      lcd.print(dist);
      UI();
      if (inchesLC > oldLC) {
        turnLeft(10);
      }
      if (inchesLC < oldLC) {
        turnRight(10);
      }
    }
    forward(1);
    c = 3;
    Serial_port();
    lcd.clear();
    lcd.print("F");
    lcd.print("   dist = ");
    lcd.print(dist);
  }
  else {
    if (inchesRC < inchesLC && inchesRC <= k1) {
      turnLeft(15);
    }
    else if (inchesRC > inchesLC && inchesLC <= k1) {
      turnRight(15);
    }
    else if (inchesR < inchesL) {
      turnRight(50);
      stopcar(1);
    }
    else if (inchesR > inchesL) {
      turnLeft(50);
      stopcar(1);
    }
    forward(100);
    c = 3;
    Serial_port();
  }
  TF();
  UI();
}
void UI() {                                //超音波副程式
  pinMode(pingPinL, OUTPUT); //輸出
  digitalWrite(pingPinL, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPinL, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPinL, LOW);
  pinMode(pingPinL, INPUT); //輸入
  durationL = pulseIn(pingPinL, HIGH, 10000);  //距離最大值大該在150左右
  inchesL = durationL * 0.034 / 2;
  if (inchesL == 0) {
    inchesL = 200;
  }
  pinMode(pingPinR, OUTPUT);  //輸出
  digitalWrite(pingPinR, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPinR, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPinR, LOW);
  pinMode(pingPinR, INPUT);  //輸入
  durationR = pulseIn(pingPinR, HIGH, 10000);  //距離最大值大該在150左右
  inchesR = durationR * 0.034 / 2;
  if (inchesR == 0) {
    inchesR = 200;
  }
  pinMode(pingPinLC, OUTPUT);
  digitalWrite(pingPinLC, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPinLC, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPinLC, LOW);
  pinMode(pingPinLC, INPUT);
  durationLC = pulseIn(pingPinLC, HIGH, 10000);  //距離最大值大該在150左右
  inchesLC = durationLC * 0.034 / 2;
  if (inchesLC == 0) {
    inchesLC = 200;
  }
  pinMode(pingPinRC, OUTPUT);
  digitalWrite(pingPinRC, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPinRC, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPinRC, LOW);
  pinMode(pingPinRC, INPUT);
  durationRC = pulseIn(pingPinRC, HIGH, 10000);  //距離最大值大該在150左右
  inchesRC = durationRC * 0.034 / 2;
  if (inchesRC == 0) {
    inchesRC = 200;
  }
}
void TF() {                                //紅外線測距程式
  if (myLidarLite.distance() < 6000) {
    dist = myLidarLite.distance();
  }
  else {
    dist = 6000;
  }
  delay(10);
}
void backward(int time) {                   //前進副程式
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
  delay(time);
}
void turnRight(int time) {                 //右轉副程式
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1700);
  delay(time);
}
void turnLeft(int time) {                  //左轉副程式
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1300);
  delay(time);
}
void forward(int time) {                  //後退副程式
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
  //servoRight.writeMicroseconds(1600);
  //  servoLeft.writeMicroseconds(1400);
  delay(time);
}
void stopcar(int time) {                   //停止副程式
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  delay(time);
}
void Serial_port() {                       //監看
  if (millis() >= time_1 + 100) {
    if (c == 1) {
      Serial.print("L");
      Serial.println(dist);
    }
    else if (c == 2) {
      Serial.print("R");
      Serial.println(dist);
    }
    else if (c == 3) {
      Serial.print("F");
      Serial.println(dist);
    }
    else if (c == 4) {
      Serial.print("l");
      Serial.println(dist);
    }
    else if (c == 5) {
      Serial.print("r");
      Serial.println(dist);
    }
    time_1 = millis();
  }
}
