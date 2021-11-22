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

    print("couleur :        ", mode[0])
    print("complémentaire : ", modeCompl)
    print("nbOcc : ", mode[1])
    #on harmonise les couleur de l'image
    dif=45
    a=0
    b=0
    c=0  
    d=0    
    e=0
    for i in range(0,imgHSV.shape[0]):
        for j in range(0,imgHSV.shape[1]):
            #calcul de la distance entre le mode et le complémentaire
            #on modifie les pixel courant  
            
            
            distColor = distModulo_WithoutAbs(mode[0],imgHSV[i,j][0], 179)    # abs(mode[0]-imgHSV[i,j][0])# distanceComp(mode[0], img[i,j],0)
            distCompl = distModulo_WithoutAbs(modeCompl,imgHSV[i,j][0], 179)   # abs(modeCompl-imgHSV[i,j][0]) #distanceComp(modeCompl, img[i,j],0)
            distColora = abs(distColor)
            distCompla = abs(distCompl)
            if abs(distColor) < abs(distCompl):
                
                if(distColora<imgHSV[i,j][0]<distCompla or  distColora>imgHSV[i,j][0]): 
                    imgHSV.itemset((i,j,0),mode[0]*(distColor/dif) + (imgHSV[i,j][0]*(1-distColor/dif)))
                    a+=1
                elif (distColora<distCompla<imgHSV[i,j][0]) :
                    b+=1
                    colors=imgHSV[i,j][0]-255
                    imgHSV.itemset((i,j,0),mode[0]*(distColor/dif) + (colors*(1-distColor/dif)))
                elif (distColora>distCompla>imgHSV[i,j][0]) :
                    b+=1
                    colors=imgHSV[i,j][0]+255
                    imgHSV.itemset((i,j,0),mode[0]*(distColor/dif) + (colors*(1-distColor/dif)))
                else:
                    e+=1
            else:
                
                if(distCompla<imgHSV[i,j][0]<distColora or  distCompla>imgHSV[i,j][0]):
                    c+=1
                    imgHSV.itemset((i,j,0),modeCompl*(distCompl/dif)+ (imgHSV[i,j][0]*(1-distCompl/dif)))
                elif (distCompla<distColora<imgHSV[i,j][0]) :
                    d+=1
                    colors=imgHSV[i,j][0]-255
                    imgHSV.itemset((i,j,0),mode[0]*(distCompl/dif) + (colors*(1-distCompl/dif)))
                elif (distCompla>distColora>imgHSV[i,j][0]) :
                    d+=1
                    colors=imgHSV[i,j][0]+255
                    imgHSV.itemset((i,j,0),mode[0]*(distCompl/dif) + (colors*(1-distCompl/dif)))
                else:
                    e+=1

    print(a,b,c,d,e)

            



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "tulipes"
#filename = "fleurs"
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
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_ComplHSV2.jpg", hsvImage)
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Compl42.jpg", img)


