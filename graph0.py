import matplotlib.pyplot as plt
import numpy as np
import serial
import time
plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,2,25,80])#X=0-2,Y=25-30
A = []
b = []
ser=serial.Serial('COM3',9600,timeout=1000)
i=0
x=list()
y=list()
time.sleep(5)
while (1):
    val=ser.readline()
    if val.find("\n"):
        a = val.replace("\r\n","")
        b = a.replace("\xc2\xa5n","")
        b = b.replace(".","")
        A = b.split(",")

        a1 = A[1]
        a1=long(a1)
        a1=a1*1.0/100

        a2 = A[0]
        a2=long(a2)
        a2=a2*1.0/100

        print a1
        print a2


        x.append(i)
        y.append(a1)
        plt.scatter(i,a1,c='blue')
        i+=150*1.0/3600*1.0
        #temp_y=np.random.random()
        x.append(i)
        y.append(a2)
        plt.scatter(i,a2,c='red')
        i+=150*1.0/3600*1.0
        plt.show()
        plt.pause(2.50) #Note this correction
