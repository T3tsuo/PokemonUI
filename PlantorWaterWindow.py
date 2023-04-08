# Form implementation generated from reading ui file 'PlantorWater.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest
import time
import multiprocessing
import httpimport
import pickle

from thread_workers import *

plantorwater_process = None
window = None
app = None
place_mapping = {'Mistralton': 1, 'Abundant Shrine': 2}
interact_mapping = {'Water': 'water', 'Pickup and Plant': 'plant'}
window_position = None


def set_window_icon_from_response(http_response):
    global window
    pixmap = QPixmap()
    pixmap.loadFromData(http_response.readAll())
    icon = QIcon(pixmap)
    if window is not None:
        window.setWindowIcon(icon)


class CheckProcess(QRunnable):
    signal = WorkerSignal()

    @pyqtSlot()
    def run(self):
        global plantorwater_process
        while plantorwater_process.is_alive():
            time.sleep(0.1)
        self.signal.finished.emit()


def stop_plantorwater():
    global plantorwater_process
    if plantorwater_process is not None and plantorwater_process.is_alive():
        plantorwater_process.terminate()


class Ui_PlantorWaterWindow(object):

    def __init__(self, x, y):
        global app, window_position
        app = x
        window_position = y

    def setupUi(self, PlantorWaterWindow):
        global window, window_position
        PlantorWaterWindow.setObjectName("MainWindow")
        PlantorWaterWindow.setFixedSize(800, 600)
        PlantorWaterWindow.setStyleSheet("background-color: black;")
        PlantorWaterWindow.setWindowTitle("PokemonUI")
        if window_position is not None:
            PlantorWaterWindow.move(window_position)
        window = PlantorWaterWindow
        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(set_window_icon_from_response)
        self.nam.get(QNetworkRequest(QUrl("https://raw.githubusercontent.com/"
                                          "T3tsuo/PokemonUI/main/cache/poke.ico")))
        self.centralwidget = QtWidgets.QWidget(parent=PlantorWaterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setText("Plant or Water")
        self.title.adjustSize()
        self.title.move(PlantorWaterWindow.width() // 2 - self.title.width() // 2,
                        PlantorWaterWindow.height() // 4 - self.title.height())
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.place = QtWidgets.QComboBox(parent=self.centralwidget)
        self.place.setGeometry(QtCore.QRect(PlantorWaterWindow.width() // 2 - 170,
                                            PlantorWaterWindow.height() // 2 - 20, 170, 40))
        self.place.setStyleSheet("background-color: white;")
        self.place.addItem("--")
        self.place.addItem("Mistralton")
        self.place.addItem("Abundant Shrine")
        self.place.model().sort(0)
        self.place.setFont(font)
        self.interact = QtWidgets.QComboBox(parent=self.centralwidget)
        self.interact.setGeometry(QtCore.QRect(PlantorWaterWindow.width() // 2,
                                               PlantorWaterWindow.height() // 2 - 20, 170, 40))
        self.interact.setStyleSheet("background-color: white;")
        self.interact.addItem("--")
        self.interact.addItem("Water")
        self.interact.addItem("Pickup and Plant")
        self.interact.model().sort(0)
        self.interact.setFont(font)
        self.start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button.setStyleSheet("color: black; background-color: grey;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setGeometry(QtCore.QRect(PlantorWaterWindow.width() // 2 - 60,
                                                   PlantorWaterWindow.height() * 3 // 4 - 45 // 2, 120, 45))
        self.start_button.setText("Start")
        self.stop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_button.setStyleSheet("color: black; background-color: grey;")
        self.stop_button.setFont(font)
        self.stop_button.setGeometry(QtCore.QRect(PlantorWaterWindow.width() // 2 - 60,
                                                  PlantorWaterWindow.height() * 3 // 4 - 45 // 2, 120, 45))
        self.stop_button.setText("Stop")
        self.stop_button.hide()
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 70, 30))
        self.backBtn.setText("Esc")
        self.backBtn.setStyleSheet("color: black; background-color: grey;")
        self.backBtn.setFont(font)
        self.is_running = QtWidgets.QLabel(parent=self.centralwidget)
        self.is_running.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.is_running.setFont(font)
        self.is_running.hide()
        self.is_running.setText("Running...")
        self.is_running.adjustSize()
        self.is_running.move(PlantorWaterWindow.width() // 2 - self.is_running.width() // 2,
                             PlantorWaterWindow.height() * 2 // 3 - self.is_running.height())
        PlantorWaterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=PlantorWaterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PlantorWaterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=PlantorWaterWindow)
        self.statusbar.setObjectName("statusbar")
        PlantorWaterWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(PlantorWaterWindow)
        self.threadpool = QThreadPool()

        self.start_button.clicked.connect(self.run_plantorwater)
        self.start_button.setAutoDefault(True)

        self.stop_button.clicked.connect(stop_plantorwater)
        self.stop_button.setAutoDefault(True)

        self.backBtn.setShortcut("Esc")
        self.backBtn.clicked.connect(self.open_PokemonUI)
        self.backBtn.clicked.connect(stop_plantorwater)
        self.backBtn.clicked.connect(PlantorWaterWindow.close)
        self.backBtn.setAutoDefault(True)

        app.aboutToQuit.connect(closeEvent)

    def run_plantorwater(self):
        global plantorwater_process, window
        if str(self.place.currentText()) != "--" and str(self.interact.currentText()) != "--":
            plantorwater_process = multiprocessing.Process(target=run_script,
                                                           args=[place_mapping[str(self.place.currentText())],
                                                                 interact_mapping[str(self.interact.currentText())]])
            plantorwater_process.daemon = True
            plantorwater_process.start()

            is_alive_worker = CheckProcess()
            is_alive_worker.signal.finished.connect(self.hide_status)
            self.threadpool.start(is_alive_worker)

            self.start_button.hide()
            self.stop_button.show()
            self.is_running.show()

    def hide_status(self):
        self.is_running.hide()
        self.stop_button.hide()
        self.start_button.show()

    def open_PokemonUI(self):
        global app, window
        self.temp_window = QtWidgets.QMainWindow()
        from PokemonUI import Ui_PokemonUI
        self.ui = Ui_PokemonUI(app, window.pos())
        self.ui.setupUi(self.temp_window)
        self.temp_window.show()


def closeEvent():
    global window
    pickle.dump(window.pos(), open("window_position.dat", "wb"))
    for p in multiprocessing.active_children():
        p.terminate()


def run_script(place, interact):
    with httpimport.github_repo(username='T3tsuo', repo='PlantorWater', ref='main'):
        import PlantorWater
    PlantorWater.run(place, interact)
