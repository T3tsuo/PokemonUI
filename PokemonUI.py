# Form implementation generated from reading ui file 'PokemonUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PokemonUI(object):
    def setupUi(self, PokemonUI):
        PokemonUI.setObjectName("PokemonUI")
        PokemonUI.setFixedSize(800, 600)
        PokemonUI.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=PokemonUI)
        self.centralwidget.setObjectName("centralwidget")
        self.everstoneFarming = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.everstoneFarming.setText("EverstoneFarming")
        self.everstoneFarming.setStyleSheet("color: black; background-color: grey;")
        self.everstoneFarming.setFont(font)
        self.everstoneFarming.setGeometry(QtCore.QRect(PokemonUI.width() // 2 - 140 // 2,
                                                       PokemonUI.height() // 4 - 50 // 2, 140, 50))
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

        self.retranslateUi(PokemonUI)
        QtCore.QMetaObject.connectSlotsByName(PokemonUI)

        self.everstoneFarming.clicked.connect(self.load_everstone_farming_window)
        self.everstoneFarming.clicked.connect(PokemonUI.close)


    def retranslateUi(self, PokemonUI):
        _translate = QtCore.QCoreApplication.translate
        PokemonUI.setWindowTitle(_translate("PokemonUI", "PokemonUI"))


    def load_everstone_farming_window(self):
        self.window = QtWidgets.QMainWindow()
        from EverstoneFarmingWindow import Ui_EverstoneFarming
        ui = Ui_EverstoneFarming()
        ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PokemonUI = QtWidgets.QMainWindow()
    ui = Ui_PokemonUI()
    ui.setupUi(PokemonUI)
    PokemonUI.show()
    sys.exit(app.exec())
