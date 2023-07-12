# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, Qt
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTextBrowser, QDialog, QListWidgetItem
#导入designer工具生成的login模块
from GUI import Ui_Form
from GUI2 import Ui_secondForm
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import json
import requests
from GUI3 import Ui_decform
from GUI4 import Ui_AddDialog
from GUI5 import Ui_InfoDialog
import time
import subprocess
from Gprice import Fprice, Getname
import re

money = ["TRY", "ARS", "CNY", "USD"]
currency_options = ["里拉", "阿根廷比索", "人民币", "美元"]
directory = 'loadRatio'


def get_current_timestamp():
    return int(time.time())


class PortError(Exception):
    pass


def getRate():
    global kd
    # 请求API数据获得json数据文件
    try:
        res = {}
        if port == -1:
            raise PortError
        rcode = Fprice(res, port)
        res['timestamp'] = get_current_timestamp()
    except PortError:
        myWin.showwarning("请运行脚本获取本地代理端口后重试")
        kd[0] = ""
        kd[1] = ""
        myWin.fromcomboBox.setCurrentText("请选择")
        myWin.tocomboBox.setCurrentText("请选择")
        return -1
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
    #print(res)
    if rcode == -1:
        myWin.showerror("请求失败，请稍后重试或者更换代理IP")
        return -1
    return res


# 创建目录（如果不存在）
if not os.path.exists(directory):
    os.makedirs(directory)

os.makedirs("data", exist_ok=True)

ratio = {}


def remindtext(mes):
    myWin.showinfo(mes)


def on_closing():
    filename = 'Gprice.json'
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                pre_tstamp = json.load(f)['timestamp']
            if type(ratio) == dict and "timestamp" in ratio.keys(
            ) and ratio["timestamp"] > pre_tstamp:
                with open(filepath, 'w') as file:
                    json.dump(ratio, file)
        except TypeError:
            with open(filepath, 'w') as file:
                json.dump(ratio, file)
        except KeyError:
            with open(filepath, 'w') as file:
                json.dump(ratio, file)
    else:
        if ratio != -1:
            with open(filepath, 'w') as file:
                json.dump(ratio, file)
    with open(os.path.join("data", "items_data.csv"), "w",
              encoding='utf-8') as file:
        # 遍历 QListWidget 中的每个 item
        for row in range(decWin.itemList.count()):
            item = decWin.itemList.item(row)
            steamitem = item.data(1)
            # 将饰品信息以逗号分隔的形式写入文件
            line = f"{steamitem.name},{steamitem.inprice},{steamitem.outprice},{steamitem.currency},{steamitem.url}\n"
            file.write(line)
    secondWin.close()
    decWin.close()


def noinfowork(kd1, kd2):
    global ratio
    filename = 'Gprice.json'
    filepath = os.path.join(directory, filename)
    try:
        if ratio == -1 or kd1 not in ratio.keys() or kd2 not in ratio.keys():
            with open(filepath, 'r') as f:
                ratio = json.load(f)
    except FileNotFoundError:
        remindtext("本地数据不存在，获取steam价格中，请稍等......")
        ratio = getRate()
        if ratio == -1:
            myWin.showerror("获取steam价格失败，请重试")
            return -1
    if ratio == -1:
        remindtext("本地数据损坏，获取steam价格中，请稍等......")
        ratio = getRate()
        if ratio == -1:
            return -1
    if (kd1 not in ratio.keys()) or (kd2 not in ratio.keys()):
        remindtext("本地数据损坏，获取steam价格中，请稍等......")
        ratio = getRate()
        if ratio == -1:
            return -1
    if "timestamp" not in ratio.keys():
        remindtext("本地数据损坏，获取steam价格中，请稍等......")
        ratio = getRate()
        if ratio == -1:
            return -1
    if ratio['timestamp'] <= get_current_timestamp() - 6 * 60 * 60:
        remindtext("本地数据过时超过6小时，重新获取steam价格中，请稍等......")
        ratio = getRate()
        if ratio == -1:
            return -1
    pr1 = ratio[kd1]
    pr2 = ratio[kd2]
    return pr2 / pr1


def work(kd1, kd2, tsr1, tsr2):
    rt = noinfowork(kd1, kd2)
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
    global opt
    try:
        if rt == 0 or rt == -1:
            if kd[0] not in money or kd[1] not in money:
                raise NameError
            remindtext("汇率信息获取错误，重新获取汇率中，请稍等......")
            rt = work(kd[0], kd[1], opt[0], opt[1])
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


def showdec():
    if (not decWin.isVisible()):
        decWin.move(myWin.geometry().right() - 200,
                    myWin.geometry().top() + 200)
        decWin.show()
    else:
        decWin.close()


