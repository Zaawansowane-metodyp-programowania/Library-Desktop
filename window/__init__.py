URL = 'https://library-api-app.azurewebsites.net/api/'


def run_window(app=None):
    from window.login import Login
    from window.main_window import MainWindow
    from PySide2 import QtWidgets
    import json
    import sys

    window = Login()
    dec = window.exec_()
    if dec == QtWidgets.QDialog.Accepted:
        result = json.loads(window.response.text)
        print(result)
        window = MainWindow(result)
        window.setContentsMargins(10, 10, 10, 10)
    elif dec == QtWidgets.QDialog.Rejected:
        sys.exit(0)

    app.exec_()
