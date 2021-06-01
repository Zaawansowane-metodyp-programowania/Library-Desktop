import pytest
from PySide2 import QtCore

from window.main_window import MainWindow
from window.mainwidget import MainWidget

user = {
    "id": 0,
    "roleId": 3,
    "token": ""
}


@pytest.fixture
def main_window(qtbot):
    """
    Test Main Window
    """
    q_widget = MainWindow(user=user)
    qtbot.addWidget(q_widget)
    return q_widget


@pytest.fixture
def main_widget(qtbot):
    """
    Test Main Widget
    """
    q_widget = MainWidget(user=user)
    qtbot.addWidget(q_widget)
    return q_widget


def test_main_window(main_window):
    assert main_window.geometry() == QtCore.QRect(100, 100, 800, 600)
    assert main_window.windowTitle() == 'Biblioteka'


def test_main_widget_buttons(main_widget):
    assert main_widget.btn_home.text() == 'Strona główna'
    assert main_widget.btn_my_book.text() == 'Wypożyczone książki'
    assert main_widget.btn_reserved.text() == 'Zarezerwowane książki'
    assert main_widget.btn_library.text() == 'Biblioteka'
    assert main_widget.btn_profile.text() == 'Usuwanie profili'
    assert main_widget.btn_permission.text() == 'Utwórz konto z uprawnieniami'
    assert main_widget.btn_change_passwd.text() == 'Zmiana hasła'
    assert main_widget.btn_set_permission.text() == 'Uprawnienia'
    assert main_widget.btn_logout.text() == 'Wylogowanie'
    assert main_widget.btn_add_book.text() == 'Dodaj nową książkę'
    assert main_widget.btn_delete_profile.text() == 'Usuń konto'
    assert main_widget.btn_next_page.text() == 'Następna >'
    assert main_widget.btn_back_page.text() == '< Poprzednia'
    assert main_widget.btn_back_page.text() == '< Poprzednia'
    assert main_widget.btn_delete_book.text() == 'Usuń książkę'
    assert main_widget.btn_borrow_book.text() == 'Wypożycz książkę'
