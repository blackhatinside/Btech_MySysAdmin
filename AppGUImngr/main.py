from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie #to play gif files
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication

# import sys

Form, Window = uic.loadUiType("desktop.ui")

app = QApplication([])
# window.setFixedSize(1920,1080)


window = Window() #create a UI object
form = Form() #create a form
form.setupUi(window) #load UI to form
window.show() #display output in form

# sys.exit(app.exec())
app.exec()

#------------------------
# window2 = Window()
# form2 = Form()
# form2.setupUi(window2)
# window2.show()

