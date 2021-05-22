import queue
import threading

from PySide2 import QtGui
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QDialog, QFormLayout, QDialogButtonBox, QLabel, QLineEdit, QSpacerItem, QSizePolicy, \
    QMessageBox

from api_connect.post_request import post_request
from window import URL


class Register(QDialog):
    """
    Klasa służąca do utworzenia nowego użytkownika z najniższymi uprawnieniami.
    """
    def __init__(self):
        super(Register, self).__init__()
        self.url_register = 'account/register'

        layout = QFormLayout()
        btn_box = QDialogButtonBox()
        lbl_name = QLabel('Imię:')
        lbl_subname = QLabel('Nazwisko:')
        lbl_email = QLabel('Email:')
        lbl_pass2 = QLabel('Wpisz hasło:')
        lbl_pass3 = QLabel('Wpisz hasło ponownie:')
        self.edit_name = QLineEdit()
        self.edit_surname = QLineEdit()
        self.edit_email = QLineEdit()
        self.edit_pass2 = QLineEdit()
        self.edit_pass3 = QLineEdit()
        self.edit_pass2.setEchoMode(QLineEdit.Password)
        self.edit_pass3.setEchoMode(QLineEdit.Password)
        v_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.regex = QRegExp('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        self.validator = QRegExpValidator(self.regex)
        self.edit_email.setValidator(self.validator)

        self.setWindowTitle('Rejestracja')
        self.setWindowIcon(QtGui.QIcon('resources/library_icon.png'))
        self.setMinimumWidth(640)
        self.setMinimumHeight(400)

        btn_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        layout.addRow(lbl_name, self.edit_name)
        layout.addRow(lbl_subname, self.edit_surname)
        layout.addRow(lbl_email, self.edit_email)
        layout.addRow(lbl_pass2, self.edit_pass2)
        layout.addRow(lbl_pass3, self.edit_pass3)
        layout.setItem(6, QFormLayout.LabelRole, v_spacer)
        layout.setWidget(7, QFormLayout.FieldRole, btn_box)
        self.setLayout(layout)

        btn_box.rejected.connect(self.reject)
        btn_box.accepted.connect(self.register_user)

    def register_user(self):
        """
        Rejestruje nowego użytkownika z zerowymi uprawnieniami (jedynie rezerwowanie książek i przeglądanie
        własnych, wypożyczonych książek).
        """
        jsons = {
            "name": self.edit_name.text(),
            "surname": self.edit_surname.text(),
            "email": self.edit_email.text(),
            "password": self.edit_pass2.text(),
            "confirmPassword": self.edit_pass3.text(),
            "roleId": 1
        }

        if jsons.get('password') != jsons.get('confirmPassword'):
            QMessageBox.warning(self, "Błędne hasła", "Hasła nie są takie same.")
            return
        if jsons.get('password') == '':
            QMessageBox.warning(self, "Błąd", "Hasła nie mogą być puste.")
            return
        if len(self.edit_pass2.text()) < 6:
            QMessageBox.warning(self, "Błąd", "Hasło jest za krótkie.")
            return
        if jsons.get('email') == '':
            QMessageBox.warning(self, "Błąd", "Email nie może być pusty.")
            self.edit_new_email.setFocus()
            return

        que = queue.Queue()
        x = threading.Thread(target=post_request, args=("".join([URL, self.url_register]), jsons, None, que))

        x.start()
        x.join()

        response = que.get()
        if response == 'ConnectionError':
            QMessageBox.critical(self, "Błąd", 'Błąd połączenia z internetem! Sprawdź połączenie.')
            return
        print(response)
        if response.status_code == 200:
            QMessageBox.information(self, "Rejestracja", 'Pomyślnie zarejestrowano nowego użytkownika.')
        self.accept()
