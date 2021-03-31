from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget, QDialog, QDialogButtonBox, QSpacerItem, \
    QSizePolicy, QFormLayout, QAbstractItemView


class Widget(QWidget):
    def __init__(self, user):
        super(Widget, self).__init__()
        self.get_books_api = '/books'
        self.get_users_api = '/users'
        self.user = user
        self.h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._user_id = None

        # Strona główna
        self.lbl_home = QLabel('To jest dom')

        # Biblioteka
        self.lbl_title = QLabel('Wyszukaj poniżej')
        self.edit_search = QLineEdit()
        self.tbl_result = QTableWidget()

        self.tbl_result.setAlternatingRowColors(True)
        self.tbl_result.setCornerButtonEnabled(True)
        self.tbl_result.verticalHeader().setSortIndicatorShown(True)
        self.tbl_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_result.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_result.verticalHeader().setVisible(False)
        self.tbl_result.cellClicked.connect(self.cell_was_clicked)

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
        btn_box.accepted.connect(lambda: self.change_passwd(self._user_id))

    def cell_was_clicked(self, row, column):
        item = self.tbl_result.item(row, 0)
        print("Wiersz %d i kolumna %d została kliknięta: " % (row, column), item.text())
        self._user_id = item.text()
        if self.user.get('id') == 34:
            self.on_change_passwd_clicked()
