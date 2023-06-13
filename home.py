# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import multiprocessing

window = None
uis = []


def open_item_ui():
    global window, uis
    for p in multiprocessing.active_children():
        p.terminate()
    uis[1].setupUi(window, uis)


def open_pokemon_ui():
    global window, uis
    for p in multiprocessing.active_children():
        p.terminate()
    uis[2].setupUi(window, uis)


class Ui_HomeUI(object):
    def setupUi(self, HomeUI, list):
        global window, uis
        uis = list
        window = HomeUI
        HomeUI.setObjectName("MainWindow")
        HomeUI.setWindowTitle("PokemonUI")
        HomeUI.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=HomeUI)
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
        self.itemBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.itemBtn.setObjectName("itemBtn")
        self.itemBtn.setText("Item")
        self.verticalLayout_3.addWidget(self.itemBtn)
        self.levelBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.levelBtn.setObjectName("levelBtn")
        self.levelBtn.setText("Level")
        self.verticalLayout_3.addWidget(self.levelBtn)
        self.plantingBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.plantingBtn.setObjectName("plantingBtn")
        self.plantingBtn.setText("Planting")
        self.verticalLayout_3.addWidget(self.plantingBtn)
        self.pokemonBtn = QtWidgets.QPushButton(parent=self.scriptscontainer)
        self.pokemonBtn.setObjectName("pokemonBtn")
        self.pokemonBtn.setText("Pokemon")
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MainSubContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # load home ui
        self.homecontainer = QtWidgets.QWidget(parent=self.MainSubContainer)
        self.homecontainer.setObjectName("homecontainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.homecontainer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.titlecontainer = QtWidgets.QWidget(parent=self.homecontainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.titlecontainer.sizePolicy().hasHeightForWidth())
        self.titlecontainer.setSizePolicy(sizePolicy)
        self.titlecontainer.setObjectName("titlecontainer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.titlecontainer)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.titlehome = QtWidgets.QLabel(parent=self.titlecontainer)
        self.titlehome.setText("PokemonUI")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlehome.sizePolicy().hasHeightForWidth())
        self.titlehome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titlehome.setFont(font)
        self.titlehome.setObjectName("titlehome")
        self.verticalLayout_7.addWidget(self.titlehome)
        self.verticalLayout_6.addWidget(self.titlecontainer, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.descriptionlabel = QtWidgets.QLabel(parent=self.homecontainer)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptionlabel.setFont(font)
        self.descriptionlabel.setText("Check out github for documentations on how to run the script")
        self.descriptionlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.descriptionlabel.setWordWrap(True)
        self.descriptionlabel.setObjectName("descriptionlabel")
        self.verticalLayout_6.addWidget(self.descriptionlabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.homecontainer)
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
        self.logtitle.setText("Logs")
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 861, 189))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollLog.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollLog)
        self.verticalLayout_2.addWidget(self.LogSubContainer)
        self.horizontalLayout.addWidget(self.MainContainer)
        HomeUI.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(HomeUI)

        self.itemBtn.clicked.connect(open_item_ui)
        self.pokemonBtn.clicked.connect(open_pokemon_ui)
