import requests
import json
import time
from bs4 import BeautifulSoup

CNYheader = {
    'Cookie':
    'steamLoginSecure=76561199184792059%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxQl8yMkJCQ0IxNl82OEUxRSIsICJzdWIiOiAiNzY1NjExOTkxODQ3OTIwNTkiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4NzYyNzk5NiwgIm5iZiI6IDE2Nzg4OTk5MDUsICJpYXQiOiAxNjg3NTM5OTA1LCAianRpIjogIjBEMDlfMjJCQkNCMTJfMkUwODAiLCAib2F0IjogMTY4NzUzOTkwNCwgInJ0X2V4cCI6IDE3MDU4MDg4MzAsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI0My4yMDYuMjM0LjE3MyIsICJpcF9jb25maXJtZXIiOiAiNDMuMjA2LjIzNC4xNzMiIH0.C8fjurSovHCWljva2ElNFh_x6MI22fwyws14lg4a53zFF1FmqfKBZxSiA5Cl5kLN0X5Z3wS8r48Mq9MGJzKXCA; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1687539911%7D'
}
TRYheader = {
    'Cookie':
    'steamLoginSecure=76561199357667004%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQwRl8yMkJCQ0IxNF8wQTNBQSIsICJzdWIiOiAiNzY1NjExOTkzNTc2NjcwMDQiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4NzYyNjE3NSwgIm5iZiI6IDE2Nzg4OTk2MTcsICJpYXQiOiAxNjg3NTM5NjE3LCAianRpIjogIjBEMEFfMjJCQkNCMTVfRjc1NkIiLCAib2F0IjogMTY4NzUzOTYxNiwgInJ0X2V4cCI6IDE3MDU2Nzc1NDYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxMDMuMTY3LjEzNS4xMzMiLCAiaXBfY29uZmlybWVyIjogIjEwMy4xNjcuMTM1LjYzIiB9.JIjzVE_Ocxf1sg3wNBjkHpdLlZVSKz65xPX0gcV4BYNAY8TIdCb4VEJihoBl89f5-QQZ97t0QjJLrpR7ZvoDBA;webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1687539635%7D'
}
ARSheader = {
    'Cookie':
    'steamLoginSecure=76561199510157463%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxNl8yMkJCQ0IxMl9GN0Q3MiIsICJzdWIiOiAiNzY1NjExOTk1MTAxNTc0NjMiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4NzYyODUyMiwgIm5iZiI6IDE2Nzg5MDA4MzQsICJpYXQiOiAxNjg3NTQwODM0LCAianRpIjogIjBEMUVfMjJCQkNCMTdfRDk4OEMiLCAib2F0IjogMTY4NzU0MDgzMywgInJ0X2V4cCI6IDE3MDU5NDM1NTMsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxMDMuMTY3LjEzNS43MyIsICJpcF9jb25maXJtZXIiOiAiMTAzLjE2Ny4xMzUuNjMiIH0.dVVadmg25HEQyIDXaKdE8FPGAXMsP_dk3u_SrmBbZOLk5ARefpLSf7r0sDXtnO5x262fjcPEhzuvungeHg8ADw;webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1687540835%7D'
}
USDheader = {}

header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

with open("currency.json", 'r', encoding='utf-8') as f:
    data = json.load(f)


def getprice(wrice, header, type, port):
    time.sleep(0.5)
    global data
    proxy = {
        'http': '127.0.0.1:{}'.format(port),
        'https': '127.0.0.1:{}'.format(port)
    }
    para = {
        'country': 'HK',
        'language': 'schinese',
        'currency': '{}'.format(data[type]["eCurrencyCode"]),
        'item_nameid': '14962973',
        'two_factor': '0'
    }
    url = "https://steamcommunity.com/market/itemordershistogram?country=HK&language=schinese&currency={}&item_nameid=14962973&two_factor=0".format(
        data[type]["eCurrencyCode"])
    # 发送GET请求并获取响应
    response = requests.get(url, proxies=proxy, headers=header, params=para)

    # 检查请求是否成功
    if response.status_code == 200:
        #with open('test.html','w',encoding='utf-8') as f:
        #    f.write(response.text)
        elements = response.json()
        element = elements['sell_order_graph'][0][0]
        if element:
            #print("第一个元素价格:", element)
            wrice[type] = float(element)
            return 0
        else:
            return -1
    else:
        return -1


def Fprice(wrice, port):
    rcode = 0
    rcode = min(getprice(wrice, header, 'ARS', port), rcode)
    rcode = min(getprice(wrice, header, 'CNY', port), rcode)
    rcode = min(getprice(wrice, header, 'TRY', port), rcode)
    rcode = min(getprice(wrice, header, 'USD', port), rcode)
    return rcode
    #print(wrice)


def Getname(url, port):
    proxy = {
        'http': '127.0.0.1:{}'.format(port),
        'https': '127.0.0.1:{}'.format(port)
    }
    qheader = {
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url, proxies=proxy, headers=qheader)
    #with open("test.html", 'w', encoding='utf-8') as f:
    #    f.write(response.text)
    # 解析 HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # 使用选择器选择元素并获取文本内容
    element = soup.select_one("#mainContents > div.market_listing_nav_container > div > a:nth-child(2)")
    if element:
        text = element.text.strip()
        return text
    else:
        return None


if __name__ == '__main__':
    res = {}
    with open('port.txt', 'r') as f:
        port = int(f.readline())
    print(
        Getname(
            "https://steamcommunity.com/market/listings/570/Astral%20Drift?buffPrice=22",
            port))
