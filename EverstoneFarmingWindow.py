# Form implementation generated from reading ui file 'EverstoneFarming.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import httpimport
import multiprocessing
from PyQt6 import QtCore, QtGui, QtWidgets
import time

from thread_workers import *

everstone_process = None
window = None


class CheckProcess(QRunnable):
    signal = WorkerSignal()

    @pyqtSlot()
    def run(self):
        global everstone_process
        while everstone_process.is_alive():
            time.sleep(0.1)
        self.signal.finished.emit()


class Ui_EverstoneFarming(object):
    def setupUi(self, EverstoneFarmingWindow):
        global window
        EverstoneFarmingWindow.setObjectName("MainWindow")
        EverstoneFarmingWindow.setFixedSize(800, 600)
        EverstoneFarmingWindow.setStyleSheet("background-color: black;")
        EverstoneFarmingWindow.setWindowTitle("PokemonUI")
        window = EverstoneFarmingWindow
        self.centralwidget = QtWidgets.QWidget(parent=EverstoneFarmingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setStyleSheet("color: #cccccc;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setText("Everstone Farming")
        self.title.adjustSize()
        self.title.move(EverstoneFarmingWindow.width() // 2 - self.title.width() // 2,
                        EverstoneFarmingWindow.height() // 4 - self.title.height())
        self.sweetScentInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.sweetScentInput.setFont(font)
        self.sweetScentInput.setStyleSheet("background-color: white;")
        self.sweetScentInput.setGeometry(QtCore.QRect(EverstoneFarmingWindow.width() // 2 - 170,
                                                      EverstoneFarmingWindow.height() // 2 - 20, 170, 40))
        self.sweetScentInput.setObjectName("sweetScentInput")
        self.sweetScentInput.setPlaceholderText("How many sweet scents")
        self.timeInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.timeInput.setFont(font)
        self.timeInput.setStyleSheet("background-color: white;")
        self.timeInput.setGeometry(QtCore.QRect(EverstoneFarmingWindow.width() // 2,
                                                EverstoneFarmingWindow.height() // 2 - 20, 170, 40))
        self.timeInput.setObjectName("timeInput")
        self.timeInput.setPlaceholderText("Duration length of script")
        self.start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_button.setStyleSheet("color: black; background-color: grey;")
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setGeometry(QtCore.QRect(EverstoneFarmingWindow.width() // 2 - 60,
                                                   EverstoneFarmingWindow.height() * 3 // 4 - 45 // 2, 120, 45))
        self.start_button.setText("Start")
        self.stop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_button.setStyleSheet("color: black; background-color: grey;")
        self.stop_button.setFont(font)
        self.stop_button.setGeometry(QtCore.QRect(EverstoneFarmingWindow.width() // 2 - 60,
                                                  EverstoneFarmingWindow.height() * 3 // 4 - 45 // 2, 120, 45))
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
        font.setPointSize(18)
        self.is_running.setFont(font)
        self.is_running.hide()
        self.is_running.adjustSize()
        self.is_running.move(EverstoneFarmingWindow.width() // 2 - self.is_running.width() // 2,
                             EverstoneFarmingWindow.height() * 2 // 3 - self.is_running.height())
        EverstoneFarmingWindow.setCentralWidget(self.centralwidget)
        self.threadpool = QThreadPool()

        self.sweetScentInput.returnPressed.connect(self.run_everstone_farming)
        self.timeInput.returnPressed.connect(self.run_everstone_farming)

        self.start_button.clicked.connect(self.run_everstone_farming)
        self.start_button.setAutoDefault(True)

        self.stop_button.clicked.connect(self.stop_everstone_farming)
        self.stop_button.setAutoDefault(True)

        self.backBtn.setShortcut("Esc")
        self.backBtn.clicked.connect(self.open_PokemonUI)
        self.backBtn.clicked.connect(self.stop_everstone_farming)
        self.backBtn.clicked.connect(EverstoneFarmingWindow.close)
        self.backBtn.setAutoDefault(True)

        QtCore.QMetaObject.connectSlotsByName(EverstoneFarmingWindow)


    def run_everstone_farming(self):
        global everstone_process, window
        if self.sweetScentInput.text() != "" and self.timeInput.text() != "":
            everstone_process = multiprocessing.Process(target=run_script,
                                                        args=[self.sweetScentInput.text(), self.timeInput.text()])
            everstone_process.daemon = True
            everstone_process.start()

            is_alive_worker = CheckProcess()
            is_alive_worker.signal.finished.connect(self.hide_status)
            self.threadpool.start(is_alive_worker)

            self.start_button.hide()
            self.stop_button.show()
            self.is_running.setText("Running...")
            self.is_running.adjustSize()
            self.is_running.move(window.width() // 2 - self.is_running.width() // 2,
                                 window.height() * 2 // 3 - self.is_running.height())
            self.is_running.show()

    def stop_everstone_farming(self):
        global everstone_process
        if everstone_process is not None and everstone_process.is_alive():
            everstone_process.terminate()

    def hide_status(self):
        self.is_running.hide()
        self.stop_button.hide()
        self.start_button.show()

    def open_PokemonUI(self):
        self.temp_window = QtWidgets.QMainWindow()
        from PokemonUI import Ui_PokemonUI
        self.ui = Ui_PokemonUI()
        self.ui.setupUi(self.temp_window)
        self.temp_window.show()


def run_script(n, t):
    with httpimport.github_repo(username='T3tsuo', repo='EverstoneFarming', ref='main'):
        import EverstoneFarming
    EverstoneFarming.run(n, t)
