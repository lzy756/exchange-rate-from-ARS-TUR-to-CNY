# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondForm(object):
    def setupUi(self, secondForm):
        secondForm.setObjectName("secondForm")
        secondForm.resize(582, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        secondForm.setWindowIcon(icon)
        self.showtextBrowser = QtWidgets.QTextBrowser(secondForm)
        self.showtextBrowser.setGeometry(QtCore.QRect(0, 0, 511, 411))
        self.showtextBrowser.setStyleSheet("")
        self.showtextBrowser.setObjectName("showtextBrowser")
        self.clearButton = QtWidgets.QPushButton(secondForm)
        self.clearButton.setGeometry(QtCore.QRect(520, 130, 51, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")

        self.retranslateUi(secondForm)
        QtCore.QMetaObject.connectSlotsByName(secondForm)

    def retranslateUi(self, secondForm):
        _translate = QtCore.QCoreApplication.translate
        secondForm.setWindowTitle(_translate("secondForm", "历史查询记录"))
        self.showtextBrowser.setHtml(_translate("secondForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.clearButton.setText(_translate("secondForm", "清\n"
"空\n"
"文\n"
"本\n"
"框"))