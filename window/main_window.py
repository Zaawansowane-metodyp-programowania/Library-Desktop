from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QAction
from qt_material import QtStyleTools, list_themes

from configparse import writing
from window.mainwidget import MainWidget


class MainWindow(QMainWindow, QtStyleTools):
    """
    Klasa dziedzicząca po QMainWindow, wzorzec budowniczy.
    Ustawienie podstawowego głównego okna.
    """

    def __init__(self, user, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 800, 600)

        self.setWindowTitle('Biblioteka')
        self.setWindowIcon(QtGui.QIcon('resources/library_icon.png'))
        bar = self.menuBar()
        style = bar.addMenu("Motyw")
        for item in list_themes():
            style.addAction(item.replace('_', ' ').split('.')[0].capitalize())
        style.triggered[QAction].connect(self.processtrigger)
        widget = MainWidget(user)
        self.setCentralWidget(widget)

    def processtrigger(self, q):
        self.apply_stylesheet(self, q.text().lower().replace(' ', '_') + '.xml')
        writing(q.text().lower().replace(' ', '_') + '.xml')
