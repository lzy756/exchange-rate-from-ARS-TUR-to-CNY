import requests
from bs4 import BeautifulSoup

ratio = {}


def work(kd, kd1, tsr, tsr1):
    if kd + kd1 in ratio.keys():
        rt = ratio[kd + kd1]
    else:
        # 请求URL并把结果用BeautifulSoup解析
        url = 'http://www.webmasterhome.cn/huilv/' + kd + '/' + kd + kd1 + '/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        rt = float(
            soup.select('#ExResult > div.exres > div.mexltop > span')[0].text)

        ratio[kd + kd1] = rt

    print('现在' + tsr + '对' + tsr1 + '的汇率为：' + str(rt))
    print("输入\'back\'返回货币种类选择，输入\'exit\'退出程序")

    while True:
        a = input("输入需要转换的值（单位：" + kd + "）\n")
        if a == "back":
            return 0
        elif a == "exit":
            return -1
        try:
            print(a + kd + '兑换为' + tsr1 + '结果为：{:.2f}'.format(float(a) * rt) +
                  kd1)
        except ValueError:
            print('输入错误，请重新输入')
            continue


res = 0
while res == 0:
    kd = input("选择源货币种类(0：里拉，1：阿根廷比索,2：美元，3：人民币)\n")
    if kd == "0":
        kd = "TRY"
        tsr = "里拉"
    elif kd == "1":
        kd = "ARS"
        tsr = "阿根廷比索"
    elif kd == "2":
        kd = "USD"
        tsr = "美元"
    elif kd == "3":
        kd = "CNY"
        tsr = "人民币"

    kd1 = input("选择目的货币种类(0：里拉，1：阿根廷比索,2：美元，3：人民币)\n")
    if kd1 == "0":
        kd1 = "TRY"
        tsr1 = "里拉"
    elif kd1 == "1":
        kd1 = "ARS"
        tsr1 = "阿根廷比索"
    elif kd1 == "2":
        kd1 = "USD"
        tsr1 = "美元"
    elif kd1 == "3":
        kd1 = "CNY"
        tsr1 = "人民币"

    res = work(kd, kd1, tsr, tsr1)
    if res == -1:
        break

input("Press Enter to continue...")
