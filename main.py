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


def main():
    app = MainApplication(sys.argv)

    # Tłumaczenie
    qt_translator = QTranslator()
    qt_translator.load("qt_" + QLocale.system().name(),
                       QLibraryInfo.location(QLibraryInfo.TranslationsPath))
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
        print(result)
        window = MainWindow(result)
        window.setContentsMargins(10, 10, 10, 10)
    elif dec == QtWidgets.QDialog.Rejected:
        sys.exit(0)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
