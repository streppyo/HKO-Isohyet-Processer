import glob
import cv2
import requests
import urllib
import math, sys, os
from datetime import datetime, timedelta

import numpy as np


import hkoiso




def GenerateIsohyet(date):

    img_height, img_width = 545, 550
    n_channels = 4
    transparent_img = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)

    #check if date & time equal today
    currDT = datetime.now()
    if currDT.strftime("%m%d") == date:
        hh = (currDT - timedelta(hours = 1)).strftime("%H") if int(currDT.strftime("%M")) < 15 else currDT.strftime("%H")
        mm = '30' if int(currDT.strftime("%M")) > 45 else '15' if int(currDT.strftime("%M")) > 30 else '00' if int(currDT.strftime("%M")) > 15 else '45'
        url = r"https://www.hko.gov.hk/wxinfo/rainfall/cokrig_barnes/rfmapmid" + hh + mm + "e.png"
    else:
        url = r"https://www.hko.gov.hk/wxinfo/rainfall/cokrig_barnes/rfmap24hrs" + date + "0000e.png"
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    images = cv2.imdecode(arr, 1)

    mask = cv2.inRange(images, hkoiso.blacklower, hkoiso.blackupper)
    transparent_img[np.where(mask!=0)] =  [0,0,0,255]

    for layer in hkoiso.isohyetLayerList:
        print('Processing ' + str(layer.rainfall))
        mask = cv2.inRange(images, layer.lower, layer.upper)
        transparent_img[np.where(mask!=0)] =  layer.color
        cv2.imwrite(os.path.dirname(os.path.abspath(__file__)) + r"/static/images/" + date + ".png", transparent_img, [cv2.IMWRITE_JPEG_QUALITY, 80])


    cv2.destroyAllWindows()

if __name__ == '__main__':
    GenerateIsohyet(sys.argv[1])
