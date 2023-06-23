import requests
import re
from bs4 import BeautifulSoup

url = "https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Nova%20%7C%20Koi%20%28Minimal%20Wear%29"

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


def getprice(wrice, header, type, port):
    proxy = {
        'http': '127.0.0.1:{}'.format(port),
        'https': '127.0.0.1:{}'.format(port)
    }
    # 发送GET请求并获取响应
    response = requests.get(url, proxies=proxy, headers=header)

    # 检查请求是否成功
    if response.status_code == 200:
        #with open('test.html','w',encoding='utf-8') as f:
        #    f.write(response.text)
        soup = BeautifulSoup(response.content, "lxml")
        element = soup.find(
            "span",
            class_="market_listing_price market_listing_price_with_fee")
        if element:
            price = element.text.strip()
            print("第一个元素价格:", price)
            patten = r'[0-9,.]+'
            matches = re.findall(patten, price)
            if type in ('ARS', 'TRY'):
                value = ''.join(matches).replace('.', '').replace(',', '.')
            else:
                value = ''.join(matches).replace(',', '')
            wrice[type] = float(value)
        else:
            print("未找到匹配元素")
    else:
        print("请求失败:", response.status_code)


def Fprice(wrice, port):
    getprice(wrice, ARSheader, 'ARS', port)
    getprice(wrice, CNYheader, 'CNY', port)
    getprice(wrice, TRYheader, 'TRY', port)
    getprice(wrice, USDheader, 'USD', port)
    print(wrice)
