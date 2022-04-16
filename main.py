import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal, QObject
from testui import Ui_MainWindow

class Communicate(QObject):
    message = pyqtSignal()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button.clicked.connect(self.count_down)
        self.c.message.connect(self.close_message)

    def count_down(self):
        self.uic.listWidget.addItem("hello")
        if self.uic.listWidget.count() % 4 == 0:
            self.c.message.emit()

    def close_message(self):
        self.uic.listWidget.close()
        self.uic.label.setText("close")
        QMessageBox.about(self, "hello", "message")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

