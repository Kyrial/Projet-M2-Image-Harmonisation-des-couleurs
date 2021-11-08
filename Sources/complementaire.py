import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieCompl(histo, img, verbose = True):
    #le mode correspond a un p
    #mode = couleur, occurance 
    mode = (0,0)

    ite = 0
    for key, value in histo.items():
        ite+=1
        color = list(key)
      #  print(color)
        #calcul de la couleur complémentaire
        colorCompl = [abs(255-color[0]),abs(255-color[1]),abs(255-color[2])]
                
        #on prend en compte aussi les voisines
        somme =sommeVoisine(histo,color) + sommeVoisine(histo, colorCompl)

        if somme > mode[1]:
            mode = (color, somme)
        if verbose:
            verbosePourcent(ite, len(histo))
       # print("de la recherche de la meilleurs harmonie")
    modeCompl = [abs(255-mode[0][0]),abs(255-mode[0][1]),abs(255-mode[0][2])]

    print("couleur :        ", mode[0])
    print("complémentaire : ", modeCompl)
    print("nbOcc : ", mode[1])    
    #on harmonise les couleur de l'image
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            #calcul de la distance entre le mode et le complémentaire
            #on modifie les pixel courant

        
            distColor = distance(mode[0], img[i,j])
            distCompl = distance(modeCompl, img[i,j])
            if distColor < distCompl:
                color = mode[0]
                dist = distColor
            else:
                color = modeCompl
                dist = distCompl
            
            
            for k in range(3):
                """
                distColor = distanceComp(mode[0], img[i,j],k)
                distCompl = distanceComp(modeCompl, img[i,j],k)
                if distColor < distCompl:
                    color = mode[0]
                    #dist = distColor
                else:
                    color = modeCompl
                    #dist = distCompl 
                """
                dist = distanceComp(color, img[i,j], k)
                
                    #plusieur choix de fonction possible ? sqrt ?
                #formule =  min(math.exp(dist/15)-1,20)
                #formule = math.sqrt(dist)
                #formule = max(0,math.floor(25/(1+math.exp(-(dist-70)/8))-1 ))   #sigmoïde
                #formule =  min(math.exp(dist/15)-1,2)
                pivot =distanceComp(mode[0], modeCompl,k)/4
                if dist<pivot:
                    formule = dist/2
                if(dist>pivot and not ifMilieux(img[i,j],mode[0],modeCompl,k)):
                    formule = pivot/2
                else:
                    formule = (pivot/2)-dist/2
                formule = min(60,max(0,math.floor(formule)))                
                if color[k] > img[i,j][k]:
          
                    img.itemset((i,j,k), img.item(i,j,k)+formule)
                else:
                    img.itemset((i,j,k), img.item(i,j,k)-formule)
            



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "cat3"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



histo = getHisto(img)
            

findBestHarmonieCompl(histo, img)
#findBestHarmonieTriad(histo, img)

cv2.imwrite("../Images/Outputs/"+filename+"_Compl.jpg", img)



                
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
