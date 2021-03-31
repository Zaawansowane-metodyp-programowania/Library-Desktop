import json
import queue
import threading

from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QTableWidgetItem, QMessageBox

from api_connect.get_request import get_request
from api_connect.patch_request import patch_request
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
        self.btn_permission = QPushButton('Uprawnienia')
        self.btn_change_passwd = QPushButton('Zmiana hasła')
        self.btn_logout = QPushButton('Wylogowanie')

        # Ustawienia widgetów
        self.menu_layout.setContentsMargins(-1, -1, -1, 25)
        self.btn_home.clicked.connect(self.on_home_clicked)
        self.btn_my_book.clicked.connect(self.on_book_clicked)
        self.btn_library.clicked.connect(self.on_library_clicked)
        self.btn_profile.clicked.connect(self.on_profile_clicked)
        self.btn_permission.clicked.connect(self.on_permission_clicked)
        if self.user.get('id') != 34:
            self.btn_change_passwd.clicked.connect(self.on_change_passwd_clicked)
        else:
            self.btn_change_passwd.clicked.connect(self.on_change_passwd_admin_clicked)
        self.btn_logout.clicked.connect(self.on_logout_clicked)

        # Przypisanie widgetów do layoutów
        self.menu_layout.addWidget(self.btn_home)
        self.menu_layout.addWidget(self.btn_my_book)
        self.menu_layout.addWidget(self.btn_library)
        self.menu_layout.addWidget(self.btn_profile)
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
        self.clear_layout()
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.edit_search)
        self.text_layout.addWidget(self.tbl_result)
        self.get_books()

    def on_library_clicked(self):
        print("library")

    def on_profile_clicked(self):
        print("profile")

    def on_permission_clicked(self):
        print("permission")

    def on_change_passwd_clicked(self):
        print("Change password")
        self.clear_layout()
        self.text_layout.addWidget(self.passwd)
        self.edit_passwd1.setFocus()

    def on_change_passwd_admin_clicked(self):
        print("Change admin password")
        self.clear_layout()
        self.get_users()
        self.text_layout.addWidget(self.tbl_result)

    def on_logout_clicked(self):
        print("Logout")
        self.clear_layout()
        self.parent().destroy()
        run_window()

    def set_data(self, data):
        self.tbl_result.clear()
        row_count = (len(data))
        column_count = (len(data[0]))

        self.tbl_result.setColumnCount(column_count)
        self.tbl_result.setRowCount(row_count)

        self.tbl_result.setHorizontalHeaderLabels((list(data[0].keys())))

        if list(data[0].keys())[0] == 'id':
            self.tbl_result.hideColumn(0)

        for row in range(row_count):
            for column in range(column_count):
                item = (list(data[row].values())[column])
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

    def change_passwd(self, user_id=None):
        if user_id is None:
            user_id = self.user.get('id')
        print(user_id)
        token = self.user.get('token')
        url_password = "".join(['users/changePassword/', str(user_id)])

        if self.user.get('id') == 34:
            self.edit_passwd3.setText(self.edit_passwd2.text())
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
        que = queue.Queue()
        x = threading.Thread(target=patch_request, args=("".join([URL, url_password]), jsons, token, que))

        x.start()
        x.join()

        response = que.get()
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
