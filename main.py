import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from darktheme.widget_template import DarkPalette

from mainwidget import MainWidget


class MainApplication(QApplication):
    """
    Klasa dziedzicząca po QApplication.
    Ustawienie ciemnego motywu.
    """

    def __init__(self, *args, **kwargs):
        super(MainApplication, self).__init__(*args, **kwargs)

        # Włączanie HDPI dla tekstu i ikon
        self.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        self.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

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

        self.setWindowTitle('Biblioteka')
        self.setWindowIcon(QtGui.QIcon('resources/library_icon.png'))
        widget = MainWidget()
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = MainApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
