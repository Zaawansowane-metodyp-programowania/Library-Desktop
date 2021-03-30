from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget, QDialog, QDialogButtonBox, QSpacerItem, \
    QSizePolicy, QFormLayout


class Widget(QWidget):
    def __init__(self, user):
        super(Widget, self).__init__()
        self.get_books_api = '/books'
        self.user = user
        self.h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        # Zmiana hasła
        self.dialog_layout = QFormLayout()
        self.passwd = QDialog()
        btn_box = QDialogButtonBox()
        lbl_passwd1 = QLabel('Wpisz stare hasło:')
        lbl_passwd2 = QLabel('Wpisz nowe hasło:')
        lbl_passwd3 = QLabel('Wpisz nowe hasło ponownie:')
        self.edit_passwd1 = QLineEdit()
        self.edit_passwd2 = QLineEdit()
        self.edit_passwd3 = QLineEdit()
        self.v_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        btn_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        if self.user.get('id') != 34:
            self.dialog_layout.addRow(lbl_passwd1, self.edit_passwd1)
            self.dialog_layout.addRow(lbl_passwd3, self.edit_passwd3)
        self.dialog_layout.addRow(lbl_passwd2, self.edit_passwd2)
        self.dialog_layout.setItem(3, QFormLayout.LabelRole, self.v_spacer)
        self.dialog_layout.setWidget(4, QFormLayout.FieldRole, btn_box)
        self.passwd.setLayout(self.dialog_layout)

        btn_box.rejected.connect(self.on_home_clicked)
        btn_box.accepted.connect(self.change_passwd)
