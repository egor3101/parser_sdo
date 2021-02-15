from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def launch_GUI(value_of_check_data):
    Form, Window = uic.loadUiType("table.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    if value_of_check_data == False:
        form.label_2.setText('Ваши отметки не изменены')
    else:
        form.label_2.setText('Ваши отметки изменены.Проверьте,пожалуйста,сайт')

    app.exec()
