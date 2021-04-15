from Veri_Coklama_Araci.design.tasarim import Ui_Form
from Veri_Coklama_Araci.variables.variables import vari
from Veri_Coklama_Araci.functions import functions,checking
from Veri_Coklama_Araci.functions.ChangedEvents import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":

        app = QtWidgets.QApplication(sys.argv)

        ui = Ui_Form()
        variables = vari()


        ui.setupUi()

        # CLİCKED EVENTS

        ui.btn_zooming.clicked.connect(lambda : checking.uygunsaKucultyadaBuyut(variables))
        ui.btn_brightness.clicked.connect(lambda: checking.uygunsaParlaklikDegis(variables))
        ui.btn_rotate.clicked.connect(lambda: checking.uygunsaDondur(variables))




        #CHANGED EVENTS
        ui.line_zoom.textChanged.connect(lambda : zoomChanged(ui,variables))
        ui.line_location.textChanged.connect(lambda : locationChanged(ui,variables))
        ui.line_count.textChanged.connect(lambda : countChanged(ui,variables))
        ui.line_brightness.textChanged.connect(lambda : brightnessChanged(ui,variables))

        sys.exit(app.exec_())


