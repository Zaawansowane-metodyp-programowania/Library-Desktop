from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QFont, QRegExpValidator
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget, QDialog, QDialogButtonBox, QSpacerItem, \
    QSizePolicy, QFormLayout, QAbstractItemView, QPushButton, QMessageBox, QComboBox

from window.home_text_browser import HomeTextBrowser


class Widget(QWidget):
    def __init__(self, user):
        super(Widget, self).__init__()
        self.get_books_api = 'books'
        self.get_users_api = 'users'
        self.user = user
        self.h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._user_id = None
        self._role_id = 1
        self.dialog_password = QDialog()
        self.dialog_profile = QDialog()
        self.dialog_permission = QDialog()
        self.layout_password = QFormLayout()
        self.layout_profile = QFormLayout()
        self.layout_permission = QFormLayout()
        self.regex = QRegExp('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        self.validator = QRegExpValidator(self.regex)

        # Strona główna
        self.lbl_home = HomeTextBrowser()

        # Profil
        self.edit_name = QLineEdit()
        self.edit_subname = QLineEdit()
        self.edit_email = QLineEdit()
        self.btn_delete_profile = QPushButton('Usuń konto')
        self.profile_widget()

        # Biblioteka
        self.lbl_title = QLabel()
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
        self.edit_passwd1 = QLineEdit()
        self.edit_passwd2 = QLineEdit()
        self.edit_passwd3 = QLineEdit()
        self.change_password_widget()

        # Profil z uprawnieniami
        self.edit_pass2 = QLineEdit()
        self.edit_pass3 = QLineEdit()
        self.edit_new_name = QLineEdit()
        self.edit_new_surname = QLineEdit()
        self.edit_new_email = QLineEdit()
        self.combo_role_id = QComboBox(self)
        self.role_profile_widget()

    def clear_form(self):
        for i in reversed(range(self.layout_password.count())):
            self.layout_password.itemAt(i).widget().setParent(None)

    def change_password_widget(self):
        btn_box = QDialogButtonBox()
        lbl_passwd1 = QLabel('Wpisz stare hasło:')
        lbl_passwd2 = QLabel('Wpisz nowe hasło:')
        lbl_passwd3 = QLabel('Wpisz nowe hasło ponownie:')

        btn_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        if self.user.get('roleId') != 3:
            self.layout_password.addRow(lbl_passwd1, self.edit_passwd1)
        self.layout_password.addRow(lbl_passwd2, self.edit_passwd2)
        self.layout_password.addRow(lbl_passwd3, self.edit_passwd3)
        self.layout_password.setItem(3, QFormLayout.LabelRole, self.v_spacer)
        self.layout_password.setWidget(4, QFormLayout.FieldRole, btn_box)
        self.dialog_password.setLayout(self.layout_password)

        btn_box.rejected.connect(self.on_home_clicked)
        btn_box.accepted.connect(lambda: self.change_passwd(self._user_id))

    def profile_widget(self):
        self.btn_delete_profile.setStyleSheet("color: #dc3545; border-color : #dc3545")
        lbl_name = QLabel('Imię:')
        lbl_subname = QLabel('Nazwisko:')
        lbl_email = QLabel('Email:')
        btn_profile_box = QDialogButtonBox()
        btn_profile_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)

        self.edit_email.setValidator(self.validator)

        self.layout_profile.setWidget(0, QFormLayout.FieldRole, self.btn_delete_profile)
        self.layout_profile.addRow(lbl_name, self.edit_name)
        self.layout_profile.addRow(lbl_subname, self.edit_subname)
        self.layout_profile.addRow(lbl_email, self.edit_email)
        self.layout_profile.setItem(4, QFormLayout.LabelRole, self.v_spacer)
        self.layout_profile.setWidget(5, QFormLayout.FieldRole, btn_profile_box)
        self.dialog_profile.setLayout(self.layout_profile)

        btn_profile_box.rejected.connect(self.on_home_clicked)
        btn_profile_box.accepted.connect(self.change_profile)
        self.btn_delete_profile.clicked.connect(self.delete_profile)

    def role_profile_widget(self):
        self.combo_role_id.addItem('Użytkownik')
        self.combo_role_id.addItem('Pracownik')
        self.combo_role_id.addItem('Administrator')
        self.combo_role_id.activated[str].connect(self.on_changed)
        self.edit_pass2.setEchoMode(QLineEdit.Password)
        self.edit_pass3.setEchoMode(QLineEdit.Password)
        self.edit_new_email.setValidator(self.validator)

        btn_box = QDialogButtonBox()
        lbl_name = QLabel('Imię:')
        lbl_subname = QLabel('Nazwisko:')
        lbl_email = QLabel('Email:')
        lbl_pass2 = QLabel('Wpisz hasło:')
        lbl_pass3 = QLabel('Wpisz hasło ponownie:')
        lbl_role = QLabel('Rola:')

        btn_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.layout_permission.addRow(lbl_name, self.edit_new_name)
        self.layout_permission.addRow(lbl_subname, self.edit_new_surname)
        self.layout_permission.addRow(lbl_email, self.edit_new_email)
        self.layout_permission.addRow(lbl_pass2, self.edit_pass2)
        self.layout_permission.addRow(lbl_pass3, self.edit_pass3)
        self.layout_permission.addRow(lbl_role, self.combo_role_id)
        self.layout_permission.setItem(7, QFormLayout.LabelRole, self.v_spacer)
        self.layout_permission.setWidget(8, QFormLayout.FieldRole, btn_box)
        self.dialog_permission.setLayout(self.layout_permission)

        btn_box.rejected.connect(self.on_home_clicked)
        btn_box.accepted.connect(self.post_user)

    def on_changed(self, text):
        role_id = {
            'Użytkownik': 1,
            'Pracownik': 2,
            'Administrator': 3
        }
        self._role_id = role_id.get(text)

    def cell_was_clicked(self, row, column):
        item = self.tbl_result.item(row, 0)
        print("Wiersz %d i kolumna %d została kliknięta: " % (row, column), item.text())
        self._user_id = item.text()

        if self.user.get('roleId') == 3 and self.lbl_title.text() == 'Zmiana hasła':
            self.on_change_passwd_clicked()

        if int(self._user_id) != self.user.get('id') and self.lbl_title.text() == 'Usuwanie profilu':
            self.delete_profile(self._user_id)
        if int(self._user_id) == self.user.get('id') and self.lbl_title.text() == 'Usuwanie profilu':
            QMessageBox.warning(self, "Błąd!", "Nie można usunąć konta admina!")
            return

    def profile_clicked(self, row, column):
        item = self.tbl_result.item(row, 0)
        print("Wiersz %d i kolumna %d została kliknięta: " % (row, column), item.text())
        self._user_id = item.text()
