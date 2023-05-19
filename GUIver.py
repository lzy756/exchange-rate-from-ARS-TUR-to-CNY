import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pickle
import os

date = time.strftime('%Y%m%d', time.localtime(time.time()))
ratio = {}
money = ["TRY", "ARS", "CNY", "USD"]
directory = 'loadRatio'
filename = date + '_object.pkl'
filepath = os.path.join(directory, filename)

def getRate(kd1, kd2):
    # 请求URL并把结果用BeautifulSoup解析
        url = 'http://www.webmasterhome.cn/huilv/' + kd1 + '/' + kd1 + kd2 + '/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            rt = float(soup.select('#ExResult > div.exres > div.mexltop > span')[0].text)
            ratio[kd1 + kd2] = rt
        except ValueError:
            messagebox.showerror("错误", "获取汇率信息失败")
            dropdown.set(defname)
            dropdown1.set(defname1)
            return -1
        
# 创建目录（如果不存在）
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    with open(filepath, 'rb') as file:
        ratio = pickle.load(file)
except FileNotFoundError:
    for i in money:
        for j in money:
            if i != j:
                getRate(i, j)
    with open(filepath, 'wb') as file:
        pickle.dump(ratio, file)


def work(kd1, kd2, tsr1, tsr2):
    # if kd1 + kd2 in ratio.keys():
    rt = ratio[kd1 + kd2]
    # else:
    #     # 请求URL并把结果用BeautifulSoup解析
    #     url = 'http://www.webmasterhome.cn/huilv/' + kd1 + '/' + kd1 + kd2 + '/'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content, 'html.parser')

    #     try:
    #         rt = float(
    #             soup.select('#ExResult > div.exres > div.mexltop > span')
    #             [0].text)
    #         ratio[kd1 + kd2] = rt
    #     except ValueError:
    #         messagebox.showerror("错误", "获取汇率信息失败")
    #         dropdown.set(defname)
    #         dropdown1.set(defname1)
    #         return -1
    result_text.insert(tk.END,'现在' + tsr1 + '对' + tsr2 + '的汇率为：' + str(rt) + '\n')
    return rt


def calculate(event=None):
    try:
        a = float(input_field.get())
        result_text.insert(
            tk.END,
            input_field.get() + kd[0] + '兑换为' + opt[1] +
            '的结果为：{:.2f}'.format(a * rt) + kd[1] + '\n')
    except ValueError:
        messagebox.showerror("错误", "输入的不是数字")
    except NameError:
        messagebox.showerror("错误", "还未选择货币单位")


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
        return
    if kd[0] != "" and kd[1] != "":
        rt = work(*kd, opt[0], opt[1])


def clear_Text():
    result_text.delete("1.0", tk.END)


root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")
style.configure('TCombobox')

root.resizable(0, 0)
root.title("exchange rate")
root.geometry('650x399')
# 加载背景图片
image = tk.PhotoImage(file="1.png")

# 创建一个标签并将背景图片设置为标签的图像
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#currency_var = tk.StringVar()
#currency_var1 = tk.StringVar()
#currency_options = {"里拉": "0", "阿根廷比索": "1", "人民币": "2", "美元": "3"}
currency_options1 = ["里拉", "阿根廷比索", "人民币", "美元"]

defname = "转换前货币种类"
#currency_var.set(defname)
dropdown = ttk.Combobox(root,
                        values=currency_options1,
                        style='TCombobox',
                        width=15)
dropdown.bind("<<ComboboxSelected>>",
              lambda event: update_currency(dropdown.get(), 0))
dropdown.set(defname)
dropdown.grid(row=0, column=0, padx=5, pady=5)
'''currency_dropdown = tk.OptionMenu(
    root,
    currency_var,
    *currency_options.keys(),
    command=lambda option: update_currency(option, 0))
currency_dropdown.config(width=12)
currency_dropdown.grid(row=0, column=0, padx=5, pady=5)'''

defname1 = "转换后货币种类"
dropdown1 = ttk.Combobox(root,
                         values=currency_options1,
                         style='TCombobox',
                         width=15)
dropdown1.bind("<<ComboboxSelected>>",
               lambda event: update_currency(dropdown1.get(), 1))
dropdown1.set(defname1)
dropdown1.grid(row=0, column=2, padx=5, pady=5)
'''currency_var1.set(defname1)
currency_dropdown = tk.OptionMenu(
    root,
    currency_var1,
    *currency_options.keys(),
    command=lambda option: update_currency(option, 1))
currency_dropdown.config(width=12)
currency_dropdown.grid(row=0, column=2, padx=5, pady=5)'''

re_field = tk.Label(text="请输入转换的值：", fg="#39C5BB", anchor="e")
re_field.grid(row=1, column=0, sticky="e")

input_field = tk.Entry(root)
input_field.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.grid(row=2, column=1, padx=5, pady=5)

del_button = tk.Button(root, text="清除文本框", command=clear_Text)
del_button.grid(row=2, column=2, padx=5, pady=5, sticky='w')

result_text = tk.Text(root, height=20, width=37)  # 设置Text部件的高度和宽度
result_text.place(x=70, y=125)

# 创建滚动条并与 Text 部件关联
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.place(x=333, y=126, height=263)

# 将滚动条与 Text 部件进行关联
result_text.config(yscrollcommand=scrollbar.set)

input_field.bind("<Return>", calculate)

# 设置第3行的大小
#root.rowconfigure(3, weight=1)

root.mainloop()