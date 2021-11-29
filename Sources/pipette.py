# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import cv2
import colorsys
from imgTools import *

class Window(QMainWindow):

    def hex_to_hsv(self,value):
        value = value.lstrip('#')
        lv = len(value)
        a = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        a = colorsys.rgb_to_hsv(a[0],a[1],a[2])
        b = a[0]*360/2, a[1]*255, a[2]
 
        return b


    def __init__(self):
        super().__init__()

        # calling method
        self.UiComponents()


    # method for components
    def UiComponents(self):

        # opening color dialog
        color = QColorDialog.getColor()
        a=self.hex_to_hsv(color.name())
        return a



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
