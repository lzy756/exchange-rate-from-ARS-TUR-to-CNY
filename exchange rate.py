import requests
from bs4 import BeautifulSoup

def work(kd,tsr):
    # 请求URL并把结果用BeautifulSoup解析
    url = 'http://www.webmasterhome.cn/huilv/CNY/CNY'+kd+'/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rt=float(soup.select('#ExResult > div.exres > div.mexltop > span')[0].text)

    print('现在人民币对'+tsr+'的汇率为：'+str(rt))
    print("输入\'back\'返回货币种类选择，输入\'exit\'退出程序")

    while True:    
        a=input("输入需要转换的值（单位："+kd+"）\n")
        if a=="back":
            return 1
        elif a=="exit":
            return -1
        try:
            a=float(a)
            print('兑换结果为：{:.2f}'.format(a/rt))    
        except ValueError:
            print('输入错误，请重新输入')
            continue

res=0
while res==0:
    kd=input("选择货币种类(0：里拉，1：阿根廷比索)\n")
    if kd=="0":
        kd="TRY"
        tsr="里拉"
    else:
        kd="ARS"
        tsr="阿根廷比索"

    res=work(kd,tsr)
    if res==-1:
        break
    else:
        res=0

input("Press Enter to continue...")
