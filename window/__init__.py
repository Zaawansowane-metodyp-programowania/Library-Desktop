URL = 'https://library-api-app.azurewebsites.net/api/'


def run_window(app=None):
    from window.login import Login
    import sys
    window = Login()
    dec = window.exec_()
    from PySide2 import QtWidgets
    if dec == QtWidgets.QDialog.Accepted:
        import json
        result = json.loads(window.response.text)
        print(json.dumps(result, indent=4, sort_keys=True))
        from window.main_window import MainWindow
        window = MainWindow(result)
        window.setContentsMargins(10, 10, 10, 10)
    elif dec == QtWidgets.QDialog.Rejected:
        sys.exit(0)
    sys.exit(app.exec_())