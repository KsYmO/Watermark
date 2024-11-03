# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background: rgb(34,193,195);\n"
"background: linear-gradient(42deg, rgba(34,193,195,1) 0%, rgba(253,187,45,1) 100%);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 140, 521, 321))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20%;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_name = QtWidgets.QLabel(parent=self.frame)
        self.label_name.setGeometry(QtCore.QRect(20, 10, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik Black")
        font.setPointSize(18)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.path_choose = QtWidgets.QToolButton(parent=self.frame)
        self.path_choose.setGeometry(QtCore.QRect(230, 170, 141, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_choose.sizePolicy().hasHeightForWidth())
        self.path_choose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setKerning(True)
        self.path_choose.setFont(font)
        self.path_choose.setStyleSheet("border-radius: 15% 10%;\n"
"background-color: #fdbb2d")
        self.path_choose.setObjectName("path_choose")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.radioButton_img = QtWidgets.QRadioButton(parent=self.frame)
        self.radioButton_img.setGeometry(QtCore.QRect(30, 110, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.radioButton_img.setFont(font)
        self.radioButton_img.setObjectName("radioButton_img")
        self.img_choose = QtWidgets.QToolButton(parent=self.frame)
        self.img_choose.setGeometry(QtCore.QRect(180, 110, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.img_choose.setFont(font)
        self.img_choose.setStyleSheet("border-radius: 15% 10%;\n"
"background-color: #fdbb2d")
        self.img_choose.setObjectName("img_choose")
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
        self.textEdit.setGeometry(QtCore.QRect(120, 80, 104, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.textEdit.setStyleSheet("border-radius: 15% 10%;\n"
"background-color: #fdbb2d")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.radioButton_text = QtWidgets.QRadioButton(parent=self.frame)
        self.radioButton_text.setGeometry(QtCore.QRect(30, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.radioButton_text.setFont(font)
        self.radioButton_text.setObjectName("radioButton_text")
        self.create_btn = QtWidgets.QPushButton(parent=self.frame)
        self.create_btn.setGeometry(QtCore.QRect(210, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.create_btn.setFont(font)
        self.create_btn.setStyleSheet("border-radius: 15% 10%;\n"
"background-color: #fdbb2d")
        self.create_btn.setObjectName("create_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WM Paster"))
        self.label_name.setText(_translate("MainWindow", "Выберите тип водяного знака и файл"))
        self.path_choose.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Путь к изображению:"))
        self.radioButton_img.setText(_translate("MainWindow", "Изображение:"))
        self.img_choose.setText(_translate("MainWindow", "..."))
        self.radioButton_text.setText(_translate("MainWindow", "Текст:"))
        self.create_btn.setText(_translate("MainWindow", "Создать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
