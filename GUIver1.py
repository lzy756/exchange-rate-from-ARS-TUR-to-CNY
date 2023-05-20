# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
#导入designer工具生成的login模块
from GUI import Ui_Form
import os
from PyQt5 import QtCore
import json
import requests
from bs4 import BeautifulSoup
import time

money = ["TRY", "ARS", "CNY", "USD"]
currency_options = ["里拉", "阿根廷比索", "人民币", "美元"]
directory = 'loadRatio'
filename = 'exchange rate.json'
filepath = os.path.join(directory, filename)


def get_current_timestamp():
    return int(time.time())


def on_closing():
    with open(filepath, 'w') as file:
        json.dump(ratio, file)


def getRate(kd1, kd2):
    # 请求URL并把结果用BeautifulSoup解析
    if kd1 == kd2:
        ratio[kd1 + kd2]["rate"] = 1.0
        ratio[kd1 + kd2]["timestamp"] = get_current_timestamp()
        return 0
    try:
        url = 'https://www.waihui999.com/{0}{1}/#100'.format(
            kd1.lower(), kd2.lower())
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
    except requests.exceptions.ProxyError:
        myWin.showwarning("请关闭代理软件再次尝试")
        return -1
    except requests.exceptions.ConnectionError:
        myWin.showerror("没有正常的网络连接无法正常使用")
    try:
        rt = float(
            soup.select(
                'body > div.wrapper > div.container > div > div.mod-panel > div.ft > table:nth-child(1) > tbody > tr > td:nth-child(2)'
            )[0].text)
        ratio[kd1 + kd2]["rate"] = rt
        ratio[kd1 + kd2]["timestamp"] = get_current_timestamp()
    except ValueError:
        myWin.showerror("解析html文件获取汇率信息失败")
        myWin.fromcomboBox.setCurrentText("请选择")
        myWin.tocomboBox.setCurrentText("请选择")
        return -1


# 创建目录（如果不存在）
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    with open(filepath, 'rb') as file:
        ratio = json.load(file)
except FileNotFoundError:
    ratio = {}


def remindtext(mes):
    myWin.showinfo(mes)


def work(kd1, kd2, tsr1, tsr2):
    current_timestamp = get_current_timestamp()
    one_hour_ago = current_timestamp - 3600
    if kd1 + kd2 in ratio.keys():
        if "timestamp" not in ratio[kd1 + kd2].keys() or ratio[
                kd1 + kd2]["timestamp"] < one_hour_ago:
            ratio[kd1 + kd2] = {}
            remindtext("本地汇率信息损坏或过期超过1小时，重新获取在线汇率中，请稍等......")
            if getRate(kd1, kd2) == -1:
                return -1
    else:
        ratio.setdefault(kd1 + kd2, {})
        remindtext("本地汇率信息不存在，重新获取在线汇率中，请稍等......")
        if getRate(kd1, kd2) == -1:
            return -1
    if "rate" not in ratio[kd1 + kd2].keys():
        remindtext("本地汇率信息损坏，重新获取在线汇率中，请稍等......")
        if getRate(kd1, kd2) == -1:
            return -1
    rt = ratio[kd1 + kd2]["rate"]
    myWin.showtextBrowser.append('现在' + tsr1 + '对' + tsr2 + '的汇率为：' + str(rt))
    return rt


def calculate():
    if rt == 0:
        getRate(kd[0], kd[1])
        remindtext("汇率信息获取错误，重新获取在线汇率中，请稍等......")
    try:
        a = float(myWin.lineEdit.text())
        myWin.showtextBrowser.append(myWin.lineEdit.text() + kd[0] + '兑换为' +
                                     opt[1] + '的结果为：{:.2f}'.format(a * rt) +
                                     kd[1])
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
        self.clearButton.clicked.connect(self.clear_text)

    def closeEvent(self, event):
        on_closing()
        event.accept()

    def showerror(self, mes):
        QMessageBox.critical(self, "错误", mes, QMessageBox.Ok)

    def showwarning(self, mes):
        QMessageBox.warning(self, "警告", mes, QMessageBox.Ok)

    def showinfo(self, mes):
        QMessageBox.information(self, "信息", mes, QMessageBox.Ok)

    def clear_text(self):
        self.showtextBrowser.clear()


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())