# Form implementation generated from reading ui file 'pokemon.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
import multiprocessing, time, os
from PyQt6.QtCore import QRunnable, pyqtSlot, QThreadPool
from git import Repo

from thread_workers import WorkerSignal

pokemon_process = None
window = None
is_run = False
uis = {}

log_data = ""


class CheckProcess(QRunnable):
    signal = WorkerSignal()

    @pyqtSlot()
    def run(self):
        global pokemon_process, is_run
        while pokemon_process.is_alive() and is_run:
            self.signal.update_log.emit()
            time.sleep(0.1)
        if is_run:
            self.signal.finished.emit()


class Ui_PokemonUI(object):
    def setupUi(self, PokemonUI, dict):
        global window, uis
        uis = dict
        window = PokemonUI
        PokemonUI.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setPointSize(16)
        PokemonUI.setFont(font)
        PokemonUI.setStyleSheet("*{\n"
                                "    border: none;\n"
                                "    background-color: transparent;\n"
                                "    background: none;\n"
                                "    padding: 0;\n"
                                "    margin: 0;\n"
                                "    color: #fff;\n"
                                "}\n"
                                "#centralwidget{\n"
                                "    background-color: #1f232a;\n"
                                "}\n"
                                "#featurecontainer{\n"
                                "    background-color: #16191d;\n"
                                "}\n"
                                "#MainContainer{\n"
                                "    background-color: #16191d;\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(parent=PokemonUI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.featurecontainer = QtWidgets.QWidget(parent=self.centralwidget)
        self.featurecontainer.setObjectName("featurecontainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.featurecontainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.configsubcontainer = QtWidgets.QWidget(parent=self.featurecontainer)
        self.configsubcontainer.setStyleSheet("QPushButton{\n"
                                              "    padding: 2px, 5px;\n"
                                              "}")
        self.configsubcontainer.setObjectName("configsubcontainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.configsubcontainer)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.homeBtn = QtWidgets.QPushButton(parent=self.configsubcontainer)
        self.homeBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feather/feather/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeBtn.setIcon(QtGui.QIcon('feather/home.svg'))
        self.homeBtn.setIconSize(QtCore.QSize(30, 30))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_4.addWidget(self.homeBtn)
        self.settingsBtn = QtWidgets.QPushButton(parent=self.configsubcontainer)
        self.settingsBtn.setText("")
        self.settingsBtn.setIcon(QtGui.QIcon('feather/settings.svg'))
        self.settingsBtn.setIconSize(QtCore.QSize(30, 30))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.verticalLayout.addWidget(self.configsubcontainer, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scriptscontainer = QtWidgets.QWidget(parent=self.featurecontainer)
        self.scriptscontainer.setStyleSheet("QPushButton{\n"
                                            "    text-align: left;\n"
                                            "    font-size: 18px;\n"
                                            "    padding: 2px, 5px;\n"
                                            "}")
        self.scriptscontainer.setObjectName("scriptscontainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scriptscontainer)
        self.verticalLayout_3.setContentsMargins(5, 0, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.breedBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.breedBtn.setObjectName("breedBtn")
        self.breedBtn.setText("Breed")
        self.verticalLayout_3.addWidget(self.breedBtn)
        self.itemBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.itemBtn.setObjectName("itemBtn")
        self.verticalLayout_3.addWidget(self.itemBtn)
        self.levelBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.levelBtn.setObjectName("levelBtn")
        self.verticalLayout_3.addWidget(self.levelBtn)
        self.plantingBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.plantingBtn.setObjectName("plantingBtn")
        self.verticalLayout_3.addWidget(self.plantingBtn)
        self.pokemonBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.pokemonBtn.setObjectName("pokemonBtn")
        self.verticalLayout_3.addWidget(self.pokemonBtn)
        self.verticalLayout.addWidget(self.scriptscontainer)
        self.horizontalLayout.addWidget(self.featurecontainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.MainContainer = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainContainer.sizePolicy().hasHeightForWidth())
        self.MainContainer.setSizePolicy(sizePolicy)
        self.MainContainer.setObjectName("MainContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainSubContainer = QtWidgets.QWidget(parent=self.MainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.MainSubContainer.sizePolicy().hasHeightForWidth())
        self.MainSubContainer.setSizePolicy(sizePolicy)
        self.MainSubContainer.setObjectName("MainSubContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.MainSubContainer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.containertitlecombo = QtWidgets.QWidget(parent=self.MainSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.containertitlecombo.sizePolicy().hasHeightForWidth())
        self.containertitlecombo.setSizePolicy(sizePolicy)
        self.containertitlecombo.setObjectName("containertitlecombo")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.containertitlecombo)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.title = QtWidgets.QLabel(parent=self.containertitlecombo)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout_7.addWidget(self.title)
        self.verticalLayout_6.addWidget(self.containertitlecombo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.subconfigitem = QtWidgets.QWidget(parent=self.MainSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.subconfigitem.sizePolicy().hasHeightForWidth())
        self.subconfigitem.setSizePolicy(sizePolicy)
        self.subconfigitem.setObjectName("subconfigitem")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.subconfigitem)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pokecombo = QtWidgets.QComboBox(parent=self.subconfigitem)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pokecombo.setFont(font)
        self.pokecombo.setStyleSheet("background-color: transparent; color: white; margin: 10px;")
        self.pokecombo.setObjectName("pokecombo")
        self.pokecombo.setPlaceholderText("")
        self.pokecombo.addItem("--")
        self.pokecombo.addItem("Ditto")
        self.verticalLayout_8.addWidget(self.pokecombo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.duskballs = QtWidgets.QTextEdit(parent=self.subconfigitem)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.duskballs.setFont(font)
        self.duskballs.setStyleSheet("background-color: transparent; border: 1px solid white;")
        self.duskballs.setObjectName("duskballs")
        self.verticalLayout_8.addWidget(self.duskballs)
        self.verticalLayout_6.addWidget(self.subconfigitem, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.buttonscontainer = QtWidgets.QWidget(parent=self.MainSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttonscontainer.sizePolicy().hasHeightForWidth())
        self.buttonscontainer.setSizePolicy(sizePolicy)
        self.buttonscontainer.setStyleSheet("QPushButton{\n"
                                            "    font-size: 18px;\n"
                                            "    padding: 2px, 5px;\n"
                                            "}")
        self.buttonscontainer.setObjectName("buttonscontainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.buttonscontainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.runBtn = QtWidgets.QPushButton(parent=self.buttonscontainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.runBtn.setFont(font)
        self.runBtn.setStyleSheet("padding: 10px 25px 10px 25px; border: 1px solid white;")
        self.runBtn.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.runBtn)
        self.verticalLayout_6.addWidget(self.buttonscontainer, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.MainSubContainer)
        self.LogSubContainer = QtWidgets.QWidget(parent=self.MainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.LogSubContainer.sizePolicy().hasHeightForWidth())
        self.LogSubContainer.setSizePolicy(sizePolicy)
        self.LogSubContainer.setObjectName("LogSubContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.LogSubContainer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logtitle = QtWidgets.QLabel(parent=self.LogSubContainer)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logtitle.setFont(font)
        self.logtitle.setObjectName("logtitle")
        self.verticalLayout_5.addWidget(self.logtitle, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollLog = QtWidgets.QScrollArea(parent=self.LogSubContainer)
        self.scrollLog.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollLog.sizePolicy().hasHeightForWidth())
        self.scrollLog.setSizePolicy(sizePolicy)
        self.scrollLog.setStyleSheet("background-color: #2a3038;")
        self.scrollLog.setWidgetResizable(True)
        self.scrollLog.setObjectName("scrollLog")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 861, 187))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.logLabel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.logLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logLabel.setFont(font)
        self.logLabel.setObjectName("logLabel")
        self.verticalLayout_9.addWidget(self.logLabel)
        self.scrollLog.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollLog)
        self.verticalLayout_2.addWidget(self.LogSubContainer)
        self.horizontalLayout.addWidget(self.MainContainer)
        PokemonUI.setCentralWidget(self.centralwidget)

        self.threadpool = QThreadPool()

        self.homeBtn.clicked.connect(self.hide_status)
        self.homeBtn.clicked.connect(lambda: open_ui("home"))

        self.settingsBtn.clicked.connect(self.hide_status)
        self.settingsBtn.clicked.connect(lambda: open_ui("settings"))

        self.breedBtn.clicked.connect(self.hide_status)
        self.breedBtn.clicked.connect(lambda: open_ui("breed"))

        self.itemBtn.clicked.connect(self.hide_status)
        self.itemBtn.clicked.connect(lambda: open_ui("item"))

        self.levelBtn.clicked.connect(self.hide_status)
        self.levelBtn.clicked.connect(lambda: open_ui("level"))

        self.plantingBtn.clicked.connect(self.hide_status)
        self.plantingBtn.clicked.connect(lambda: open_ui("plant"))

        self.runBtn.clicked.connect(self.run_pokemon_farming)
        self.runBtn.setAutoDefault(True)

        self.retranslateUi(PokemonUI)
        QtCore.QMetaObject.connectSlotsByName(PokemonUI)

    def update_log(self):
        global log_data
        if os.path.isfile("log.txt"):
            with open("log.txt", "r") as f_temp:
                data_temp = f_temp.read()
            # if data has been updated
            if data_temp != log_data:
                # update it
                log_data = data_temp
                # if there is a new line at the end then strip it
                if len(log_data) != 0 and log_data[len(log_data) - 1] == "\n":
                    log_data = log_data[:-1]
                # then set the log
                self.logLabel.setText(log_data)
                self.scrollLog.verticalScrollBar().setValue(self.scrollLog.verticalScrollBar().maximum())

    def run_pokemon_farming(self):
        global pokemon_process, window, is_run
        # if everything is entered correctly
        if self.duskballs.toPlainText() != "" and str(self.pokecombo.currentText()) != "--" and not is_run:
            # delete everything from the old log
            if os.path.isfile("log.txt"):
                os.remove("log.txt")
            is_run = True
            pokemon_process = multiprocessing.Process(target=run_script,
                                                   args=[self.duskballs.toPlainText(),
                                                         str(self.pokecombo.currentText())])
            pokemon_process.daemon = True
            pokemon_process.start()

            self.is_alive_worker = CheckProcess()
            # hide status once program is done
            self.is_alive_worker.signal.finished.connect(self.hide_status)
            # run update log on main thread
            self.is_alive_worker.signal.update_log.connect(self.update_log)
            self.threadpool.start(self.is_alive_worker)

            self.runBtn.setText("Stop")
        elif is_run and pokemon_process is not None and pokemon_process.is_alive():
            self.hide_status()

    def hide_status(self):
        global pokemon_process, is_run
        if is_run:
            is_run = False
            pokemon_process.terminate()
            self.runBtn.setText("Start")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PokemonUI"))
        self.itemBtn.setText(_translate("MainWindow", "Item"))
        self.pokemonBtn.setText(_translate("MainWindow", "Pokemon"))
        self.levelBtn.setText(_translate("MainWindow", "Level"))
        self.plantingBtn.setText(_translate("MainWindow", "Planting"))
        self.title.setText(_translate("MainWindow", "Poke Farming"))
        self.pokecombo.setItemText(0, _translate("MainWindow", "--"))
        self.duskballs.setPlaceholderText(_translate("MainWindow", "How many duskballs"))
        self.runBtn.setText(_translate("MainWindow", "Start"))
        self.logtitle.setText(_translate("MainWindow", "Logs"))


def open_ui(ui_name):
    global window, uis
    for p in multiprocessing.active_children():
        p.terminate()
    uis[ui_name].setupUi(window, uis)


def run_script(n, pokemon):
    if pokemon == "Ditto":
        # go to script folder to import main file and all dependencies
        sys.path.insert(0, "scripts/PokemonScripts/PokemonFarming/DittoFarm")
        import DittoFarm
        DittoFarm.run(n)
