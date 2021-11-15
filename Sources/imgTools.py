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
    dist = abs(color[comp] - couleur[comp])
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

def getHistoHSV(img):
    histo = {}
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(0,hsvImage.shape[0]):
        for j in range(0,hsvImage.shape[1]):
            pixel = hsvImage[i,j]
            if pixel[0] in histo.keys():
                histo[pixel[0]] = histo[pixel[0]]+ 1
            else:
                histo[pixel[0]] = 1
    return histo

def sommeVoisinHSV(histoHSV, teinte):
    somme = 0;
    if teinte in histoHSV.keys():
        somme = somme + histoHSV[teinte]
    return somme;

# Different applications use different scales for HSV. 
#For example gimp uses H = 0-360, S = 0-100 and V = 0-100. 
#But OpenCV uses H: 0-179, S: 0-255, V: 0-255

def distModulo(val1, val2, maxVal):
    dist = abs(val1 - val2)
    return min(dist , maxVal- dist)

def distModulo_WithoutAbs(val1, val2, maxVal):
    dist = abs(val1 - val2)
    return min(dist , maxVal- dist) if val1 - val2 >= 0 else -min(dist , maxVal- dist)


def getDistofTuple(tupleTeinte, pixelHSV,):
    teinte = 255
    dist = 255
    for i in tupleTeinte:
        if distModulo(i, pixelHSV[0], 179) < dist:
            dist = distModulo(i, pixelHSV[0], 179)
            teinte = i
    return teinte, dist

def min_SUP_modulo(tupleTeinte, pixelHSV):
    teinte = 255
    dist = 255
    for i in tupleTeinte:
        if (pixelHSV[0] - i) %179:
            dist = (pixelHSV[0] - i) %179
            teinte = i
    return teinte, dist

def min_INF_modulo(tupleTeinte, pixelHSV):
    teinte = 255
    dist = 255
    for i in tupleTeinte:
        if (i -pixelHSV[0]) %179:
            dist = (i -  pixelHSV[0]) %179
            teinte = i
    return teinte, dist










def chooseColor(tupleTeinte,pixelHSV):
    teinte_inf, dist_inf = min_INF_modulo(tupleTeinte, pixelHSV)
    teinte_sup, dist_sup = min_SUP_modulo(tupleTeinte, pixelHSV)
    
    
    distModulo = (dist_sup - dist_inf) % 179
    
    if dist_inf < dist_sup:
        formule = dist_inf/2
        return (pixelHSV[0] -formule) %179
    else:
        formule = dist_sup/2
        return (pixelHSV[0] + formule) %179
    

    """
    formule = dist1/2
    if(len(tupleTeinte)>1):
        teinte2, dist2 = getDistofTuple(list(tupleTeinte).remove(teinte1), pixelHSV)

        distpivot = asb(dist1 - dist2)/2
        if dist>distpivot//2:
            formule = (pivot/2)-dist/2
    """


"""
distColor = mode[0]-imgHSV[i,j][0]
distCompl = modeCompl-imgHSV[i,j][0]
            if abs(distColor) < abs(distCompl):

                imgHSV.itemset((i,j,0),mode[0]*(distColor/45) + (imgHSV[i,j][0]*(1-distColor/45)))
            else:

                imgHSV.itemset((i,j,0),modeCompl*(distCompl/45)+ (imgHSV[i,j][0]*(1-distCompl/45)))
"""
    

