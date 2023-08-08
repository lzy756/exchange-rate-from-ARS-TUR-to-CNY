# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 596)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(956, 596))
        Form.setMaximumSize(QtCore.QSize(956, 596))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.fromcomboBox = QtWidgets.QComboBox(Form)
        self.fromcomboBox.setGeometry(QtCore.QRect(130, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.fromcomboBox.setFont(font)
        self.fromcomboBox.setObjectName("fromcomboBox")
        self.fromcomboBox.addItem("")
        self.tocomboBox = QtWidgets.QComboBox(Form)
        self.tocomboBox.setGeometry(QtCore.QRect(360, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.tocomboBox.setFont(font)
        self.tocomboBox.setObjectName("tocomboBox")
        self.tocomboBox.addItem("")
        self.calbutton = QtWidgets.QPushButton(Form)
        self.calbutton.setGeometry(QtCore.QRect(270, 340, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.calbutton.setFont(font)
        self.calbutton.setObjectName("calbutton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(-2, -2, 960, 600))
        self.listView.setStyleSheet("background-image: url(:/3.jpg);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(74, 255, 240);\n"
"background-color: transparent;")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.changeButton = QtWidgets.QPushButton(Form)
        self.changeButton.setGeometry(QtCore.QRect(270, 200, 61, 51))
        self.changeButton.setStyleSheet("image: url(:/arrow.png);\n"
"background-color: transparent;")
        self.changeButton.setText("")
        self.changeButton.setObjectName("changeButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.outEdit = QtWidgets.QLineEdit(Form)
        self.outEdit.setGeometry(QtCore.QRect(360, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.outEdit.setFont(font)
        self.outEdit.setText("")
        self.outEdit.setReadOnly(True)
        self.outEdit.setObjectName("outEdit")
        self.historybuttom = QtWidgets.QPushButton(Form)
        self.historybuttom.setGeometry(QtCore.QRect(390, 380, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.historybuttom.setFont(font)
        self.historybuttom.setObjectName("historybuttom")
        self.hvEdit = QtWidgets.QLineEdit(Form)
        self.hvEdit.setGeometry(QtCore.QRect(250, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.hvEdit.setFont(font)
        self.hvEdit.setText("")
        self.hvEdit.setReadOnly(True)
        self.hvEdit.setObjectName("hvEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.chbEdit = QtWidgets.QLineEdit(Form)
        self.chbEdit.setGeometry(QtCore.QRect(40, 450, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.chbEdit.setFont(font)
        self.chbEdit.setText("")
        self.chbEdit.setObjectName("chbEdit")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.sellEdit = QtWidgets.QLineEdit(Form)
        self.sellEdit.setGeometry(QtCore.QRect(40, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.sellEdit.setFont(font)
        self.sellEdit.setText("")
        self.sellEdit.setObjectName("sellEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 500, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.sjEdit = QtWidgets.QLineEdit(Form)
        self.sjEdit.setGeometry(QtCore.QRect(230, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.sjEdit.setFont(font)
        self.sjEdit.setText("")
        self.sjEdit.setReadOnly(False)
        self.sjEdit.setObjectName("sjEdit")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(230, 500, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.blvEdit = QtWidgets.QLineEdit(Form)
        self.blvEdit.setGeometry(QtCore.QRect(230, 450, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.blvEdit.setFont(font)
        self.blvEdit.setText("")
        self.blvEdit.setReadOnly(True)
        self.blvEdit.setObjectName("blvEdit")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(230, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
"color: rgb(74, 255, 240);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.batbottom = QtWidgets.QPushButton(Form)
        self.batbottom.setGeometry(QtCore.QRect(390, 450, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.batbottom.setFont(font)
        self.batbottom.setObjectName("batbottom")
        self.favbottom = QtWidgets.QPushButton(Form)
        self.favbottom.setGeometry(QtCore.QRect(390, 540, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.favbottom.setFont(font)
        self.favbottom.setObjectName("favbottom")
        self.listView.raise_()
        self.fromcomboBox.raise_()
        self.tocomboBox.raise_()
        self.calbutton.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.changeButton.raise_()
        self.label_4.raise_()
        self.outEdit.raise_()
        self.historybuttom.raise_()
        self.hvEdit.raise_()
        self.label_5.raise_()
        self.chbEdit.raise_()
        self.label_6.raise_()
        self.sellEdit.raise_()
        self.label_7.raise_()
        self.sjEdit.raise_()
        self.label_8.raise_()
        self.blvEdit.raise_()
        self.label_9.raise_()
        self.batbottom.raise_()
        self.favbottom.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "exchange rate"))
        self.fromcomboBox.setItemText(0, _translate("Form", "请选择"))
        self.tocomboBox.setItemText(0, _translate("Form", "请选择"))
        self.calbutton.setText(_translate("Form", "计算"))
        self.label.setText(_translate("Form", "转换前货币量"))
        self.label_2.setText(_translate("Form", "转换后货币种类"))
        self.label_3.setText(_translate("Form", "转换前货币种类"))
        self.label_4.setText(_translate("Form", "转换后的结果"))
        self.historybuttom.setText(_translate("Form", "历史记录"))
        self.label_5.setText(_translate("Form", "当前汇率"))
        self.label_6.setText(_translate("Form", "成本"))
        self.label_7.setText(_translate("Form", "售价"))
        self.label_8.setText(_translate("Form", "实际收到"))
        self.label_9.setText(_translate("Form", "比率"))
        self.batbottom.setText(_translate("Form", "运行脚本设置代理"))
        self.favbottom.setText(_translate("Form", "饰品收藏列表"))
import picture_rc
