from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl
import sys


class ApiGet:

    def __init__(self):

        self.nam = QtNetwork.QNetworkAccessManager()
        self.do_request()

    def do_request(self):

        url = 'https://localhost:44340/api/users'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.nam.finished.connect(self.handle_response)
        self.nam.get(req)

    @staticmethod
    def handle_response(reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))

        else:
            print("Wykryto błąd: ", er)
            print(reply.errorString())

        QCoreApplication.quit()


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    ApiGet()
    sys.exit(app.exec_())
