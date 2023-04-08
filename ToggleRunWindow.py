# Form implementation generated from reading ui file 'ToggleRun.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest
import multiprocessing
import time
import httpimport
import pickle

from thread_workers import *

toggle_process = None
window = None
app = None
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
        global toggle_process
        while toggle_process.is_alive():
            time.sleep(0.1)
        self.signal.finished.emit()


def stop_toggle():
    global toggle_process
    if toggle_process is not None and toggle_process.is_alive():
        toggle_process.terminate()


class Ui_ToggleRun(object):

    def __init__(self, x, y):
        global app, window_position
        app = x
        window_position = y

    def setupUi(self, ToggleRunWindow):
        global window, window_position
        ToggleRunWindow.setFixedSize(800, 600)
        ToggleRunWindow.setWindowTitle("PokemonUI")
        ToggleRunWindow.setStyleSheet("background-color: black;")
        if window_position is not None:
            ToggleRunWindow.move(window_position)
        window = ToggleRunWindow
        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(set_window_icon_from_response)
        self.nam.get(QNetworkRequest(QUrl("https://raw.githubusercontent.com/"
                                          "T3tsuo/PokemonUI/main/cache/poke.ico")))
        self.centralwidget = QtWidgets.QWidget(parent=ToggleRunWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setText("Toggle Run")
        self.title.adjustSize()
        self.title.move(ToggleRunWindow.width() // 2 - self.title.width() // 2,
                        ToggleRunWindow.height() // 4 - self.title.height())
        self.start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button.setStyleSheet("color: black; background-color: grey;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setGeometry(QtCore.QRect(ToggleRunWindow.width() // 2 - 60,
                                                   ToggleRunWindow.height() // 2 - 45 // 2, 120, 45))
        self.start_button.setText("Start")
        self.stop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_button.setStyleSheet("color: black; background-color: grey;")
        self.stop_button.setFont(font)
        self.stop_button.setGeometry(QtCore.QRect(ToggleRunWindow.width() // 2 - 60,
                                                  ToggleRunWindow.height() // 2 - 45 // 2, 120, 45))
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
        self.is_running.move(ToggleRunWindow.width() // 2 - self.is_running.width() // 2,
                             ToggleRunWindow.height() * 2 // 5 - self.is_running.height())
        ToggleRunWindow.setCentralWidget(self.centralwidget)
        self.threadpool = QThreadPool()

        self.start_button.clicked.connect(self.run_toggle)
        self.start_button.setAutoDefault(True)

        self.stop_button.clicked.connect(stop_toggle)
        self.stop_button.setAutoDefault(True)

        self.backBtn.setShortcut("Esc")
        self.backBtn.clicked.connect(self.open_PokemonUI)
        self.backBtn.clicked.connect(stop_toggle)
        self.backBtn.clicked.connect(ToggleRunWindow.close)
        self.backBtn.setAutoDefault(True)

        app.aboutToQuit.connect(closeEvent)

        QtCore.QMetaObject.connectSlotsByName(ToggleRunWindow)

    def run_toggle(self):
        global toggle_process, window
        toggle_process = multiprocessing.Process(target=run_script)
        toggle_process.daemon = True
        toggle_process.start()

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


def run_script():
    with httpimport.github_repo(username='T3tsuo', repo='LevelFarming', ref='main'):
        import ToggleRun
    ToggleRun.run()
