# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname="C:\Windows\Fonts\msgothic.ttc");
import serial
import time
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
A = []
b = []
tim=[30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
tem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ser=serial.Serial('COM12',9600,timeout=1)
i=0


time.sleep(5)
fig=plt.figure()
plt.axis([30,0,15,80])#X=30-0,Y=25-80


while True:
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    val=ser.readline()


    if val.find("\n"):
        a = val.replace("\r\n","")
        b = a.replace("\xc2\xa5n","")
        b = b.replace(".","")
        A = b.split(",")

        try:
            a1 = A[0]
            a1=long(a1)
            a1=a1*1.0/100
            a2 = A[1]
            a2=long(a2)
            a2=a2*1.0/100
            a11=str(a1)
            a21=str(a2)
            print "\n"
            print u"計測日時"+":\t"+time.asctime()
            print u"気温"+"\t:\t"+a11
            print u"湿度"+"\t:\t"+a21
            print "\n"
            del tem[0]
            del hum[0]
            tem.append(a1)
            hum.append(a2)
            plt.title(u"温湿度計", fontproperties = fp)
            plt.xlabel(u"経過時間 (分)", fontproperties=fp)
            plt.ylabel(u"温湿度", fontproperties=fp)
            plt.axis([30,0,20,80])
            plt.plot(tim,tem, color="r", label=u"温度 (℃)")
            plt.plot(tim,hum, color="b", label=u"湿度 (％)")
            plt.legend(prop = fp)
            if i<=32:
                plt.pause(.1)
                i+=1
            if i>=33:
                plt.pause(60)
            plt.clf()

        except:
            print"error"

if __name__ == "__main__":
    pause_plot()
