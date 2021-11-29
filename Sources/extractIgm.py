import cv2
import random
import math
from imgTools import *
import string, os 
from analogue_converge import *

dir = "../../dataset/jpg/"
ite = 0
verbose = True



for image in os.listdir(dir):

        
    #print(str(ite) + "  "+ str(len(os.listdir(dir)))+"   "+str(internIte)+"    "+ str(len(os.listdir(dir+curr_dir))))
    img = cv2.imread (dir+"/"+image)
    
    histoHSV = getHistoHSV(img)

    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    imgOut = findBestHarmonieAnalogue(histoHSV, hsvImage,False)
    resultat = cv2.cvtColor(imgOut, cv2.COLOR_HSV2BGR)

    cv2.imwrite("../Images/datasetAnalogue/"+image+"_Analogue_converge.jpg", resultat)
    
    if verbose:
        verbosePourcent(ite, len(os.listdir(dir)))
        
    ite=ite+1




"""
for curr_dir in os.listdir(dir):
    internIte=0
    for image in os.listdir(dir+curr_dir):
        
        #print(str(ite) + "  "+ str(len(os.listdir(dir)))+"   "+str(internIte)+"    "+ str(len(os.listdir(dir+curr_dir))))
        img = cv2.imread (dir+curr_dir+"/"+image)
        
        histoHSV = getHistoHSV(img)

        hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        imgOut = findBestHarmonieAnalogue(histoHSV, hsvImage,False)
        resultat = cv2.cvtColor(imgOut, cv2.COLOR_HSV2BGR)

        cv2.imwrite("../Images/datasetAnalogue/"+image+"_Analogue_converge.jpg", resultat)
       
        if verbose:

            verbosePourcentCombined(ite, len(os.listdir(dir)),internIte, len(os.listdir(dir+curr_dir)))
           
        internIte+=1
    ite=ite+1
"""