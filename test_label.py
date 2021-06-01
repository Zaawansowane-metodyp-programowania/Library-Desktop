import pytest
from PySide2.QtWidgets import QLabel


@pytest.fixture
def label(qtbot):
    """
    Test QLabel. W atrybucie musi być qtbot. Funkcja musi zwracać obiekt sprawdzany.
    """
    q_label = QLabel()
    q_label.setText("Hello World")
    qtbot.addWidget(q_label)
    return q_label


def test_label(label):
    assert label.text() == "Hello World"
