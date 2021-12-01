# -*- coding: utf-8 -*-
import cv2
import random
import math
from imgTools import *
import string, os 
from analogue_converge import *
from complementaire_converge import *
from complAdjacente_converge import *
from monochromatique_converge import *
from triadique_converge import *
from doubleComplementaire_converge import *

verbose = True




#import numpy
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import QMainWindow, QApplication












from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMenuBar, QMenu, QAction, QRadioButton,QColorDialog
from PyQt5.QtGui import QImage
import colorsys

import imutils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.loaded = False
        self.lastImage =0
        self.vignette = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 571)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
        self.label.setObjectName("label")


        self.vignetteLabel = QtWidgets.QLabel(self.centralwidget)
        self.vignetteLabel.setText("meow")
        #self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
        self.vignetteLabel.setObjectName("vignetteLabel")
        self.vignetteLayout = QtWidgets.QHBoxLayout()
        self.vignetteLayout.setObjectName("vignetteLayout")
        self.vignetteLayout.addWidget(self.vignetteLabel)
        self.gridLayout.addLayout(self.vignetteLayout, 0, 2, 1, 1)

        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        #Text for slider
        self.TexteLiderAnalogue = QtWidgets.QLabel(self.centralwidget)
        self.TexteLiderAnalogue.setText("écart analogue")
        self.TexteLiderAnalogue.setObjectName("écart analogue")
        self.TexteLiderAnalogue.setStyleSheet("QLabel { color : grey; }")

        #slider analogue
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setRange(1,179)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setObjectName("analogue")
        #Layout for text and slider analogue
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addWidget(self.TexteLiderAnalogue)
        self.horizontalLayout_4.addWidget(self.horizontalSlider)
        self.gridLayout.addLayout(self.horizontalLayout_4,4, 0, 1 , 1)

        #Text for slider
        self.TexteLiderAdjacente = QtWidgets.QLabel(self.centralwidget)
        self.TexteLiderAdjacente.setText("écart adjacente")
        self.TexteLiderAdjacente.setObjectName("écart analogue")

        #slider adjacente
        self.horizontalSlider2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider2.setRange(1,179)
        self.horizontalSlider2.setObjectName("adjacene")
        #Layout for text and slider adjacente
        self.horizontalLayout_4.addWidget(self.TexteLiderAdjacente)
        self.horizontalLayout_4.addWidget(self.horizontalSlider2)

        """
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        """
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        #layout harmonie
        self.harmonieLayout = QtWidgets.QHBoxLayout()
        self.harmonieLayout.setObjectName("harmonieLayout")
        self.gridLayout.addLayout(self.harmonieLayout, 2, 0, 1, 1)
        
        
        self._createMenuBar(MainWindow)
        #bouton radio couleur
        self.createRadioButton()


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        #Bouton reset
        self.retourButton = QtWidgets.QPushButton(self.centralwidget)
        self.retourButton.setObjectName("Retour")
        self.horizontalLayout_2.addWidget(self.retourButton)

        #Bouton analogue
        self.AnalogueButton = QtWidgets.QPushButton(self.centralwidget)
        self.AnalogueButton.setObjectName("Analogue")
        self.harmonieLayout.addWidget(self.AnalogueButton)


        #Bouton Complementaire
        self.ComplementaireButton = QtWidgets.QPushButton(self.centralwidget)
        self.ComplementaireButton.setObjectName("Complementaire")
        self.harmonieLayout.addWidget(self.ComplementaireButton)
        #Bouton ComplementaireAdjacente
        self.ComplAdjButton = QtWidgets.QPushButton(self.centralwidget)
        self.ComplAdjButton.setObjectName("ComplAdj")
        self.harmonieLayout.addWidget(self.ComplAdjButton)
        #Bouton MonoButton
        self.MonoButton = QtWidgets.QPushButton(self.centralwidget)
        self.MonoButton.setObjectName("ComplAdj")
        self.harmonieLayout.addWidget(self.MonoButton)
                #Bouton triadique
        self.triadiqueButton = QtWidgets.QPushButton(self.centralwidget)
        self.triadiqueButton.setObjectName("ComplAdj")
        self.harmonieLayout.addWidget(self.triadiqueButton)
                #Bouton MonoButton
        self.DoubleComplButton = QtWidgets.QPushButton(self.centralwidget)
        self.DoubleComplButton.setObjectName("ComplAdj")
        self.harmonieLayout.addWidget(self.DoubleComplButton)



        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)
        self.horizontalSlider.valueChanged['int'].connect(self.analogue_value)
        self.horizontalSlider2.valueChanged['int'].connect(self.adjacente_value)
        #self.pushButton_2.clicked.connect(self.loadImage)
        #self.pushButton.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Added code here
        self.filename = None # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value
        self.analogue_value_now = 10 # Updated analogue value
        self.adjacente_value_now = 10 # Updated adjacente value


    def connectButton(self):
                #connection bouton
        self.retourButton.clicked.connect(self.resetImg)
        self.AnalogueButton.clicked.connect(self.LaunchAnalogue)
        self.ComplementaireButton.clicked.connect(self.LaunchComplementaire)
        self.ComplAdjButton.clicked.connect(self.LaunchComplAdjacente)
        self.MonoButton.clicked.connect(self.launchMonochromatique)
        self.triadiqueButton.clicked.connect(self.launchTriadique)
        self.DoubleComplButton.clicked.connect(self.launchDoubleCompl)


    def createRadioButton(self):
        self.colorAutoBtn = QRadioButton('Couleur Auto')
        self.pipetteBtn = QRadioButton('Pipette')

        self.colorAutoBtn.toggled.connect(self.onClickAutoColor)
        self.pipetteBtn.clicked.connect(self.onClickPipette)

        #layout.addWidget(self.rbtn1)
        #layout.addWidget(self.rbtn2)
        self.horizontalLayout_2.addWidget(self.colorAutoBtn)
        self.horizontalLayout_2.addWidget(self.pipetteBtn)
        self.colorAutoBtn.setChecked(True) 


    def _createMenuBar(self, MainWindow):
        menuBar = MainWindow.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", MainWindow)
        menuBar.addMenu(fileMenu)
        MainWindow.openAction = QAction("&Open...", MainWindow)
        MainWindow.saveAction = QAction("&Save", MainWindow)
        fileMenu.addAction(MainWindow.saveAction)
        fileMenu.addAction(MainWindow.openAction)

        MainWindow.openAction.triggered.connect(self.loadImage)
        MainWindow.saveAction.triggered.connect(self.savePhoto)

        # Creating menus using a title
        #editMenu = menuBar.addMenu("&Edit")
        #helpMenu = menuBar.addMenu("&Help")


    def hex_to_hsv(self,value):
        value = value.lstrip('#')
        lv = len(value)
        a = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        a = colorsys.rgb_to_hsv(a[0],a[1],a[2])
        b = a[0]*360/2, a[1]*255, a[2]
 
        return b

    def onClickAutoColor(self):
        if self.colorAutoBtn.isChecked() and self.loaded:
            self.pretraitement()
    def onClickPipette(self):
        if self.pipetteBtn.isChecked() and self.loaded:
        
            # opening color dialog
            color = QColorDialog.getColor()
            a=self.hex_to_hsv(color.name())
            print(a)
            self.histoHSV ={}
            self.histoHSV[a[0]] =50000
            return a



    def loadImage(self):
        """ This function will load the user selected image
            and set it to label using the setPhoto function
        """
       
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        if self.filename != "":
            self.loaded = True
            self.connectButton()
            self.image = cv2.imread(self.filename)
            self.lastImage = cv2.imread(self.filename)
            self.pretraitement()
            self.setPhoto(self.image)
    def setPhoto(self,image):
        """ This function will take image input and resize it 
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def addVignette(self, vignette):
        self.tmp = vignette
        vignette = imutils.resize(vignette,width=100)
        frame = cv2.cvtColor(vignette, cv2.COLOR_BGR2RGB)
        vignette = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.vignetteLabel.setPixmap(QtGui.QPixmap.fromImage(vignette))

    def brightness_value(self,value):
        """ This function will take value from the slider
            for the brightness from 0 to 99
        """
        self.brightness_value_now = value
        print('Brightness: ',value)
        self.update()
        
        
    def blur_value(self,value):
        """ This function will take value from the slider 
            for the blur from 0 to 99 """
        self.blur_value_now = value
        print('Blur: ',value)
        self.update()

    def analogue_value(self,value):
        self.analogue_value_now = value
        print('équart analogue: ',value)
        if(self.loaded):
            self.LaunchAdjacente()

    def adjacente_value(self,value):
        self.adjacente_value_now = value
        print('équart adjacente: ',value)
        if(self.loaded):
            self.LaunchComplAdjacente()
    
    
    def changeBrightness(self,img,value):
        """ This function will take an image (img) and the brightness
            value. It will perform the brightness change using OpenCv
            and after split, will merge the img and return it.
        """
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
        
    def changeBlur(self,img,value):
        """ This function will take the img image and blur values as inputs.
            After perform blur operation using opencv function, it returns 
            the image img.
        """
        kernel_size = (value+1,value+1) # +1 is to avoid 0
        img = cv2.blur(img,kernel_size)
        return img

    def changeAnalogue(self,img,value):
        img = cv2.analogue_converge(img,value)
        return img

    def changeAdjacent(self,img,value):
        img = cv2.complAdjacente_converge(img,value)
        return img
    
    def update(self):
        """ This function will update the photo according to the 
            current values of blur and brightness and set it to photo label.
        """
        if(self.loaded):
            img = self.changeBrightness(self.image,self.brightness_value_now)
            img = self.changeBlur(img,self.blur_value_now)
            self.setPhoto(img)
    
    def savePhoto(self):
        """ This function will save the image"""
        # here provide the output file name
        # lets say we want to save the output as a time stamp
        # uncomment the two lines below
        
        # import time
        # filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        
        # Or we can give any name such as output.jpg or output.png as well
        # filename = 'Snapshot.png'    
    
        # Or a much better option is to let user decide the location and the extension
              # using a file dialog.
        
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        
        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',self.filename)
    

    def resetImg(self):
        self.resetColorButton()
        self.image = self.lastImage
        self.setPhoto(self.image)
   
    def pretraitement(self):
        self.histoHSV = getHistoHSV(self.lastImage)
        #self.histoHSV ={}
        #self.histoHSV[100] =50000


    def LaunchAnalogue(self):
        self.resetColorButton()
        self.horizontalSlider.setEnabled(True)
        self.TexteLiderAnalogue.setStyleSheet("QLabel { color : black; }")
        self.AnalogueButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonieAnalogue(self.histoHSV, self.hsvImage, self.analogue_value_now, False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("analogue finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)
        
    def LaunchComplementaire(self):
        self.resetColorButton()
        self.ComplementaireButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonieCompl(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("Complementaire finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)
        
    def LaunchComplAdjacente(self): 
        self.resetColorButton()
        self.ComplAdjButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")     
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonieComplAdj(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("Complementaire adjacente finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)

    def launchMonochromatique(self):
        self.resetColorButton()
        self.MonoButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonieMono(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("monochromatique finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)

    def launchDoubleCompl(self):
        self.resetColorButton()
        self.DoubleComplButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonieDoubleCompl(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("DoubleCompl finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)

    def launchTriadique(self):
        self.resetColorButton()
        self.triadiqueButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}")
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)
        self.hsvImage, self.vignette = findBestHarmonietriadique(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("triadique finish")
        self.setPhoto(self.image)
        self.addVignette(self.vignette)


    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyshine photo editor"))
      #  self.pushButton_2.setText(_translate("MainWindow", "Open"))
       # self.pushButton.setText(_translate("MainWindow", "Save"))

        self.retourButton.setText(_translate("MainWindow", "Retour"))
        self.AnalogueButton.setText(_translate("MainWindow", "Analogue"))
        self.ComplementaireButton.setText(_translate("MainWindow", "Complémentaire"))
        self.ComplAdjButton.setText(_translate("MainWindow", "Complémentaire Adjacente"))
        self.MonoButton.setText(_translate("MainWindow", "Monochromatique"))
        self.triadiqueButton.setText(_translate("MainWindow", "Triadique"))
        self.DoubleComplButton.setText(_translate("MainWindow", "Double Complementaire"))


    def resetColorButton(self):
        self.AnalogueButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.ComplementaireButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.ComplementaireButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.ComplAdjButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.MonoButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.triadiqueButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.DoubleComplButton.setStyleSheet("QPushButton"
                    "{"
                    "background-color : white;"
                    "}")
        self.hideSlider()
    def hideSlider(self):
         self.horizontalSlider.setEnabled(False)
         self.TexteLiderAnalogue.setStyleSheet("QLabel { color : grey; }")


# Subscribe to PyShine Youtube channel for more detail! 

# WEBSITE: www.pyshine.com


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
