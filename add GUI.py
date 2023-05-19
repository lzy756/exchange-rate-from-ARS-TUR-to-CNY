import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def work(kd1, kd2, tsr1, tsr2):
    # 请求URL并把结果用BeautifulSoup解析
    url = 'http://www.webmasterhome.cn/huilv/' + kd1 + '/' + kd1 + kd2 + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        rt = float(
            soup.select('#ExResult > div.exres > div.mexltop > span')[0].text)
    except ValueError:
        messagebox.showerror("错误", "获取汇率信息失败")
        currency_var.set(defname)
        currency_var1.set(defname)
        return -1
    result_text.insert(tk.END,
                       '现在' + tsr1 + '对' + tsr2 + '的汇率为：' + str(rt) + '\n')
    return rt


def calculate(event=None):
    try:
        a = float(input_field.get())
        result_text.insert(
            tk.END,
            input_field.get() + kd[0] + '兑换为' + currency_var1.get() +
            '的结果为：{:.2f}'.format(a * rt) + kd[1] + '\n')
    except ValueError:
        messagebox.showerror("错误", "输入的不是数字")


kd = ["", ""]


def update_currency(option, num):
    global rt
    global kd
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
        rt = work(*kd, currency_var.get(), currency_var1.get())


root = tk.Tk()

root.title("exchange rate")
root.geometry('600x400')
currency_var = tk.StringVar()
currency_var1 = tk.StringVar()
currency_options = {"里拉": "0", "阿根廷比索": "1", "人民币": "2", "美元": "3"}

defname = "请选择转换前货币种类"
currency_var.set(defname)
currency_dropdown = tk.OptionMenu(
    root,
    currency_var,
    *currency_options.keys(),
    command=lambda option: update_currency(option, 0))
currency_dropdown.config(width=15)
currency_dropdown.grid(row=0, column=0, padx=5, pady=5)

currency_var1.set(defname)
currency_dropdown = tk.OptionMenu(
    root,
    currency_var1,
    *currency_options.keys(),
    command=lambda option: update_currency(option, 1))
currency_dropdown.config(width=15)
currency_dropdown.grid(row=0, column=2, padx=5, pady=5)

input_field = tk.Entry(root)
input_field.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.grid(row=2, column=1, padx=5, pady=5)

result_text = tk.Text(root, height=15, width=50)  # 设置Text部件的高度和宽度
result_text.place(x=60, y=125)

input_field.bind("<Return>", calculate)

# 设置第3行的大小
#root.rowconfigure(3, weight=1)

root.mainloop()
