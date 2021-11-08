import cv2
import random
import math


#permet d'afficher les pourcentage de progression
def verbosePourcent(current, valMax):
    if verbosePourcent.pourcent < int(current*100/valMax):
        print("\033[A                             \033[A")
        print( int(current*100/valMax) , "%" )
        verbosePourcent.pourcent = int(current*100/valMax)
    if verbosePourcent.pourcent ==100:
        verbosePourcent.pourcent = 0 # reset le compteur une fois 100% atteint
verbosePourcent.pourcent=0


##


#somme l'occurance des pixel voisin de la couleur courante
def sommeVoisine(histo,color, distanceVoisin = 3):
    #distanceVoisin = 3
    voisins = range(-distanceVoisin, distanceVoisin)
    
    somme = 0
    #Parourt les 8 voisins de color
    for b, g, r in zip(voisins,voisins, voisins):
        colorV = (color[0] + b, color[1] + g, color[2] + r)
        if colorV in histo.keys():
           somme += histo[colorV]
    return somme

        
#retourne la distance entre deux couleurs
def distance(color, couleur):
    dist = math.sqrt(pow(color[0] - couleur[0], 2) +
                    pow(color[1] - couleur[1], 2) +
                    pow(color[2] - couleur[2], 2));
    return dist
def distanceComp(color, couleur, comp):
    dist = abs(color[comp] - couleur[comp]);
    return dist

def ifMilieux(isMid, color2, color3, k):
    if (color2[k] > isMid[k] and isMid[k] > color3[k]) or (color2[k] < isMid[k] and isMid[k] < color3[k]):
        return True
    else: return False

def getHisto(img):
    histo = {}
    #parcours de l'image pour remplir l'histogramme
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            pixel = img[i,j]
            
            if tuple(pixel) in histo.keys():
                histo[tuple (pixel)] = histo[tuple (pixel)]+ 1
            else:
                histo[tuple(pixel)] = 1
    return histo





