import queue
import sys
import threading

from PySide2 import QtGui
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QLabel, QApplication, QLineEdit, QFormLayout, \
    QMessageBox, QPushButton, QSpacerItem, QSizePolicy

from api_connect.post_request import post_request
from window import URL
from window.register import Register


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()

        self.url_login = 'account/login'
        self.response = None
        self.jsons = {}

        self.setWindowTitle('Logowanie')
        self.setWindowIcon(QtGui.QIcon('resources/library_icon.png'))
        self.lbl_login = QLabel('Login (e-mail):')
        self.lbl_passwd = QLabel('Hasło:')
        self.edit_login = QLineEdit()
        self.edit_passwd = QLineEdit()
        self.edit_passwd.setEchoMode(QLineEdit.Password)
        self.setMinimumWidth(400)
        self.btn_register = QPushButton('Utwórz nowe konto')
        self.btn_register.setStyleSheet("color: #17a2b8; border-color : #17a2b8")

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self.login_in)
        self.buttonBox.rejected.connect(self.reject)
        self.btn_register.clicked.connect(self.register)

        self.layout = QFormLayout()
        self.layout.setWidget(0, QFormLayout.LabelRole, self.lbl_login)
        self.layout.setWidget(0, QFormLayout.FieldRole, self.edit_login)
        self.layout.setWidget(1, QFormLayout.LabelRole, self.lbl_passwd)
        self.layout.setWidget(1, QFormLayout.FieldRole, self.edit_passwd)
        self.layout.addRow(self.btn_register)

        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.show()

    def register(self):
        dialog = Register()
        dialog.show()
        dialog.exec_()

    def login_in(self):
        if not self.edit_login.text() or not self.edit_passwd.text():
            QMessageBox.warning(self, "Błędne dane logowania", "Proszę wpisać login oraz hasło")
            self.edit_login.setFocus()
            return

        jsons = {
            "email": self.edit_login.text(),
            "password": self.edit_passwd.text()
        }
        que = queue.Queue()
        x = threading.Thread(target=post_request, args=("".join([URL, self.url_login]), jsons, None, que))

        x.start()
        x.join()

        self.response = que.get()
        if self.response == 'ConnectionError':
            QMessageBox.critical(self, "Błąd", 'Błąd połączenia z internetem! Sprawdź połączenie')
            return
        print(self.response)
        if self.response.status_code == 400:
            QMessageBox.critical(self, "Niepoprawne dane logowania", self.response.text)
            self.edit_login.setText('')
            self.edit_passwd.setText('')
            self.edit_login.setFocus()
            return

        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Login()
    app.exec_()
