import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieCompl(histoHSV, imgHSV, verbose = True):
    #le mode correspond a un p
    #mode = couleur, occurance 
    mode = (0,0)
    ite = 0
    for key, value in histoHSV.items():
        ite+=1
        color = key #teinte de la couleur
      #  print(color)
        #calcul de la couleur complémentaire
        colorCompl = (color+90)%180
        #on prend en compte aussi les voisines
        #somme =sommeVoisine(histoHSV,color) + sommeVoisine(histoHSV, colorCompl)
        somme = sommeVoisinHSV(histoHSV, color)+ sommeVoisinHSV(histoHSV, colorCompl)

        if somme > mode[1]:
            mode = (color, somme)
        if verbose:
            verbosePourcent(ite, len(histoHSV))

    modeCompl =  (mode[0]+90)%180
    if(verbose):
        print("couleur :        ", mode[0])
        print("complémentaire : ", modeCompl)
        print("nbOcc : ", mode[1])
    #on harmonise les couleur de l'image
    value = mode[0]
    tupleTeinte = [int(modeCompl),int(value)]
    dicodegrade = getDicoDegrade(tupleTeinte)

    h,s,v = cv2.split(imgHSV)
    for i in range(len(dicodegrade)):
        h[h==i] = dicodegrade[i]
    imgHSV = cv2.merge((h,s,v))


    '''for i in range(0,imgHSV.shape[0]):
        for j in range(0,imgHSV.shape[1]):
           # print("\nappel fonction: ",tupleTeinte,imgHSV[i,j] )
            colorcurr = (imgHSV[i,j])
            #imgHSV.itemset((i,j,0),   getColor_Degrader(tupleTeinte,colorcurr ))
            imgHSV.itemset((i,j,0),   dicodegrade[colorcurr[0]])'''
    couleurs = vignette([mode[0],modeCompl])
    return imgHSV
    #cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Compl_converge_Vignette.jpg", couleurs)
            



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

#filename = "cat3"
#filename = "tulipes"
#img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
#ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#histoHSV = getHistoHSV(img)


#hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#findBestHarmonieCompl(histoHSV, hsvImage)
#findBestHarmonieTriad(histo, img)

#img = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Compl100HSV.jpg", hsvImage)
#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Compl_converge.jpg", img)

