import json
import sys

from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QTranslator, QLocale, QLibraryInfo
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication
from qt_material import apply_stylesheet

from configparse import read_style
from window.login import Login
from window.main_window import MainWindow


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


if __name__ == '__main__':
    app = MainApplication(sys.argv)

    # Tłumaczenie
    qt_translator = QTranslator()
    qt_translator.load('./resources/qt_pl.qm')
    app.installTranslator(qt_translator)

    try:
        style = read_style()
        apply_stylesheet(app, theme=style, invert_secondary=True)
    except KeyError as e:
        print(e)
        apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=True)

    app.setFont(QFont('', 12))

    window = Login()
    dec = window.exec_()
    if dec == QtWidgets.QDialog.Accepted:
        result = json.loads(window.response.text)
        print(json.dumps(result, indent=4, sort_keys=True))
        window = MainWindow(result)
        window.show()
    elif dec == QtWidgets.QDialog.Rejected:
        sys.exit(0)
    sys.exit(app.exec_())
