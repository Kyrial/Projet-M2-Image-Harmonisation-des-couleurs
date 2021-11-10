import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieMono(histo, img, L, verbose = True):
	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			b, r, g = img.item(i,j,0), img.item(i,j,1), img.item(i,j,2)
			gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
			rp, gp, bp = L[0]/255, L[1]/255, L[2]/255








			img[i,j] = [gray*rp,gray*gp,gray*bp]










#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "cat3"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



histo = getHisto(img)
     

#findBestHarmonieCompl(histo, img)
findBestHarmonieMono(histo, img, [255,0,255])

#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_monoHSV.jpg", hsvImage)
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_mono.jpg", img)










