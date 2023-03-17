from PyQt6.QtCore import *


class WorkerSignal(QObject):
    finished = pyqtSignal()
