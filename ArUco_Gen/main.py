from re import M
import cv2 as cv
from cv2 import aruco  # module to generate markers
import numpy as np

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)  #dictoneary generate type of marker 4X4 type 50 numbers of marker

MARKER_SIZE = 400    #pixcel size of markers

# generateing 20 number of mrkers 
for id in range(20):
    marker_image = aruco.drawMarker(marker_dict, id, MARKER_SIZE) #drawing the marker
    #cv.imshow('img', marker_image)
    #cv.waitKey(0)
    #break
    cv.imwrite(f'markers/marker_{id}.png', marker_image)
