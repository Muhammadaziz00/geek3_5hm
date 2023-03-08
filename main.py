from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys

def push_botton():
    print("hello AZIZ")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Python PyQt5")
    window.setGeometry(400, 400, 400, 400)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World")
    main_text.move(150, 150)

    main_botton = QtWidgets.QPushButton(window)
    main_botton.setText("нажми")
    main_botton.move(135, 190)
    main_botton.clicked.connect(push_botton)


    window.show()
    sys.exit(app.exec_())
application()