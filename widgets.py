from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()

        # Strona główna
        self.lbl_home = QLabel('To jest dom')

        # Biblioteka
        self.lbl_title = QLabel('Wyszukaj poniżej')
        self.edit_search = QLineEdit()
        self.tbl_result = QTableWidget()

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)
