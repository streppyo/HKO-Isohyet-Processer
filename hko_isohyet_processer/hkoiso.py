
import numpy as np


class isohyetlayer:
    def __init__(self, r, l, u, c):
        self.rainfall = r
        self.lower = l
        self.upper = u
        self.color = c


def ColorEncode(array):
      output = []
      output.append(array[0] * 255/360)
      output.append(array[1] * 255/100)
      output.append(array[2] * 255/100)
      return output


x_2 = isohyetlayer(2,np.array([0,220,0]),np.array([255,255,50]),[255,110,110,10])
x_5 = isohyetlayer(5,np.array([205,200,0]),np.array([210,230,50]),[255,110,110,20])
x_10 = isohyetlayer(10,np.array(ColorEncode([30,0,0])),np.array(ColorEncode([40,100,100])),[255,110,110,30])
x_20 = isohyetlayer(20,np.array(ColorEncode([45,80,0])),np.array(ColorEncode([50,100,100])),[255,110,110,50])
x_30 = isohyetlayer(30,np.array(ColorEncode([0,90,0])),np.array(ColorEncode([0,100,100])),[255,110,110,70])
x_40 = isohyetlayer(40,np.array(ColorEncode([0,80,0])),np.array(ColorEncode([0,90,100])),[255,110,110,90])
x_50 = isohyetlayer(50,np.array(ColorEncode([0,50,95])),np.array(ColorEncode([0,70,100])),[255,110,110,110])
x_70 = isohyetlayer(70,np.array(ColorEncode([0,20,70])),np.array(ColorEncode([0,50,100])),[255,110,110,130])
x_100 = isohyetlayer(100,np.array(ColorEncode([0,0,70])),np.array(ColorEncode([0,20,100])),[255,110,110,150])
x_140 = isohyetlayer(100,np.array(ColorEncode([120,0,50])),np.array(ColorEncode([150,20,70])),[255,110,110,170])
x_200 = isohyetlayer(200,np.array(ColorEncode([230,0,0])),np.array(ColorEncode([290,5,100])),[255,110,110,190])
x_300 = isohyetlayer(300,np.array(ColorEncode([250,5,0])),np.array(ColorEncode([310,10,100])),[255,110,110,210])
x_400 = isohyetlayer(400,np.array([220,90,240]),np.array([239,100,255]),[255,110,110,230])
x_500 = isohyetlayer(500,np.array([230,0,245]),np.array([240,235,255]),[255,110,110,240])
x_600 = isohyetlayer(600,np.array([240,0,240]),np.array([255,235,255]),[255,110,110,250])

isohyetLayerList = [x_2,x_5,x_10,x_20,x_30,x_40,x_50,x_70,x_100,x_140,x_200,x_300,x_400,x_500,x_600]

#Basic colours to be retained


whtielower = np.array([240,240,240])
whiteupper = np.array([255,255,255])

blacklower = np.array([0,0,0])
blackupper = np.array([80,80,80])
