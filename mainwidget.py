from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

from widgets import Widget


class PushButton(QPushButton):
    def __init__(self, text):
        super(PushButton, self).__init__(text)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setText(text)


class MainWidget(Widget):
    def __init__(self):
        super(MainWidget, self).__init__()

        # Layouty
        self.layout = QVBoxLayout()
        self.menu_layout = QHBoxLayout()
        self.text_layout = QVBoxLayout()

        # Widgety
        self.btn_home = PushButton('Strona główna')
        self.btn_my_book = PushButton('Moje książki')
        self.btn_library = PushButton('Biblioteka')
        self.btn_profile = PushButton('Profil')
        self.btn_permission = PushButton('Uprawnienia')

        # Ustawienia widgetów
        self.menu_layout.setContentsMargins(-1, -1, -1, 25)
        self.btn_home.clicked.connect(self.on_home_clicked)
        self.btn_my_book.clicked.connect(self.on_book_clicked)
        self.btn_library.clicked.connect(self.on_library_clicked)
        self.btn_profile.clicked.connect(self.on_profile_clicked)
        self.btn_permission.clicked.connect(self.on_permission_clicked)

        # Przypisanie widgetów do layoutów
        self.menu_layout.addWidget(self.btn_home)
        self.menu_layout.addWidget(self.btn_my_book)
        self.menu_layout.addWidget(self.btn_library)
        self.menu_layout.addWidget(self.btn_profile)
        self.menu_layout.addWidget(self.btn_permission)
        self.text_layout.addWidget(self.lbl_home)

        self.layout.addLayout(self.menu_layout)
        self.layout.addLayout(self.text_layout)

        self.setLayout(self.layout)

    def on_home_clicked(self):
        print("Home")
        for i in reversed(range(self.text_layout.count())):
            self.text_layout.itemAt(i).widget().setParent(None)
        self.text_layout.addWidget(self.lbl_home)

    def on_book_clicked(self):
        print("Books")
        for i in reversed(range(self.text_layout.count())):
            self.text_layout.itemAt(i).widget().setParent(None)
        self.text_layout.addWidget(self.lbl_title)
        self.text_layout.addWidget(self.edit_search)
        self.text_layout.addWidget(self.tbl_result)

    def on_library_clicked(self):
        print("library")

    def on_profile_clicked(self):
        print("profile")

    def on_permission_clicked(self):
        print("permission")
