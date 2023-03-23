# Form implementation generated from reading ui file 'PokemonUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest
import multiprocessing
import os
import pickle

window = None
app = None

if os.path.isfile("window_position.dat"):
    window_position = pickle.load(open("window_position.dat", "rb"))
else:
    window_position = None


def set_window_icon_from_response(http_response):
    global window
    pixmap = QPixmap()
    pixmap.loadFromData(http_response.readAll())
    icon = QIcon(pixmap)
    if window is not None:
        window.setWindowIcon(icon)


class Ui_PokemonUI(object):

    def __init__(self, x, y):
        global app, window_position
        app = x
        window_position = y

    def setupUi(self, PokemonUI):
        global window, app, window_position
        PokemonUI.setObjectName("PokemonUI")
        PokemonUI.setFixedSize(800, 600)
        PokemonUI.setStyleSheet("background-color: black;")
        PokemonUI.setWindowTitle("PokemonUI")
        if window_position is not None:
            PokemonUI.move(window_position)
        window = PokemonUI
        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(set_window_icon_from_response)
        self.nam.get(QNetworkRequest(QUrl("https://raw.githubusercontent.com/"
                                          "T3tsuo/PokemonUI/main/cache/poke.ico")))
        self.centralwidget = QtWidgets.QWidget(parent=PokemonUI)
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setText("PokemonUI")
        self.title.adjustSize()
        self.title.move(PokemonUI.width() // 2 - self.title.width() // 2,
                        PokemonUI.height() // 4 - self.title.height())
        self.everstoneFarming = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.everstoneFarming.setText("EverstoneFarming")
        self.everstoneFarming.setStyleSheet("color: black; background-color: grey;")
        self.everstoneFarming.setFont(font)
        self.everstoneFarming.setGeometry(QtCore.QRect(PokemonUI.width() // 2 - 140 // 2,
                                                       PokemonUI.height() // 2 - 50 // 2, 140, 50))
        self.levelFarming = QtWidgets.QPushButton(parent=self.centralwidget)
        self.levelFarming.setText("LevelFarming")
        self.levelFarming.setStyleSheet("color: black; background-color: grey;")
        self.levelFarming.setFont(font)
        self.levelFarming.setGeometry(QtCore.QRect(PokemonUI.width() // 4 - 140 // 2,
                                                   PokemonUI.height() // 2 - 50 // 2, 140, 50))
        self.plantOrWater = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plantOrWater.setText("PlantorWater")
        self.plantOrWater.setStyleSheet("color: black; background-color: grey;")
        self.plantOrWater.setFont(font)
        self.plantOrWater.setGeometry(QtCore.QRect(PokemonUI.width() * 3 // 4 - 140 // 2,
                                                   PokemonUI.height() // 2 - 50 // 2, 140, 50))
        self.toggleRun = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toggleRun.setText("ToggleRun")
        self.toggleRun.setStyleSheet("color: black; background-color: grey;")
        self.toggleRun.setFont(font)
        self.toggleRun.setGeometry(QtCore.QRect(PokemonUI.width() // 2 - 140 // 2,
                                                PokemonUI.height() * 3 // 4 - 50 // 2, 140, 50))
        PokemonUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=PokemonUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PokemonUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=PokemonUI)
        self.statusbar.setObjectName("statusbar")
        PokemonUI.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(PokemonUI)

        self.everstoneFarming.clicked.connect(self.load_everstone_farming_window)
        self.everstoneFarming.clicked.connect(PokemonUI.close)
        self.everstoneFarming.setAutoDefault(True)
        self.plantOrWater.clicked.connect(self.load_plantorwater_window)
        self.plantOrWater.clicked.connect(PokemonUI.close)
        self.plantOrWater.setAutoDefault(True)
        self.levelFarming.clicked.connect(self.load_levelfarming_window)
        self.levelFarming.clicked.connect(PokemonUI.close)
        self.levelFarming.setAutoDefault(True)
        self.toggleRun.clicked.connect(self.load_togglerun_window)
        self.toggleRun.clicked.connect(PokemonUI.close)
        self.toggleRun.setAutoDefault(True)

        app.aboutToQuit.connect(closeEvent)

    def load_everstone_farming_window(self):
        global app, window
        self.window = QtWidgets.QMainWindow()
        from EverstoneFarmingWindow import Ui_EverstoneFarming
        self.ui = Ui_EverstoneFarming(app, window.pos())
        self.ui.setupUi(self.window)
        self.window.show()

    def load_plantorwater_window(self):
        global app, window
        self.window = QtWidgets.QMainWindow()
        from PlantorWaterWindow import Ui_PlantorWaterWindow
        self.ui = Ui_PlantorWaterWindow(app, window.pos())
        self.ui.setupUi(self.window)
        self.window.show()

    def load_levelfarming_window(self):
        global app, window
        self.window = QtWidgets.QMainWindow()
        from LevelFarmingWindow import Ui_LevelFarming
        self.ui = Ui_LevelFarming(app, window.pos())
        self.ui.setupUi(self.window)
        self.window.show()

    def load_togglerun_window(self):
        global app, window
        self.window = QtWidgets.QMainWindow()
        from ToggleRunWindow import Ui_ToggleRun
        self.ui = Ui_ToggleRun(app, window.pos())
        self.ui.setupUi(self.window)
        self.window.show()


def closeEvent():
    global window
    pickle.dump(window.pos(), open("window_position.dat", "wb"))
    for p in multiprocessing.active_children():
        p.terminate()


if __name__ == "__main__":
    import sys
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    PokemonUI = QtWidgets.QMainWindow()
    ui = Ui_PokemonUI(app, window_position)
    ui.setupUi(PokemonUI)
    PokemonUI.show()
    sys.exit(app.exec())
