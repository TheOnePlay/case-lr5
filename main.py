from PyQt5 import QtWidgets
from registrationForm import Ui_Dialog


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonsBox.accepted.connect(self.handle_apply)

    def handle_apply(self):
        user_data = {
            "email": self.ui.emailEdit.text(),
            "password": self.ui.passEdit.text(),
            "name": self.ui.nameEdit.text(),
            "date_of_birth": self.ui.dateEdit.text(),
            "gender": self.ui.genderComboBox.currentText()
        }
        user_info = f"""
        Ваши данные:
        Email:\t{user_data['email']}
        Пароль:\t\t{user_data['password']}
        Имя:\t\t{user_data['name']}
        Дата рождения:\t{user_data['date_of_birth']}
        Пол:\t\t{user_data['gender']}
        """

        QtWidgets.QMessageBox.information(self, "Успешная регистрация", user_info)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