def textchange():
    a = myWin.chbEdit.text()
    b = myWin.sellEdit.text()
    c = myWin.sjEdit.text()
    myWin.blvEdit.setText("")
    myWin.sjEdit.textChanged.disconnect(textchange)
    myWin.sellEdit.textChanged.disconnect(textchange)
    try:
        sender = myWin.sender()
        if sender == myWin.chbEdit:
            c = float(c)
            a = float(a)
            d = a / c
            myWin.blvEdit.setText('{:.6f}'.format(d))
        if sender == myWin.sellEdit:
            if b != "":
                b = float(b)
                c = b * 0.87
                myWin.sjEdit.setText('{:.6f}'.format(c))
                a = float(a)
                d = a / c
                myWin.blvEdit.setText('{:.6f}'.format(d))
            else:
                myWin.sjEdit.setText('')
        if sender == myWin.sjEdit:
            if c != "":
                c = float(c)
                b = c / 0.87
                myWin.sellEdit.setText('{:.6f}'.format(b))
                a = float(a)
                d = a / c
                myWin.blvEdit.setText('{:.6f}'.format(d))
            else:
                myWin.sellEdit.setText('')
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    myWin.sjEdit.textChanged.connect(textchange)
    myWin.sellEdit.textChanged.connect(textchange)


def SetProxy():
    result = subprocess.run("修改代理设置.bat", shell=True)
    if result.returncode == 0:
        remindtext("代理修改成功")
    else:
        myWin.showerror("代理设置失败")


class steamItem:

    def __init__(self, name, inprice, outprice, currency, URL):
        self.name = name
        self.inprice = inprice
        self.outprice = outprice
        self.currency = currency
        self.url = URL


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
        self.favbottom.clicked.connect(showdec)
        self.showtextBrowser = QTextBrowser(self)
        self.showtextBrowser.setHidden(True)
        self.sjEdit.textChanged.connect(textchange)
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


def cussort(item1, item2):
    return item1.data(Qt.UserRole) - item2.data(Qt.UserRole)


class ItemListWindow(QMainWindow, Ui_decform):

    def __init__(self, parent=None):
        super(ItemListWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadItemsFromFile()
        self.sumButton.clicked.connect(self.sumup)
        self.addButton.clicked.connect(self.openAddItemWindow)
        self.deleteButton.clicked.connect(self.deleteSelectedItem)
        self.detailsButton.clicked.connect(self.showItemDetails)
        self.editButton.clicked.connect(self.editSelectedItem)
        self.itemList.itemDoubleClicked.connect(self.openItemURL)
        self.sortButton.clicked.connect(self.sortlist)

    def showerror(self, mes):
        QMessageBox.critical(self, "错误", mes, QMessageBox.Ok)

    def showwarning(self, mes):
        QMessageBox.warning(self, "警告", mes, QMessageBox.Ok)

    def showinfo(self, mes):
        QMessageBox.information(self, "信息", mes, QMessageBox.Ok)

    def sortlist(self):
        for i in range(self.itemList.count()):
            item = self.itemList.item(i)
            # 设置自定义排序键，这里以项的长度为例
            outprice=item.data(1).outprice
        #    if item.data(1).currency!='人民币':
        #        outprice=noinfowork(money[currency_options.index(item.data(1).currency)],'CNY')*outprice
        #    if outprice < 0:
        #        self.showwarning('获取steam汇价失败，请稍后重试')
        #        return -1
            item.setData(Qt.UserRole, outprice)
        self.itemList.sortItems(Qt.AscendingOrder)

    def sumup(self):
        sumin = 0
        sumout = 0
        for i in range(self.itemList.count()):
            item = self.itemList.item(i).data(1)
            tin = item.inprice
            tout = item.outprice
            if item.currency != '人民币':
                fmon = money[currency_options.index(item.currency)]
                rt = noinfowork(fmon, 'CNY')
                if rt == -1:
                    self.showwarning("获取steam汇价失败，请稍后重试")
                    return -1
                else:
                    tin = tin * rt
                    tout = tout * rt
            sumin += tin
            sumout += tout
        infwin = ItemInfoWindow(self)
        infwin.curtypelabel.setText('统计用的货币类型为人民币')
        infwin.getinlabel.setText('收藏的饰品总进价为:' + str(round(sumin, 6)))
        infwin.selloutlabel.setText('收藏饰品的总售价为:' + str(round(sumout, 6)))
        infwin.ratiolabel.setText('收藏饰品的总比率为:' +
                                  str(round(sumin / (sumout * 0.87), 6)))
        infwin.show()

    def loadItemsFromFile(self):
        try:
            # 从本地文件中读取数据，例如使用 CSV、JSON 或其他格式
            with open(os.path.join("data", "items_data.csv"),
                      "r",
                      encoding='utf-8') as file:
                # 假设每行数据包含饰品的名称和相关信息，以逗号分隔
                for line in file:
                    item_data = line.strip().split(",")
                    if len(item_data) >= 5:
                        name = item_data[0]
                        inprice = float(item_data[1])
                        outprice = float(item_data[2])
                        currency = item_data[3]
                        url = item_data[4]
                        steamitem = steamItem(name, inprice, outprice,
                                              currency, url)

                        item = QListWidgetItem()
                        item.setText(name)
                        item.setData(1, steamitem)

                        self.itemList.addItem(item)

        except FileNotFoundError:
            # 文件不存在时的处理
            pass

    def openAddItemWindow(self):
        #打开添加界面
        additemwin = ItemAddWindow(self)
        if additemwin.exec_() == QDialog.Accepted:
            # 创建 QListWidgetItem
            item = QListWidgetItem()
            # 设置 QListWidgetItem 的文本为饰品的名称
            item.setText(additemwin.name)
            # 将完整的 SteamItem 对象保存在 QListWidgetItem 的数据中
            steamitem = steamItem(additemwin.name, additemwin.inprice,
                                  additemwin.outprice, additemwin.currency,
                                  additemwin.url)
            item.setData(1, steamitem)
            # 添加 QListWidgetItem 到 QListWidget
            existing_items = self.itemList.findItems(item.text(),
                                                     Qt.MatchExactly)
            if not existing_items:
                self.itemList.addItem(item)
            else:
                self.showinfo("该物品已经存在于收藏夹中")

    def deleteSelectedItem(self):
        selectedItems = self.itemList.selectedItems()
        for item in selectedItems:
            self.itemList.takeItem(self.itemList.row(item))

    def showItemDetails(self):
        selectedItems = self.itemList.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0].data(1)
            # 在这里显示选中饰品的详细信息，可以使用QMessageBox、QDialog等组件
            iteminfowin = ItemInfoWindow(self)
            iteminfowin.curtypelabel.setText('这件货品记录价格的货币类型为:' +
                                             selectedItem.currency)
            iteminfowin.getinlabel.setText('这件货品记录的进价为:' +
                                           str(round(selectedItem.inprice, 6)))
            iteminfowin.selloutlabel.setText(
                '这件货品记录的售价为:' + str(round(selectedItem.outprice, 6)))
            iteminfowin.ratiolabel.setText('预计的比率为' + str(
                round(selectedItem.inprice /
                      (selectedItem.outprice * 0.87), 6)))
            iteminfowin.show()

    def editSelectedItem(self):
        selectedItems = self.itemList.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0].data(1)
            editwin = ItemAddWindow(self)
            editwin.URLEdit.setText(selectedItem.url)
            editwin.getinEdit.setText(str(selectedItem.inprice))
            editwin.selloutEdit.setText(str(selectedItem.outprice))
            editwin.curtypecomboBox.setCurrentText(selectedItem.currency)

            if editwin.exec_() == QDialog.Accepted:
                selectedItem.name = editwin.name
                selectedItem.inprice = editwin.inprice
                selectedItem.outprice = editwin.outprice
                selectedItem.currency = editwin.currency
                selectedItem.url = editwin.url
                selectedItems[0].setText(editwin.name)
                selectedItems[0].setData(1, selectedItem)

    def openItemURL(self, item):
        if item:
            url = QUrl(item.data(1).url)
            QDesktopServices.openUrl(url)


