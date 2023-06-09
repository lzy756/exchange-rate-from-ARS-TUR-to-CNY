# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTextBrowser
#导入designer工具生成的login模块
from GUI import Ui_Form
from GUI2 import Ui_secondForm
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import json
import requests
from bs4 import BeautifulSoup
import time
import subprocess
from fetch import fetchrate

money = ["TRY", "ARS", "CNY", "USD"]
currency_options = ["里拉", "阿根廷比索", "人民币", "美元"]
directory = 'loadRatio'
with open("currency.json", "r", encoding='utf-8') as f:
    currency_details = json.load(f)


def get_current_timestamp():
    return int(time.time())


def getRate(kd1, kd2):
    global kd
    # 请求API数据获得json数据文件
    try:
        time.sleep(3)
        kd1 = currency_details[kd1]["eCurrencyCode"]
        kd2 = currency_details[kd2]["eCurrencyCode"]
        FtoC1, CtoF1, timestamp1 = fetchrate(kd1)
        FtoC2, CtoF2, timestamp2 = fetchrate(kd2)
    except requests.exceptions.ProxyError:
        myWin.showwarning("请运行脚本设置代理后重试")
        kd[0] = ""
        kd[1] = ""
        myWin.fromcomboBox.setCurrentText("请选择")
        myWin.tocomboBox.setCurrentText("请选择")
        return -1
    except requests.exceptions.ConnectionError:
        myWin.showerror("没有正常的网络连接无法正常使用")
        kd[0] = ""
        kd[1] = ""
        myWin.fromcomboBox.setCurrentText("请选择")
        myWin.tocomboBox.setCurrentText("请选择")
        return -1
    if FtoC1 == -1 or FtoC2 == -1:
        myWin.showerror("获取在线汇率失败，请重试（不要过于频繁的尝试，多次失败建议等一会儿）")
        return -1
    if FtoC1 == -2 or FtoC2 == -2:
        remindtext("请先运行脚本配置代理")
    res = {"rate": CtoF2 / CtoF1, "timestamp": timestamp1}
    return res


# 创建目录（如果不存在）
if not os.path.exists(directory):
    os.makedirs(directory)

ratio = {}


def remindtext(mes):
    myWin.showinfo(mes)


def on_closing():
    for item in money:
        if item not in ratio.keys():
            continue
        filename = item + '.json'
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                tjson = json.load(file)
            for it in tjson.keys():
                if it not in ratio[item].keys():
                    ratio[item][it] = tjson[it]
        with open(filepath, 'w') as file:
            json.dump(ratio[item], file)
    secondWin.close()


def work(kd1, kd2, tsr1, tsr2):
    global ratio
    if kd1 not in ratio.keys():
        ratio[kd1] = {}
    if kd2 not in ratio[kd1].keys() or ratio[kd1][kd2] == -1:
        filename = kd1 + '.json'
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'rb') as file:
                dic = json.load(file)
                if kd2 not in dic.keys():
                    raise FileNotFoundError
                ratio[kd1][kd2] = dic[kd2]
                if ratio[kd1][kd2] == -1 or ratio[kd1][kd2] == None:
                    remindtext("本地汇率信息不存在，重新获取在线汇率中，请稍等......")
                    ratio[kd1][kd2] = getRate(kd1, kd2)
        except FileNotFoundError:
            remindtext("本地汇率信息不存在，重新获取在线汇率中，请稍等......")
            ratio[kd1][kd2] = getRate(kd1, kd2)
            if ratio[kd1][kd2] == -1:
                return -1
    current_timestamp = get_current_timestamp()
    if "timestamp" not in ratio[kd1][kd2].keys(
    ) or ratio[kd1][kd2]["timestamp"] <= current_timestamp - 24 * 60 * 60:
        remindtext("本地汇率信息损坏或过期超过一天，重新获取在线汇率中，请稍等......")
        ratio[kd1][kd2] = getRate(kd1, kd2)
        if ratio[kd1][kd2] == -1:
            return -1
    if "rate" not in ratio[kd1][kd2].keys():
        remindtext("本地汇率信息损坏，重新获取在线汇率中，请稍等......")
        ratio[kd1][kd2] = getRate(kd1, kd2)
        if ratio[kd1][kd2] == -1:
            return -1
    rt = ratio[kd1][kd2]["rate"]
    myWin.hvEdit.setText('{:f}'.format(rt))
    myWin.showtextBrowser.append('现在' + tsr1 + '对' + tsr2 +
                                 '的汇率为：{:f}'.format(rt))
    if (secondWin.isVisible()):
        secondWin.showtextBrowser.append('现在' + tsr1 + '对' + tsr2 +
                                         '的汇率为：{:f}'.format(rt))
    return rt


def calculate():
    global rt
    global kd
    try:
        if rt == 0 or rt == -1:
            if kd[0] not in money or kd[1] not in money:
                raise NameError
            remindtext("汇率信息获取错误，重新获取汇率中，请稍等......")
            rt = getRate(kd[0], kd[1])
            if rt == -1:
                return -1
            myWin.hvEdit.setText('{:f}'.format(rt))
        a = float(myWin.lineEdit.text())
        myWin.showtextBrowser.append(myWin.lineEdit.text() + kd[0] + '兑换为' +
                                     opt[1] + '的结果为：{:f}'.format(a * rt) +
                                     kd[1])
        if (secondWin.isVisible()):
            secondWin.showtextBrowser.append(myWin.lineEdit.text() + kd[0] +
                                             '兑换为' + opt[1] +
                                             '的结果为：{:f}'.format(a * rt) +
                                             kd[1])
        myWin.outEdit.setText('{:f}'.format(a * rt))
    except ValueError:
        myWin.showerror("输入的不是数字")
    except NameError:
        myWin.showerror("还未选择货币单位")


