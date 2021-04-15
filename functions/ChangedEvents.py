import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

def zoomChanged(ui,variables):
    variables.zoom = float(ui.line_zoom.text())

def locationChanged(ui,variables):
    variables.location = ui.line_location.text()
    isDirectory = os.path.isdir(variables.location)
    if isDirectory:
        dosyalar = os.listdir(variables.location)
        for i in dosyalar:
            if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):
                ui.lbl_image.setStyleSheet("background-image:url('Icons/correct.png');background-repeat:no-repeat;")
                ui.lbl_text.setText("Dosyada foto var")
                break
            else:
                ui.lbl_image.setStyleSheet("background-image:url('Icons/error.png');background-repeat:no-repeat;")
                ui.lbl_text.setText("Dosyada foto yok")


def countChanged(ui,variables):
    variables.count = int(ui.line_count.text())

def brightnessChanged(ui,variables):
    if ui.line_brightness.text() != "":

        variables.brightness = int(ui.line_brightness.text())
    print(variables.brightness)