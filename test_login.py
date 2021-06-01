import pytest
from PySide2.QtWidgets import QLineEdit

from window.login import Login


@pytest.fixture
def login(qtbot):
    """
    Test Login
    """
    q_login = Login()
    qtbot.addWidget(q_login)
    return q_login

@pytest.fixture
def login2(qtbot):
    """
    Test Login
    """
    q_login = Login()
    qtbot.addWidget(q_login)
    return q_login


def test_login_label(login):
    assert login.windowTitle() == "Logowanie"
    assert login.lbl_login.text() == "Login (e-mail):"
    assert login.lbl_passwd.text() == "Hasło:"


def test_login_buttons(login):
    assert login.btn_register.isVisible() is True
    assert login.buttonBox.isVisible() is True


def test_login_edit(login):
    assert login.edit_login.text() == ''
    assert login.edit_passwd.text() == ''
    assert login.edit_passwd.echoMode() is QLineEdit.EchoMode.Password
