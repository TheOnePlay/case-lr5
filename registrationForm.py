# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\registrationForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 423)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.emailEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailEdit.setObjectName("emailEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emailEdit)
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.passEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passEdit.setObjectName("passEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passEdit)
        self.Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.nameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.Label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.Label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.genderComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genderComboBox)
        self.Label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_5.sizePolicy().hasHeightForWidth())
        self.Label_5.setSizePolicy(sizePolicy)
        self.Label_5.setMaximumSize(QtCore.QSize(200, 100))
        self.Label_5.setWordWrap(True)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.rulesCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.rulesCheckBox.setObjectName("rulesCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rulesCheckBox)
        self.buttonsBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonsBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonsBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonsBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonsBox.setCenterButtons(True)
        self.buttonsBox.setObjectName("buttonsBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buttonsBox)

        self.retranslateUi(Dialog)
        self.buttonsBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonsBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация"))
        self.emailLabel.setText(_translate("Dialog", "Email"))
        self.Label.setText(_translate("Dialog", "Пароль"))
        self.Label_2.setText(_translate("Dialog", "Имя"))
        self.Label_3.setText(_translate("Dialog", "Дата рождения"))
        self.Label_4.setText(_translate("Dialog", "Пол"))
        self.genderComboBox.setItemText(0, _translate("Dialog", "Мужской"))
        self.genderComboBox.setItemText(1, _translate("Dialog", "Женский"))
        self.Label_5.setText(_translate("Dialog", "Продолжая, вы соглашаетесь с условиями Пользовательского соглашения и Соглашения о конфиденциальности"))
