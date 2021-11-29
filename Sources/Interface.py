# -*- coding: utf-8 -*-
import cv2
import random
import math
from imgTools import *
import string, os 
from analogue_converge import *
from complementaire_converge import *


verbose = True




#import numpy
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import QMainWindow, QApplication












from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMenuBar, QMenu, QAction
from PyQt5.QtGui import QImage

import imutils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        
        #self.statusBar()
        self._createMenuBar(MainWindow)




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
        self.ComplementaireButton.setObjectName("Analogue")
        self.harmonieLayout.addWidget(self.ComplementaireButton)

        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)
        #self.pushButton_2.clicked.connect(self.loadImage)
        #self.pushButton.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connection bouton
        self.retourButton.clicked.connect(self.resetImg)
        self.AnalogueButton.clicked.connect(self.LaunchAnalogue)
        self.ComplementaireButton.clicked.connect(self.LaunchComplementaire)
        # Added code here
        self.filename = None # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value

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

    def loadImage(self):
        """ This function will load the user selected image
            and set it to label using the setPhoto function
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
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
    
    def update(self):
        """ This function will update the photo according to the 
            current values of blur and brightness and set it to photo label.
        """
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
        self.image = self.lastImage
        self.setPhoto(self.image)
   
    def pretraitement(self):
        self.histoHSV = getHistoHSV(self.lastImage)
        #self.histoHSV ={}
        #self.histoHSV[100] =50000
        self.hsvImage = cv2.cvtColor(self.lastImage, cv2.COLOR_BGR2HSV)

    def LaunchAnalogue(self):
        findBestHarmonieAnalogue(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("analogue finish")
        self.setPhoto(self.image)
        
    def LaunchComplementaire(self):
        findBestHarmonieCompl(self.histoHSV, self.hsvImage,False)
        self.image = cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
        print("Complementaire finish")
        self.setPhoto(self.image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyshine photo editor"))
      #  self.pushButton_2.setText(_translate("MainWindow", "Open"))
       # self.pushButton.setText(_translate("MainWindow", "Save"))

        self.retourButton.setText(_translate("MainWindow", "Retour"))
        self.AnalogueButton.setText(_translate("MainWindow", "Analogue"))
        self.ComplementaireButton.setText(_translate("MainWindow", "Complementaire"))


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