class ItemAddWindow(QDialog, Ui_AddDialog):

    def __init__(self, parent=None):
        super(ItemAddWindow, self).__init__(parent)
        self.setupUi(self)
        self.addButton.clicked.connect(self.addItem)
        self.cancelButton.clicked.connect(self.reject)
        self.curtypecomboBox.addItems(currency_options)
        self.URLEdit.textChanged.connect(self.exgetin)

    def exgetin(self):
        patten = r'buffPrice=([.\d]+)'
        matches = re.findall(patten, self.URLEdit.text())
        if matches:
            self.getinEdit.setText(matches[0])

    def check(self, url, currency, inprice, outprice):
        if currency not in currency_options:
            self.showerror("未选择货币单位！")
            return False
        try:
            self.inprice = float(inprice)
        except ValueError:
            self.showerror("输入的进价不是数字！")
            return False
        try:
            self.outprice = float(outprice)
        except ValueError:
            self.showerror("输入的售价不是数字！")
            return False
        return True

    def addItem(self):
        #检查数据正确性并返回
        self.url = self.URLEdit.text()
        self.currency = self.curtypecomboBox.currentText()
        self.inprice = self.getinEdit.text()
        self.outprice = self.selloutEdit.text()
        if self.check(self.url, self.currency, self.inprice,
                      self.outprice) == True:
            if port == -1:
                self.showwarning("请运行脚本获取本地代理端口后重试")
            else:
                self.name = Getname(self.url, port)
                if self.name == None:
                    self.showerror("获取饰品名字失败，请检查url正确性，如果url没有错误，请稍后再试（网络问题）")
                else:
                    self.accept()

    def showerror(self, mes):
        QMessageBox.critical(self, "错误", mes, QMessageBox.Ok)

    def showwarning(self, mes):
        QMessageBox.warning(self, "警告", mes, QMessageBox.Ok)

    def showinfo(self, mes):
        QMessageBox.information(self, "信息", mes, QMessageBox.Ok)


class ItemInfoWindow(QDialog, Ui_InfoDialog):

    def __init__(self, parent=None):
        super(ItemInfoWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    result = subprocess.run("修改代理设置.bat", shell=True)
    try:
        with open('port.txt', 'r') as f:
            port = int(f.readline())
    except FileNotFoundError:
        port = -1
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    secondWin = MyMainForm1(myWin)
    decWin = ItemListWindow(myWin)
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())