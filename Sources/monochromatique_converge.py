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
        #on prend en compte aussi les voisines
        #somme =sommeVoisine(histoHSV,color) + sommeVoisine(histoHSV, colorCompl)
        somme = sommeVoisinHSV(histoHSV, color)

        if somme > mode[1]:
            mode = (color, somme)
        if verbose:
            verbosePourcent(ite, len(histoHSV))


    print("couleur :        ", mode[0])
    print("nbOcc : ", mode[1])
    tupleTeinte = [int(mode[0])]
    #on harmonise les couleur de l'image
    for i in range(0,imgHSV.shape[0]):
        for j in range(0,imgHSV.shape[1]):
                #imgHSV.itemset((i,j,0),mode[0])
                colorcurr = (imgHSV[i,j])
                imgHSV.itemset((i,j,0),   getColor_Degrader(tupleTeinte,colorcurr ))



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "fleurs"
#filename = "tulipes"
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

findBestHarmonieCompl(histoHSV, hsvImage)
#findBestHarmonieTriad(histo, img)

img = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_monoHSV.jpg", hsvImage)
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Triadique_converge.jpg", img)


