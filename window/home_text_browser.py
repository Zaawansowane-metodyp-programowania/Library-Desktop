from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTextBrowser, QFrame


class HomeTextBrowser(QTextBrowser):
    """
    Klasa obsługująca stronę główną, w której zawarte są podstawowe informacje na temat funkcjonalności programu.
    """
    def __init__(self):
        super(HomeTextBrowser, self).__init__()

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.NoFrame)

        self.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; "
            "font-style:normal;\" bgcolor=\"transparent\">\n "
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">        </p>\n "
            "<h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Witaj w "
            "aplikacji bibliotecznej!</span></h1>\n "
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\">Jeste\u015b teraz na stronie g\u0142\u00f3wnej. Aby "
            "skorzysta\u0107 z aplikacji u\u017cyj przycisk\u00f3w u g\u00f3ry.</p>\n "
            "<p align=\"cente"
            "r\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\"><br /></p>\n "
            ""
            "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Moje "
            "ksi\u0105\u017cki</span></h2>\n "
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\">Tutaj znajdziesz list\u0119 ksi\u0105\u017cek jakie "
            "wypo\u017cyczy\u0142e\u015b. Pracownicy maj\u0105 dost\u0119p do listy ksi\u0105\u017cek ka\u017cdej "
            "osoby.</p>\n "
            "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; "
            "font-weight:600;\">Biblioteka</span></h2>\n "
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text- "
            "indent:0px;\">Znajdziesz tu ca\u0142\u0105 zawarto\u015b\u0107 biblioteki. B\u0119dziesz m\u00f3g\u0142 "
            "zarezerwowa\u0107 dan\u0105 ksi\u0105\u017ck\u0119 poprzez klikni\u0119cie w ni\u0105.</p>\n "
            "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; "
            "font-weight:600;\">Profil</span></h2>\n "
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\">Tutaj znajdowa\u0107 si\u0119 b\u0119d\u0105 wszystkie informacje "
            "o tobie. B\u0119dziesz m\u00f3g\u0142 je edytowa\u0107, a tak\u017ce b\u0119dziesz mia\u0142 "
            "mo\u017cliwo\u015b\u0107 usuni\u0119cia swojego konta.</p>\n "
            "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Zmiana "
            "has\u0142a</span></h2>\n "
            "<p align=\"center\""
            "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\">Je\u015bli czujesz potrzeb\u0119, mo\u017cesz zmieni\u0107 has\u0142o na "
            "dowolne.</p>\n "
            "<h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; "
            "font-weight:600;\">Wylogowanie</span></h2>\n "
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; "
            "-qt-block-indent:0; text-indent:0px;\">Po sko\u0144czonej pracy mo\u017cesz si\u0119 wylogowa\u0107 i "
            "udost\u0119pni\u0107 program innemu u\u017cytkownikowi bez wy\u0142\u0105czania go.    "
            "</p></body></html>")
