

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtCore import *

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self):
        os.chdir("./design")
        super().__init__()
        self.resize(684, 253)

        self.setStyleSheet(open("style.qss", "r").read())

        self.btn_rotate = QtWidgets.QPushButton(self)
        self.btn_rotate.setGeometry(QtCore.QRect(230, 160, 211, 61))
        self.btn_rotate.setText("  Image Rotate")
        icon = QtGui.QIcon("../Icons/rotate.png")
        self.btn_rotate.setIcon(icon)
        self.btn_rotate.setIconSize(QSize(30,25))


        self.btn_brightness = QtWidgets.QPushButton(self)
        self.btn_brightness.setGeometry(QtCore.QRect(20, 160, 201, 61))
        self.btn_brightness.setText("Brightness")
        icon = QtGui.QIcon("../Icons/brightness.png")
        self.btn_brightness.setIcon(icon)
        self.btn_brightness.setIconSize(QSize(30,25))

        self.btn_zooming = QtWidgets.QPushButton(self)
        self.btn_zooming.setGeometry(QtCore.QRect(450, 160, 201, 61))
        self.btn_zooming.setText("Image Zooming")
        icon = QtGui.QIcon("../Icons/zoom.png")
        self.btn_zooming.setIcon(icon)
        self.btn_zooming.setIconSize(QSize(30,25))



        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(90, 20, 231, 61))
        self.groupBox.setTitle("Location")

        self.line_location = QtWidgets.QLineEdit(self.groupBox)
        self.line_location.setGeometry(QtCore.QRect(10, 20, 211, 31))

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 20, 221, 61))
        self.groupBox_2.setTitle("Count")

        self.line_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_count.setGeometry(QtCore.QRect(10, 20, 201, 31))

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 221, 61))
        self.groupBox_3.setTitle("Brightness")

        self.line_brightness = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_brightness.setGeometry(QtCore.QRect(10, 20, 201, 31))

        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 90, 221, 61))
        self.groupBox_4.setTitle("Zoom Value")

        self.line_zoom = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_zoom.setGeometry(QtCore.QRect(10, 20, 201, 31))

        self.lbl_text = QtWidgets.QLabel(self)
        self.lbl_text.setGeometry(QtCore.QRect(260, 100, 91, 51))
        self.lbl_text.setText("Location is NULL")

        self.lbl_image = QtWidgets.QLabel(self)
        self.lbl_image.setGeometry(QtCore.QRect(350, 100, 91, 51))
        self.lbl_image.setStyleSheet("background-color:Red;")


        #CHANGED EVENTS



        #self.btn_dosyaSec.setIcon(QtGui.QIcon("../icons/fileGri.png"))


        self.show()
        os.chdir("..")




