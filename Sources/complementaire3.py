import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieMono(histo, img, L, verbose = True):
	
	bb, rb, gb = L[0], L[1], L[2]
	bc, rc, gc = abs(255-bb), abs(255-rb), abs(255-gb)
	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			b, r, g = img.item(i,j,0), img.item(i,j,1), img.item(i,j,2)
			dist1 = distance([b,g,r], [bb,gb,rb])
			dist2 = distance([b,g,r], [bc,gc,rc])
			gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

			if(dist1<dist2):
				img[i,j] = [gray*(bb/255),gray*(rb/255),gray*(gb/255)]
			else:
				img[i,j] = [gray*(bc/255),gray*(rc/255),gray*(gc/255)]







#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "cat3"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




histo = getHisto(img)
     

#findBestHarmonieCompl(histo, img)
findBestHarmonieMono(histo, img,[150,180,60])

#cv2.imwrite("../Images/Outputs/"+filename+"_Comp3.jpg", img)








