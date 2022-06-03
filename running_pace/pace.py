import matplotlib.pyplot as plt
import numpy as np
import time
import datetime

def get_float_seconds(dt):
    return float(dt.hour * (60*60) + dt.minute *(60) + dt.second + float(dt.microsecond)/1000000.0)

records = [
    (60, "0:0:6.34","Christian Coleman",2018),
    (100,"0:0:9.58","Usain Bolt", 2009),
    (200,"0:0:19.19","Usain Bolt", 2009),
    (400,"0:0:43.03","Wayde Van NIEKERK", 2016),
    (800,"0:1:40.91","David Rudisha", 2012),
]

distance = [x[0] for x in records]
seconds = [datetime.datetime.strptime(x[1],"%H:%M:%S.%f") for x in records]
pace=[get_float_seconds(y)/(float(x)/float(1600.0)) for x,y in zip(distance,seconds)]
#fpace=[datetime.datetime.strptime(str(x),"%S.%f") for x in pace]
print(pace)
fpace=[datetime.timedelta(seconds=x) for x in pace]
print(str(fpace))


plt.xlabel("meters")
#plt.plot(distance, seconds)
plt.plot(distance, fpace)
plt.savefig("pace.pdf")