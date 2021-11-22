import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieAnalogue(histoHSV, imgHSV, verbose = True):
    ecart = 10
    #le mode correspond a un p
    #mode = couleur, occurance 
    mode = (0,0)
    ite = 0
    for key, value in histoHSV.items():
        ite+=1
        color = key #teinte de la couleur
      #  print(color)
        #calcul de la couleur complémentaire
        colorA = (color-ecart)%180
        colorB = (color+ecart)%180
        #on prend en compte aussi les voisines
        #somme =sommeVoisine(histoHSV,color) + sommeVoisine(histoHSV, colorCompl)
        somme = sommeVoisinHSV(histoHSV, color)+ sommeVoisinHSV(histoHSV, colorB)+ sommeVoisinHSV(histoHSV, colorA)

        if somme > mode[1]:
            mode = (color, somme)
        if verbose:
            verbosePourcent(ite, len(histoHSV))

        modecolorA = (mode[0]-ecart)%180
        modecolorB = (mode[0]+ecart)%180

    print("couleur :        ", mode[0])
    print("analogue1 : ", modecolorA)
    print("analogue2 : ", modecolorB)
    print("nbOcc : ", mode[1])
    #on harmonise les couleur de l'image
    for i in range(0,imgHSV.shape[0]):
        for j in range(0,imgHSV.shape[1]):
            #calcul de la distance entre le mode et le complémentaire
            #on modifie les pixel courant        
            distColor = abs(mode[0]-imgHSV[i,j][0])# distanceComp(mode[0], img[i,j],0)
            distcolorA = abs(modecolorA-imgHSV[i,j][0]) #distanceComp(modeCompl, img[i,j],0)
            distcolorB = abs(modecolorB-imgHSV[i,j][0])

            if not(distcolorA <ecart and distcolorB<ecart):
                if distcolorA < distcolorB:
                    imgHSV.itemset((i,j,0),modecolorA)
                else:
                    imgHSV.itemset((i,j,0),modecolorB)
    couleurs = vignette([mode[0],modecolorA,modecolorB])
    cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Analogue_converge_Vignette.jpg", couleurs)
            



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

#filename = "cat3"
filename = "tulipes"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
#ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


histoHSV = getHistoHSV(img)


hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
max =0
for i in range(0,hsvImage.shape[0]):
    for j in range(0,hsvImage.shape[1]):
        if max< hsvImage[i,j][0]:
            max = hsvImage[i,j][0]


print("max teinte   : ",max ,"\n\n\n")
#print("couleur   : ",hsvImage[0,0])

findBestHarmonieAnalogue(histoHSV, hsvImage)
#findBestHarmonieTriad(histo, img)

img = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_AnalogueHSV.jpg", hsvImage)
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Analogue_converge.jpg", img)



                
#for key, value in histo.items():
 #   if value >100:
  #      print(key[2], '    ', value)













#print(len(histo));
#print("miaou")
#print(img.shape);
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)











#for i in range(0,img.shape[0]):
#    for j in range(0,img.shape[1]):
#        pixel = img[i, j];
#        pixel = img.item(i, j,0)
#        print (pixel)


#img.itemset((50, 50, 1), 25)


"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread ("fleur.png");
#RGB -> HSV.
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#Déclaration des couleurs des courbes
color = ('r','g','b')
#Déclaration des noms des courbes.
labels = ('h','s','v')
#Pour col allant r à b et pour i allant de 0 au nombre de couleurs
for i,col in enumerate(color):
    #Hist prend la valeur de l'histogramme de hsv sur la canal i.
    hist = cv.calcHist([hsv],[i],None,[256],[0,256])
    # Plot de hist.
    plt.plot(hist,color = col,label=labels[i])
    plt.xlim([0,256])
#Affichage.
plt.show()
"""