kd = ["", ""]
opt = ["", ""]


def update_currency(option, num):
    global rt
    global kd
    global opt
    rt = 0
    myWin.hvEdit.setText("")
    myWin.outEdit.setText("")
    opt[num] = option
    if option == "里拉":
        kd[num] = "TRY"
    elif option == "阿根廷比索":
        kd[num] = "ARS"
    elif option == "人民币":
        kd[num] = "CNY"
    elif option == "美元":
        kd[num] = "USD"
    else:
        kd[num] = ""

    if kd[0] in money and kd[1] in money:
        rt = work(*kd, opt[0], opt[1])


def update_2currency(option1, option2, num1, num2):
    global rt
    global kd
    global opt
    rt = 0
    myWin.hvEdit.setText("")
    myWin.outEdit.setText("")
    opt[num1] = option1
    if option1 == "里拉":
        kd[num1] = "TRY"
    elif option1 == "阿根廷比索":
        kd[num1] = "ARS"
    elif option1 == "人民币":
        kd[num1] = "CNY"
    elif option1 == "美元":
        kd[num1] = "USD"
    else:
        kd[num1] = ""

    opt[num2] = option2
    if option2 == "里拉":
        kd[num2] = "TRY"
    elif option2 == "阿根廷比索":
        kd[num2] = "ARS"
    elif option2 == "人民币":
        kd[num2] = "CNY"
    elif option2 == "美元":
        kd[num2] = "USD"
    else:
        kd[num2] = ""

    if kd[0] in money and kd[1] in money:
        rt = work(*kd, opt[0], opt[1])


def swap():
    value1 = myWin.fromcomboBox.currentText()
    value2 = myWin.tocomboBox.currentText()

    myWin.fromcomboBox.setCurrentText(value2)
    myWin.tocomboBox.setCurrentText(value1)
    update_2currency(value2, value1, 0, 1)


def showsec():
    if (not secondWin.isVisible()):
        secondWin.move(myWin.geometry().right() - 200, myWin.geometry().top())
        text = myWin.showtextBrowser.toPlainText()
        secondWin.showtextBrowser.setPlainText(text)
        secondWin.show()
    else:
        secondWin.close()


def textchange():
    a = myWin.chbEdit.text()
    b = myWin.sellEdit.text()
    print(a, b)
    myWin.sjEdit.setText("")
    myWin.blvEdit.setText("")
    try:
        if b != "":
            b = float(b)
            c = b * 0.87
            myWin.sjEdit.setText("{:.6f}".format(c))
            if a != "":
                a = float(a)
                d = a / c
                myWin.blvEdit.setText('{:.6f}'.format(d))
    except ValueError:
        pass


def SetProxy():
    result = subprocess.run("修改代理设置.bat", shell=True)
    if result.returncode == 0:
        remindtext("代理修改成功")
    else:
        myWin.showerror("代理设置失败")


class MyMainForm(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.fromcomboBox.addItems(currency_options)
        self.tocomboBox.addItems(currency_options)
        upd1 = lambda: update_currency(self.fromcomboBox.currentText(), num=0)
        self.fromcomboBox.activated[str].connect(upd1)
        self.lineEdit.returnPressed.connect(calculate)
        upd2 = lambda: update_currency(self.tocomboBox.currentText(), num=1)
        self.tocomboBox.activated[str].connect(upd2)
        self.calbutton.clicked.connect(calculate)
        self.changeButton.clicked.connect(swap)
        self.historybuttom.clicked.connect(showsec)
        self.showtextBrowser = QTextBrowser(self)
        self.showtextBrowser.setHidden(True)
        self.chbEdit.textChanged.connect(textchange)
        self.sellEdit.textChanged.connect(textchange)
        self.batbottom.clicked.connect(SetProxy)

    def closeEvent(self, event):
        on_closing()
        event.accept()

    def showerror(self, mes):
        QMessageBox.critical(self, "错误", mes, QMessageBox.Ok)

    def showwarning(self, mes):
        QMessageBox.warning(self, "警告", mes, QMessageBox.Ok)

    def showinfo(self, mes):
        QMessageBox.information(self, "信息", mes, QMessageBox.Ok)


class MyMainForm1(QMainWindow, Ui_secondForm):

    def __init__(self, parent=None):
        super(MyMainForm1, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clear_text)

    def showerror(self, mes):
        QMessageBox.critical(self, "错误", mes, QMessageBox.Ok)

    def showwarning(self, mes):
        QMessageBox.warning(self, "警告", mes, QMessageBox.Ok)

    def showinfo(self, mes):
        QMessageBox.information(self, "信息", mes, QMessageBox.Ok)

    def clear_text(self):
        self.showtextBrowser.clear()
        myWin.showtextBrowser.clear()


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    secondWin = MyMainForm1()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())