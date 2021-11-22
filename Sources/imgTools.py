import cv2
import random
import math
import numpy as np


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
    dist = int(abs(int(val1) - int(val2)))
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

def min_INF_modulo(tupleTeinte, pixelHSV):
    teinte = 255
    dist = 255
    for i in tupleTeinte:
    #    print("distINF : ",i," pixel :",pixelHSV," ",     (pixelHSV- i) %180)
        if (pixelHSV - i) %180 < dist:
            dist = (pixelHSV - i) %180
            teinte = i
    return teinte, dist

def min_SUP_modulo(tupleTeinte, pixelHSV):
    teinte = 255
    dist = 255
    for i in tupleTeinte: 
      #  print("(i -pixelHSV)  ", (i -pixelHSV),"     (i -pixelHSV[0])%180   ", (i -pixelHSV)%180)

     #   print("distSUP : ",i," pixel :",pixelHSV," ", (i -pixelHSV) %180)
        if (i -pixelHSV) %180 < dist:
            dist = (i -  pixelHSV) %180
            teinte = i
    return teinte, dist


def vignette(colors):
    img2 = np.zeros((50,100,3),dtype=np.uint8)
    imghsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    for i in range(50):
        for j in range(100):
            imghsv2.itemset((i,j,1),179)
            imghsv2.itemset((i,j,2),179)
            #if j<(100//len(colors)):
            imghsv2.itemset((i,j,0),colors[math.floor(j/math.ceil(100/len(colors)))])
            #else:
             #   imghsv2.itemset((i,j,0),colors[1])
    img2 = cv2.cvtColor(imghsv2, cv2.COLOR_HSV2BGR)
    return img2









def chooseColor(tupleTeinte,pixelHSV):
    teinte_inf, dist_inf = min_INF_modulo(tupleTeinte, pixelHSV)
    teinte_sup, dist_sup = min_SUP_modulo(tupleTeinte, pixelHSV)
    
    
    distModulo = (dist_sup - dist_inf) % 180
    
    if dist_inf < dist_sup:
        formule = dist_inf/2
        return (pixelHSV[0] -formule) %180
    else:
        formule = dist_sup/2
        return (pixelHSV[0] + formule) %180
    

    """
    formule = dist1/2
    if(len(tupleTeinte)>1):
        teinte2, dist2 = getDistofTuple(list(tupleTeinte).remove(teinte1), pixelHSV)

        distpivot = asb(dist1 - dist2)/2
        if dist>distpivot//2:
            formule = (pivot/2)-dist/2
    """


def getColor_Degrader(tupleTeinte,pixelHSV):
    teinte_inf, dist_inf = min_INF_modulo(tupleTeinte, int(pixelHSV[0]))
    teinte_sup, dist_sup = min_SUP_modulo(tupleTeinte, int(pixelHSV[0]))
  #  print("tuple ::    ", tupleTeinte)
    #print("couleur = ", pixelHSV[0])
   # print("inf  ",teinte_inf, dist_inf)
    #print("sup  ",teinte_sup, dist_sup)
    couleur = pixelHSV[0]
    if(dist_inf ==0 or dist_inf == dist_sup):
        return couleur

    #Pivot = (dist_sup - dist_inf) % 180
    Pivot = abs(teinte_sup - teinte_inf)
    if teinte_inf >teinte_sup or Pivot == 0 :
   #     print("ici")
        Pivot = 180 -teinte_inf+ teinte_sup
    #print("pivot  ", Pivot)
    Pivot = Pivot/2
    if dist_inf < dist_sup:
     #   print('dist_inf   ', dist_inf, "   couleur, ", couleur, "  teinte_inf", teinte_inf, "   pivot ", Pivot)
        if couleur < teinte_inf:
            couleur = couleur + 180
      #      print('COOUULLEUUR   ', couleur)
       #     print("coucou ", couleur,"\n")
       #     print("pivott", Pivot," \n")
        return (teinte_inf * (1 - (dist_inf/Pivot)) + (couleur * (dist_inf/Pivot)))%180
    else:
        if couleur > teinte_sup:
       #     print("Thym -> ", couleur,"  thym superieur = ", teinte_sup )
            teinte_sup = teinte_sup + 180
      #  print(" thym superieur = ", teinte_sup, "  pivot = ", Pivot, "  dist sup ",dist_sup )
        return ((teinte_sup * (1 - dist_sup/Pivot)) + (couleur * (dist_sup/Pivot)))%180


"""
print('test1  ', getColor_Degrader( (103,13), [145]), "\n\n")
print('\ntest2  ', getColor_Degrader( (103,13), [141, 7,252]), "\n\n")
"""
"""
print('\ntest3  120 ', getColor_Degrader( (13,103), [120, 7, 252]), "\n\n")
print('\ntest3  130 ', getColor_Degrader( (13,103), [130, 7, 252]), "\n\n")
print('\ntest3  140 ', getColor_Degrader( (13,103), [140, 7, 252]), "\n\n")

print('\ntest3  140 ', getColor_Degrader( (13,103), [140, 7, 252]) )
print('\ntest3  141 ', getColor_Degrader( (13,103), [141, 7, 252]))
print('\ntest3  142 ', getColor_Degrader( (13,103), [142, 7, 252]))
print('\ntest3  143 ', getColor_Degrader( (13,103), [143, 7, 252]))
print('\ntest3  144 ', getColor_Degrader( (13,103), [144, 7, 252]))
print('\ntest3  145 ', getColor_Degrader( (13,103), [145, 7, 252]))
print('\ntest3  146 ', getColor_Degrader( (13,103), [146, 7, 252]))
print('\ntest3  147 ', getColor_Degrader( (13,103), [147, 7, 252]))
"""
#print('\ntest3  148 ', getColor_Degrader( (13,103), [148, 7, 252]))
#print('\ntest3  149 ', getColor_Degrader( (13,103), [149, 7, 252]))
#for i in range(0,180,5):
 #  print('test3 ',i,"  ", getColor_Degrader( (13,103), [i, 7, 252]),"\n" )

"""
print('\ntest3  ', getColor_Degrader( (150,10), [50]), "\n\n")
print('\ntest4  ', getColor_Degrader( (170,20), [2]), "\n\n") #pas bon
print('\ntest4  ', getColor_Degrader( (150,5), [178]), "\n\n")
"""