import numpy as np
import pandas as pd
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats

import re
#2588
"""
x = int(input())
y = int(input())
val3 = int(x * (y%10))
val4 = int((x * (y%100 - y%10))/10)
val5 = int((x * (y - (y%100)))/100)
val6 = val3 + (val4*10) + (val5*100)
print("%d\n%d\n%d\n%d" % (val3,val4,val5,val6))

#1330

i,j = (input().split())
x = int(i)
y = int(j)
if(x>y):
    print(">")
elif(x<y):
    print("<")
else:
    print("==")

#14681

xq = int(input())
yq = int(input())
if(xq>0 and yq>0):
    print(1)
elif(xq<0 and yq>0):
    print(2)
elif(xq<0 and yq<0):
    print(3)
else:
    print(4)

#2884
i,j = input().split()
h = int(i)
m = int(j)
if(m<45):
    if(h ==0):
        print("%d %d" % (23,m+15))
    else:
        print("%d %d" % (h-1,m+15))
else:
    print("%d %d" % (h, m-45))

#11021
case = int(input())
a,b = [],[]
for x in range(case):
    i,j = input().split()
    a.append(int(i))
    b.append(int(j))
for y in range(case):
    print("Case #%d: %d" % (y+1, a[y]+b[y]))

#10952
while(1):
    i,j = input().split()
    x , y = int(i),int(j)
    if(x ==0 and y==0):
        break
    else:
        print("%d" % (x+y))

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) > 0:
        print(x)
        
title = ["내달 금리ㄹㅇㄴㅁ인하 전망… 유동성 활용 가능성도","씨발 왜금리씨발인하","금리dsa인하","금리인하fdsa","fdas금리인하","fdsa금리fds인하","금리씨발아아앙인하"]
for titles in title:
    titles = titles.rstrip()
    if re.findall('\S?금리.*인하\S?', titles):
        print(titles)
"""
for i in range(10):
    print(i)