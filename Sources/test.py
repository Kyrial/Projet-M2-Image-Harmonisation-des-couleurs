import cv2
import random
import math





def convertIndexToRGB(ImgIndex, ImgOut, palette):
    for i in range(0,ImgOut.shape[0]):
        for j in range(0,ImgOut.shape[1]):
            ImgOut[i][j]= (palette[ImgIndex[i][j]][0], palette[ImgIndex[i][j]][1], palette[ImgIndex[i][j]][2]);



def k_mean(img, palette, indexPalette,  i,j):
    dist = math.sqrt(pow(img.item(i, j,0) - palette[indexPalette][0], 2) +
                    pow(img.item(i, j,1) - palette[indexPalette][1], 2) +
                    pow(img.item(i, j,2) - palette[indexPalette][2], 2));
    return dist

def remplirPalette(palette, taillePalette):
    #srand (time(NULL));
    #srand (10);
    for i in range(taillePalette):
        #palette.append(random.randint(0,256))
        palette = [[random.randint(0,256) for i in range(3)] for j in range(taillePalette)]
    return palette
        
def parcoursMoyenneK_mean( paletteMoy,  sommeC,  nbC):
    for j in range(len(paletteMoy)):
    #    print(j)
        paletteMoy[j][0] = (int) (sommeC[j][0]/max(nbC[j],1));
        paletteMoy[j][1] = (int) (sommeC[j][1]/max(nbC[j],1));
        paletteMoy[j][2] = (int) (sommeC[j][2]/max(nbC[j],1));
    return paletteMoy


def parcoursK_mean( ImgIn, ImgIndex,  palette,   sommeC ,  nbC):
    for i in range(0,img.shape[0]):
       # print("dd   ", i)    
        for j in range(0,img.shape[1]):
            
            indexMin = 0;
            distMin = k_mean(ImgIn, palette, 0,i,j);
 
            for k in range(1,len(palette)):
                dist = k_mean(ImgIn,palette, k, i, j)
                if dist< distMin:
                    distMin = dist
                    indexMin = k
                    if distMin ==0:
                        break
            ImgIndex[i, j] = indexMin;
            nbC[indexMin]+=1
            sommeC[indexMin][0] += ImgIn.item(i, j,0)
            sommeC[indexMin][1] += ImgIn.item(i, j,1)
            sommeC[indexMin][2] += ImgIn.item(i, j,2)
            
    return sommeC, nbC

def ifSamePalette( palette, palettemoy):
    for i in range(256):
        for j in range(3):
            if abs(palette[i][j]-palettemoy[i][j])>4:
                print("diff à ", i);
                return False;
    return True;


def convergence(ImgIn, ImgIndex, palette, paletteMoy): #, sommeC, nbC ):
    i=0;
    sommeC = [[0 for i in range(3)] for j in range(len(palette))]
    nbC = [0 for j in range(len(palette))]

    while(True):
        print("miaou")
        palette = parcoursMoyenneK_mean( palette,  sommeC,  nbC);
       # parcoursMoyenneK_mean(palette, sommeC, nbC, taillePalette);
        sommeC = [[0 for i in range(3)] for j in range(len(palette))]
        nbC = [0 for j in range(len(palette))]
        print("blabla")
        sommeC, nbC = parcoursK_mean(ImgIn, ImgIndex,  palette,   sommeC ,  nbC)
        print("piou piaou")
        paletteMoy = parcoursMoyenneK_mean( paletteMoy,  sommeC,  nbC)
        print("maeo")
        i+=1
        print(i)
        if ifSamePalette(palette, paletteMoy):
            break;
    return paletteMoy







#read picture
img = cv2.imread ("../Images/Inputs/cat3.jpg")
ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


taillePalette = 256;
palette = []
paletteMoy = []

palette = remplirPalette(palette, taillePalette)
paletteMoy = remplirPalette(paletteMoy, taillePalette);


paletteMoy = convergence(img, ImgIndex, palette, paletteMoy)
    
convertIndexToRGB(ImgIndex, img, paletteMoy)

cv2.imwrite("../Images/Outputs/chat3_palette.jpg", img)







print("miaou")
print(img.shape);
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
