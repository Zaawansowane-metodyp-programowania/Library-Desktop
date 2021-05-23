from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QFont, QRegExpValidator
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget, QDialog, QDialogButtonBox, QSpacerItem, \
    QSizePolicy, QFormLayout, QAbstractItemView, QPushButton, QMessageBox, QComboBox, QHBoxLayout, \
    QVBoxLayout, QPlainTextEdit

from window.home_text_browser import HomeTextBrowser


class Widget(QWidget):
    """
    Klasa z podstawowymi elementami, na podstawie której została utworzona klasa docelowa. Nie moe istnieć bez klasy
    docelowej MainWidget ze względu na zawarte odnieniesia do funkcji, które istnieją w klasie MainWidget.
    """

    def __init__(self, user):
        super(Widget, self).__init__()
        self.library = QWidget()
        self.get_books_api = 'books'
        self.get_users_api = 'users'
        self.reservation_api = '/reservation/'
        self.user = user
        self.h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._user_id = None
        self._book_id = None
        self._role_id = 1
        self.dialog_password = QDialog()
        self.dialog_profile = QDialog()
        self.dialog_permission = QDialog()
        self.dialog_set_permission = QDialog()
        self.dialog_book = QDialog()
        self.layout_password = QFormLayout()
        self.layout_profile = QFormLayout()
        self.layout_permission = QFormLayout()
        self.layout_book = QFormLayout()
        self.regex = QRegExp('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        self.validator = QRegExpValidator(self.regex)
        self.btn_cancel_box = QDialogButtonBox.Cancel
        self.btn_ok_box = QDialogButtonBox.Ok
        self.btn_save_box = QDialogButtonBox.Save

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
        self.btn_next_page = QPushButton('Następna >')
        self.btn_back_page = QPushButton('< Poprzednia')
        self.combo_sort_by = QComboBox()
        self.combo_sort_direction = QComboBox()
        self.layout_btn = QHBoxLayout()
        self.layout_search = QHBoxLayout()
        self.layout_library = QVBoxLayout()
        self.library_widget()

        self.tbl_result.setAlternatingRowColors(True)
        self.tbl_result.setCornerButtonEnabled(False)
        self.tbl_result.verticalHeader().setSortIndicatorShown(True)
        self.tbl_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_result.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_result.setWordWrap(True)
        self.tbl_result.horizontalHeader().setStretchLastSection(True)
        self.tbl_result.resizeColumnsToContents()
        self.tbl_result.resizeRowsToContents()
        self.tbl_result.verticalHeader().setDefaultAlignment(Qt.AlignCenter | Qt.TextWordWrap)
        self.tbl_result.cellDoubleClicked.connect(self.cell_was_clicked)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        # Edycja książki
        self.edit_isbn = QLineEdit()
        self.edit_book_name = QLineEdit()
        self.edit_author = QLineEdit()
        self.edit_publisher = QLineEdit()
        self.edit_publish_date = QLineEdit()
        self.edit_category = QLineEdit()
        self.edit_isbn.setPlaceholderText('Wymagane')
        self.edit_book_name.setPlaceholderText('Wymagane')
        self.edit_author.setPlaceholderText('Wymagane')
        self.edit_publisher.setPlaceholderText('Wymagane')
        self.edit_publish_date.setPlaceholderText('Wymagane')
        self.edit_category.setPlaceholderText('Wymagane')
        self.edit_language_book = QLineEdit()
        self.edit_book_description = QPlainTextEdit()
        self.btn_delete_book = QPushButton('Usuń książkę')
        self.btn_borrow_book = QPushButton('Wypożycz książkę')
        self.book_id_widget()

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

    def library_widget(self):
        """
        Tworzy widgety potrzebne do obsługi zawartości biblioteki.
        """
        self.layout_search.addWidget(self.edit_search)
        self.layout_search.addWidget(self.combo_sort_by)
        self.layout_search.addWidget(self.combo_sort_direction)
        self.layout_library.addLayout(self.layout_search)
        self.layout_btn.addWidget(self.btn_back_page)
        self.layout_btn.addItem(self.h_spacer)
        self.layout_btn.addWidget(self.btn_next_page)
        self.layout_library.addLayout(self.layout_btn)
        self.library.setLayout(self.layout_library)
        self.combo_sort_by.setMinimumWidth(160)
        self.combo_sort_direction.setMinimumWidth(120)
        self.combo_sort_by.addItem('Sortuj według')
        self.combo_sort_by.addItem('Tytuł')
        self.combo_sort_by.addItem('Opis')
        self.combo_sort_by.addItem('Kategoria')
        self.combo_sort_by.addItem('Wydawca')
        self.combo_sort_by.addItem('Data wydania')
        self.combo_sort_direction.addItem('Rosnąco')
        self.combo_sort_direction.addItem('Malejąco')
        self.combo_sort_by.activated[str].connect(self.sort_by)
        self.combo_sort_direction.activated[str].connect(self.sort_direction)

    def change_password_widget(self):
        """
        Tworzy widgety niezbędne do obsługi zmiany hasła.
        """
        btn_box = QDialogButtonBox()
        lbl_passwd1 = QLabel('Wpisz stare hasło:')
        lbl_passwd2 = QLabel('Wpisz nowe hasło:')
        lbl_passwd3 = QLabel('Wpisz nowe hasło ponownie:')

        btn_box.setStandardButtons(self.btn_cancel_box | self.btn_ok_box)
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
        """
        Tworzy widgety niezbędne do obsługi edycji i usunięcia profilu.
        """
        self.btn_delete_profile.setStyleSheet("color: #dc3545; border-color : #dc3545")
        lbl_name = QLabel('Imię:')
        lbl_subname = QLabel('Nazwisko:')
        lbl_email = QLabel('Email:')
        btn_profile_box = QDialogButtonBox()
        btn_profile_box.setStandardButtons(self.btn_cancel_box | self.btn_save_box)

        self.edit_email.setValidator(self.validator)

        self.layout_profile.addRow(self.btn_delete_profile)
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
        """
        Tworzy widgety niezbędne do obsługi utworzenia użytkownika z uprawnieniami.
        """
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

        btn_box.setStandardButtons(self.btn_cancel_box | self.btn_ok_box)
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

    def set_permission(self, user_id):
        """
        Zmienia uprawnienia użytkownika.
        """
        layout_set = QFormLayout()
        self.combo_role_id.activated[str].connect(self.on_changed)

        btn_box = QDialogButtonBox()
        lbl_role = QLabel('Rola:')

        btn_box.setStandardButtons(self.btn_cancel_box | self.btn_ok_box)
        layout_set.addRow(lbl_role, self.combo_role_id)
        layout_set.setItem(1, QFormLayout.LabelRole, self.v_spacer)
        layout_set.setWidget(2, QFormLayout.FieldRole, btn_box)
        self.dialog_set_permission.setLayout(layout_set)

        btn_box.rejected.connect(self.on_home_clicked)
        btn_box.accepted.connect(lambda: self.change_permission(user_id))

        self.on_set_permission()

    def on_changed(self, text):
        """
        Zamienia nazwę przyjazną użytkownikowi w cyfrę odpowiadającą danej roli.
        :param text: str
        """
        role_id = {
            'Użytkownik': 1,
            'Pracownik': 2,
            'Administrator': 3
        }
        self._role_id = role_id.get(text)

    def book_id_widget(self):
        """
        Tworzy widgety niezbędne do obsługi edycji, usunięcia i wypożyczenia książki.
        """
        btn_save_box = QDialogButtonBox()
        lbl_isbn = QLabel('ISBN:')
        lbl_book_name = QLabel('Tytuł książki:')
        lbl_author_name = QLabel('Autor książki:')
        lbl_publisher = QLabel('Wydawaca:')
        lbl_publish_date = QLabel('Data wydania:')
        lbl_category = QLabel('Kategoria:')
        lbl_language = QLabel('Język książki:')
        lbl_book_description = QLabel('Opis książki:')
        layout_hbox = QHBoxLayout()
        self.btn_delete_book.setStyleSheet("color: #dc3545; border-color : #dc3545")

        btn_save_box.setStandardButtons(self.btn_cancel_box | self.btn_save_box)

        layout_hbox.addWidget(self.btn_delete_book)
        layout_hbox.addWidget(self.btn_borrow_book)
        self.layout_book.addRow(layout_hbox)
        self.layout_book.addRow(lbl_isbn, self.edit_isbn)
        self.layout_book.addRow(lbl_book_name, self.edit_book_name)
        self.layout_book.addRow(lbl_author_name, self.edit_author)
        self.layout_book.addRow(lbl_publisher, self.edit_publisher)
        self.layout_book.addRow(lbl_publish_date, self.edit_publish_date)
        self.layout_book.addRow(lbl_category, self.edit_category)
        self.layout_book.addRow(lbl_language, self.edit_language_book)
        self.layout_book.addRow(lbl_book_description, self.edit_book_description)
        self.layout_book.addItem(self.v_spacer)
        self.layout_book.addRow(btn_save_box)
        self.dialog_book.setLayout(self.layout_book)

        btn_save_box.rejected.connect(self.on_home_clicked)
        btn_save_box.accepted.connect(lambda: self.new_book(self._book_id))

    def cell_was_clicked(self, row, column):
        """
        Służy do obsługi tabel w programie. Każde kliknięcie jest walidowane pod kątem roli danego użytkownika,
        a także tytułu jaki widnieje nad tabelą. Dzięki temu w całym programie wystarczy jedna tabela.
        :param row: int
        :param column: int
        """
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

        if self.lbl_title.text() == 'Biblioteka' and self.user.get('roleId') > 1:
            self._user_id = None
            self._book_id = item.text()
            self.change_book(item.text())

        if self.lbl_title.text() == 'Wypożyczone książki' and self.user.get('roleId') > 1:
            self.back_book(item.text())

        if self.lbl_title.text() == 'Biblioteka' and self.user.get('roleId') == 1:
            self._user_id = None
            data = self.reservation_book(item.text())
            if data.status_code == 400:
                QMessageBox.warning(self, "Błąd", data.text)
            else:
                QMessageBox.information(self, "Zarezerwowano", "Podana pozycja została zarezerwowana!")
            self.on_library_clicked()

        if self.lbl_title.text() == 'Użytkownicy' and self.user.get('roleId') > 1:
            self.on_book_clicked(item.text())

        if self.lbl_title.text() == 'Wybierz użytkownika':
            self.borrow_book(self._book_id, item.text())

        if self.lbl_title.text() == 'Zarezerwowane książki':
            self.delete_reservation(self.tbl_result.item(row, 2).text())

        if self.lbl_title.text() == 'Uprawnienia':
            self.set_permission(self._user_id)
