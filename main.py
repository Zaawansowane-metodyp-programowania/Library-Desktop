import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from darktheme.widget_template import DarkPalette


class MainApplication(QApplication):
    """
    Klasa dziedzicząca po QApplication.
    Ustawienie ciemnego motywu.
    """

    def __init__(self, *args, **kwargs):
        super(MainApplication, self).__init__(*args, **kwargs)

        self.setStyle('Fusion')
        self.setPalette(DarkPalette())
        self.setStyleSheet('QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }')


class MainWindow(QMainWindow):
    """
    Klasa dziedzicząca po QMainWindow, wzorzec budowniczy.
    Ustawienie podstawowego głównego okna.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Biblioteka")
        self.setWindowIcon(QtGui.QIcon('resources/library_icon.png'))


if __name__ == '__main__':
    app = MainApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
