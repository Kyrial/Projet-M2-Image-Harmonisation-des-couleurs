import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieMono(histo, img, L, verbose = True):


	bb, rb, gb = L[0], L[1], L[2]
	b1, r1, g1 = L[2], L[0], L[1]
	b2, r2, g2 = L[1], L[2], L[0]
	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			b, r, g = img.item(i,j,0), img.item(i,j,1), img.item(i,j,2)
			dist1 = distance([b,g,r], [bb,gb,rb])
			dist2 = distance([b,g,r], [b1,g1,r1])
			dist3 = distance([b,g,r], [b2,g2,r2])
			gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

			if(dist1<=dist2<=dist3 or dist1 <= dist3 <= dist2):
				img[i,j] = [gray*(bb/255),gray*(rb/255),gray*(gb/255)]
			elif (dist2 < dist3):
				img[i,j] = [gray*(b1/255),gray*(r1/255),gray*(g1/255)]
			else:
				img[i,j] = [gray*(b2/255),gray*(r2/255),gray*(g2/255)]

			if verbose:
				verbosePourcent(i*img.shape[0]+j, img.shape[0]*img.shape[1])







#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "yo"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



histo = {} # getHisto(img)
     

#findBestHarmonieCompl(histo, img)
findBestHarmonieMono(histo, img,[191,107,160])

cv2.imwrite("../Images/Outputs/"+filename+"_try2.jpg", img)



























