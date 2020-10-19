# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from movablewidget import movableWidget
import windowButton
import windowButton_hover


class Ui_mainFrame(object):
    def setupUi(self, mainFrame):
        mainFrame.setObjectName("mainFrame")
        mainFrame.resize(283, 522)
        mainFrame.setMinimumSize(QtCore.QSize(250, 500))
        mainFrame.setBaseSize(QtCore.QSize(0, 0))
        mainFrame.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main = QtWidgets.QFrame(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMinimumSize(QtCore.QSize(250, 500))
        self.main.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main.setFont(font)
        self.main.setStyleSheet("background-color: rgb(255, 230, 153);\n"
"border-radius: 30px;")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.gridLayout = QtWidgets.QGridLayout(self.main)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.titleFrame = movableWidget(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy)
        self.titleFrame.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-top-right-radius: 20px;\n"
"border-top-left-radius: 20px;")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(99999, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.close = QtWidgets.QPushButton(self.titleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setMinimumSize(QtCore.QSize(20, 20))
        self.close.setMaximumSize(QtCore.QSize(20, 20))
        self.close.setStyleSheet("QPushButton{\n"
"border-image: url(:/source/close.PNG);\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/source_hover/close_hover.png);\n"
"}\n")
        d = QtWidgets.QWidget()
        self.close.clicked.connect(d.close)
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/close.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.gridLayout.addWidget(self.titleFrame, 0, 0, 1, 2)
        self.locationInput = QtWidgets.QLineEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationInput.sizePolicy().hasHeightForWidth())
        self.locationInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.locationInput.setFont(font)
        self.locationInput.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.locationInput.setText("")
        self.locationInput.setAlignment(QtCore.Qt.AlignCenter)
        self.locationInput.setObjectName("locationInput")
        self.gridLayout.addWidget(self.locationInput, 6, 1, 1, 1)
        self.idCheck = QtWidgets.QPushButton(self.main)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idCheck.setFont(font)
        self.idCheck.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 230, 153);\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(197, 197, 197);\n"
"border-radius: 0px;\n"
"}")
        self.idCheck.setObjectName("idCheck")
        self.gridLayout.addWidget(self.idCheck, 3, 0, 1, 2)
        self.emailInput = QtWidgets.QLineEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailInput.sizePolicy().hasHeightForWidth())
        self.emailInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.emailInput.setFont(font)
        self.emailInput.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.emailInput.setText("")
        self.emailInput.setAlignment(QtCore.Qt.AlignCenter)
        self.emailInput.setObjectName("emailInput")
        self.gridLayout.addWidget(self.emailInput, 8, 1, 1, 1)
        self.idInput = QtWidgets.QLineEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idInput.sizePolicy().hasHeightForWidth())
        self.idInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idInput.setFont(font)
        self.idInput.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.idInput.setText("")
        self.idInput.setAlignment(QtCore.Qt.AlignCenter)
        self.idInput.setObjectName("idInput")
        self.gridLayout.addWidget(self.idInput, 2, 1, 1, 1)
        self.confirm = QtWidgets.QPushButton(self.main)
        self.confirm.setMinimumSize(QtCore.QSize(0, 30))
        self.confirm.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 230, 153);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(197, 197, 197);\n"
"border-radius: 15px;\n"
"}")
        self.confirm.setObjectName("confirm")
        self.gridLayout.addWidget(self.confirm, 9, 0, 1, 2)
        self.email = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 8, 0, 1, 1)
        self.password = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 4, 0, 1, 1)
        self.userDataTitle = QtWidgets.QLabel(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userDataTitle.sizePolicy().hasHeightForWidth())
        self.userDataTitle.setSizePolicy(sizePolicy)
        self.userDataTitle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userDataTitle.setFont(font)
        self.userDataTitle.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.userDataTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.userDataTitle.setObjectName("userDataTitle")
        self.gridLayout.addWidget(self.userDataTitle, 1, 0, 1, 2)
        self.location = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.location.setFont(font)
        self.location.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setObjectName("location")
        self.gridLayout.addWidget(self.location, 6, 0, 1, 1)
        self.id = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.id.setFont(font)
        self.id.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 2, 0, 1, 1)
        self.passwordInput = QtWidgets.QLineEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 0px;")
        self.passwordInput.setText("")
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")
        self.gridLayout.addWidget(self.passwordInput, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.main)

        self.retranslateUi(mainFrame)
        QtCore.QMetaObject.connectSlotsByName(mainFrame)

    def retranslateUi(self, mainFrame):
        _translate = QtCore.QCoreApplication.translate
        mainFrame.setWindowTitle(_translate("mainFrame", "Form"))
        self.idCheck.setText(_translate("mainFrame", "ID 중복확인"))
        self.confirm.setText(_translate("mainFrame", "확인"))
        self.email.setText(_translate("mainFrame", "이메일"))
        self.password.setText(_translate("mainFrame", "PW"))
        self.userDataTitle.setText(_translate("mainFrame", "회원정보 입력"))
        self.location.setText(_translate("mainFrame", " 거주지\n"
"(시/구)"))
        self.id.setText(_translate("mainFrame", "ID"))
