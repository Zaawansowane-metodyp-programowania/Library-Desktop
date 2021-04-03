import json
import queue
import threading

from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem, QMessageBox
from email_validator import validate_email, EmailNotValidError

from api_connect.delete_request import delete_request
from api_connect.get_request import get_request
from api_connect.patch_request import patch_request
from api_connect.post_request import post_request
from api_connect.put_request import put_request
from window import URL
from window import run_window
from window.widgets import Widget


class MainWidget(Widget):
    def __init__(self, user):
        super(MainWidget, self).__init__(user)
        self.que = queue.Queue()

        # Layouty
        self.layout = QVBoxLayout()
        self.menu_layout = QHBoxLayout()
        self.text_layout = QVBoxLayout()

        # Widgety
        self.btn_home = QPushButton('Strona główna')
        self.btn_my_book = QPushButton('Moje książki')
        self.btn_library = QPushButton('Biblioteka')
        self.btn_profile = QPushButton('Profil')
        self.btn_permission = QPushButton('Utwórz konto z uprawnieniami')
        self.btn_change_passwd = QPushButton('Zmiana hasła')
        self.btn_logout = QPushButton('Wylogowanie')

        # Ustawienia widgetów
        self.menu_layout.setContentsMargins(-1, -1, -1, 25)
        self.btn_home.clicked.connect(self.on_home_clicked)
        self.btn_my_book.clicked.connect(self.on_book_clicked)
        self.btn_library.clicked.connect(self.on_library_clicked)
        self.btn_permission.clicked.connect(self.on_permission_clicked)
        if self.user.get('roleId') != 3:
            self.btn_change_passwd.clicked.connect(self.on_change_passwd_clicked)
            self.btn_profile.clicked.connect(self.on_profile_clicked)
        else:
            self.btn_change_passwd.clicked.connect(self.on_change_passwd_admin_clicked)
            self.btn_profile.clicked.connect(self.on_profile_admin_clicked)
        self.btn_logout.clicked.connect(self.on_logout_clicked)

        # Przypisanie widgetów do layoutów
        self.menu_layout.addWidget(self.btn_home)
        self.menu_layout.addWidget(self.btn_my_book)
        self.menu_layout.addWidget(self.btn_library)
        self.menu_layout.addWidget(self.btn_profile)
        if self.user.get('roleId') == 3:
            self.menu_layout.addWidget(self.btn_permission)
        self.menu_layout.addWidget(self.btn_change_passwd)
        self.menu_layout.addItem(self.h_spacer)
        self.menu_layout.addWidget(self.btn_logout)
        self.text_layout.addWidget(self.lbl_home)

        self.layout.addLayout(self.menu_layout)
        self.layout.addLayout(self.text_layout)

        self.setLayout(self.layout)

    def clear_layout(self):
        for i in reversed(range(self.text_layout.count())):
            self.text_layout.itemAt(i).widget().setParent(None)

    def on_home_clicked(self):
        print("Home")
        self.clear_layout()
        self.text_layout.addWidget(self.lbl_home)

    def on_book_clicked(self):
        print("Books")

    def on_library_clicked(self):
        print("library")
        self.clear_layout()
        self.lbl_title.setText('Wyszukaj poniżej')
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.edit_search)
        self.text_layout.addWidget(self.tbl_result)
        self.get_books()

    def on_profile_clicked(self):
        print("profile")
        self.clear_layout()
        self.lbl_title.setText('Ustawienia profilu')
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.dialog_profile)
        data = self.get_user_id()
        self.edit_name.setText(data.get('name'))
        self.edit_subname.setText(data.get('surname'))
        self.edit_email.setText(data.get('email'))

    def on_profile_admin_clicked(self):
        self.clear_layout()
        self.lbl_title.setText('Usuwanie profilu')
        self.text_layout.addWidget(self.lbl_title)
        self.get_users()
        self.text_layout.addWidget(self.tbl_result)
        # self.tbl_result.cellClicked.connect(self.profile_clicked)

    def on_permission_clicked(self):
        print("permission")
        self.clear_layout()
        self.lbl_title.setText('Utwórz nowe konto z uprawnieniami')
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.dialog_permission)

    def on_change_passwd_clicked(self):
        print("Change password")
        self.clear_layout()
        self.lbl_title.setText('Zmiana hasła')
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.dialog_password)
        self.edit_passwd1.setFocus()

    def on_change_passwd_admin_clicked(self):
        print("Change admin password")
        self.clear_layout()
        self.lbl_title.setText('Zmiana hasła')
        self.text_layout.addWidget(self.lbl_title)
        self.get_users()
        self.text_layout.addWidget(self.tbl_result)

    def on_logout_clicked(self):
        print("Logout")
        self.clear_layout()
        self.close()
        self.parent().destroy()
        run_window()

    def set_data(self, data):
        self.tbl_result.clear()
        row_count = (len(data))
        column_count = (len(data[0]))
        roleid = {
            1: 'Użytkownik',
            2: 'Pracownik',
            3: 'Administrator'
        }

        self.tbl_result.setColumnCount(column_count)
        self.tbl_result.setRowCount(row_count)

        self.tbl_result.setHorizontalHeaderLabels((list(data[0].keys())))

        if list(data[0].keys())[0] == 'id':
            self.tbl_result.hideColumn(0)
        if 'roleId' in list(data[0].keys()) and self.lbl_title.text() != 'Utwórz konto z uprawnieniami':
            self.tbl_result.hideColumn(4)
        else:
            self.tbl_result.showColumn(4)

        for row in range(row_count):
            for column in range(column_count):
                item = (list(data[row].values())[column])
                if column == 4:
                    item = roleid.get(item)
                self.tbl_result.setItem(row, column, QTableWidgetItem(str(item)))

        self.tbl_result.resizeColumnsToContents()

    def get_books(self):
        x = threading.Thread(
            target=get_request,
            args=("".join([URL, self.get_books_api, '?PageNumber=1&PageSize=15']), self.user.get('token'), self.que))

        x.start()
        x.join()

        data = self.que.get()
        self.set_data(data.get('items'))

    def get_users(self):
        x = threading.Thread(
            target=get_request,
            args=("".join([URL, self.get_users_api]), self.user.get('token'), self.que))

        x.start()
        x.join()

        data = self.que.get()
        self.set_data(data)

    def get_user_id(self):
        user_id_api = "".join([URL, self.get_users_api, '/', str(self.user.get('id'))])
        x = threading.Thread(
            target=get_request,
            args=(user_id_api, self.user.get('token'), self.que))

        x.start()
        x.join()

        data = self.que.get()
        return data

    def post_user(self):
        user_api = "".join([URL, self.get_users_api])
        jsons = {
            "name": self.edit_new_name.text(),
            "surname": self.edit_new_surname.text(),
            "email": self.edit_new_email.text(),
            "password": self.edit_pass2.text(),
            "confirmPassword": self.edit_pass3.text(),
            "roleId": self._role_id
        }

        if self.edit_pass2.text() != self.edit_pass3.text():
            QMessageBox.warning(self, "Błędne hasła", "Hasła nie są takie same.")
            self.edit_pass2.setText('')
            self.edit_pass3.setText('')
            self.edit_pass2.setFocus()
            return
        if self.edit_pass2.text() == '':
            QMessageBox.warning(self, "Błąd", "Hasła nie mogą być puste.")
            self.edit_pass2.setFocus()
            return
        if self.edit_new_email.text() == '':
            QMessageBox.warning(self, "Błąd", "Email nie może być pusty.")
            self.edit_new_email.setFocus()
            return

        x = threading.Thread(
            target=post_request,
            args=(user_api, jsons, self.user.get('token'), self.que))

        x.start()
        x.join()

        data = self.que.get()
        if data.status_code == 201:
            QMessageBox.information(self, "Nowe konto", 'Utworzono nowe konto.')
        print(data)

    def change_passwd(self, user_id=None):
        if user_id is None:
            user_id = self.user.get('id')
        print(user_id)
        token = self.user.get('token')
        url_password = "".join(['users/changePassword/', str(user_id)])

        if self.edit_passwd2.text() == '' or self.edit_passwd3.text() == '':
            QMessageBox.warning(self, "Brak nowego hasła", "Nowe hasło nie może być puste")
            self.edit_passwd2.setText('')
            self.edit_passwd3.setText('')
            self.edit_passwd2.setFocus()
            return

        if self.edit_passwd2.text() != self.edit_passwd3.text():
            QMessageBox.warning(self, "Błędne dane", "Podane hasła nie są identyczne!")
            self.edit_passwd2.setText('')
            self.edit_passwd3.setText('')
            self.edit_passwd2.setFocus()
            return

        jsons = {
            "oldPassword": self.edit_passwd1.text(),
            "newPassword": self.edit_passwd2.text(),
            "confirmNewPassword": self.edit_passwd3.text()
        }
        x = threading.Thread(target=patch_request, args=("".join([URL, url_password]), jsons, token, self.que))

        x.start()
        x.join()

        response = self.que.get()
        if response.status_code == 400:
            print(response.text)
            if response.text == 'Invalid password':
                QMessageBox.warning(self, "Błędne hasło", response.text)
                self.edit_passwd1.setText('')
                self.edit_passwd1.setFocus()
                return
            error = json.loads(response.text)
            err = json.loads(json.dumps(error['errors'], indent=4, sort_keys=True))
            print(err)
            for key in err.keys():
                if key == 'NewPassword':
                    QMessageBox.warning(self, "Nowe hasło", err.get(key)[0])

        if response.status_code == 200:
            QMessageBox.information(self, "Hasło zmienione", "Hasło zostało zmienione!")
            self.edit_passwd1.setText('')
            self.edit_passwd2.setText('')
            self.edit_passwd3.setText('')
            self.on_home_clicked()

    def delete_profile(self, user_id=None):
        token = self.user.get('token')
        _user_id = user_id
        if _user_id is None:
            user_id = self.user.get('id')
        url_profile = "".join([URL, self.get_users_api, '/', str(user_id)])
        button_reply = QMessageBox.question(
            self,
            'Usuwanie',
            "Czy na pewnno chcesz usunąć te konto?\nOperacji tej nie można cofnąć.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if button_reply == QMessageBox.Yes:
            pass
        else:
            return

        x = threading.Thread(target=delete_request, args=(url_profile, token, self.que))

        x.start()
        x.join()

        response = self.que.get()
        if response.status_code == 204:
            QMessageBox.information(self, "Usunięto", "Konto zostało usunięte!")
            if _user_id != self.user.get('id'):
                return
            self.on_logout_clicked()

        if response.status_code == 500:
            QMessageBox.warning(self, "Błąd", "Nie można usunąć użytkownika, który wypożyczył książki!")
            return

    def change_profile(self):
        token = self.user.get('token')
        url_profile = "".join([URL, self.get_users_api, '/', str(self.user.get('id'))])

        name = self.edit_name.text()
        surname = self.edit_subname.text()
        email = self.edit_email.text()

        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(e)
            QMessageBox.warning(self, "Błędny email", "Proszę wpisać poprawny email")
            self.edit_email.setFocus()
            return

        if name == '' or surname == '' or email == '':
            QMessageBox.warning(self, "Błędne dane", "Podane dane nie mogą być puste!")
            self.edit_name.setFocus()
            return

        jsons = {
            "name": name,
            "surname": surname,
            "email": email
        }

        x = threading.Thread(target=put_request, args=(url_profile, jsons, token, self.que))

        x.start()
        x.join()

        response = self.que.get()
        print(response)
        if response.status_code == 200:
            QMessageBox.information(self, "Zmiana danych", "Dane zostały pomyślnie zapisane!")
            return
