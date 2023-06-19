import requests
import time

def fetchrate(kind):
    #time.sleep(3)
    url = 'https://steamcommunity.com/market/listings/730/Souvenir%20Sawed-Off%20%7C%20Snake%20Camo%20(Well-Worn)/render/?query=&start=40&count=100&currency={}'.format(kind)

    headers = {
        "Sec-Ch-Ua":
        '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "Sec-Ch-Ua-Mobile":
        "?0",
        "Sec-Ch-Ua-Platform":
        '"Windows"',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    with open('port.txt','r') as f:
        try:
            port = int(f.readline())
        except FileNotFoundError as e:
            return -2,-2,-2
    load = {'query': '', 'start': '40', 'count': '100', 'currency': str(kind)}
    proxy = {'http': '127.0.0.1:{}'.format(port), 'https': '127.0.0.1:{}'.format(port)}
    response = requests.get(url, headers=headers, params=load, proxies=proxy)
    # 将响应内容转换为JSON对象
    json_data = response.json()
    if json_data==None:
        return -1,-1,-1
    if json_data['success']:
        for key in json_data['listinginfo']:
            item = json_data['listinginfo'][key]
            if item['currencyid'] % 2000 == 23 and item['converted_price']:
                FtoC = round(item['price'] / item['converted_price'], 6)
                CtoF = round(item['converted_price'] / item['price'], 6)
                timestamp = int(time.time())
        return FtoC,CtoF,timestamp
    else:
        return -1,-1,-1

if __name__=="__main__":
    FtoC,CtoF,timestamp=fetchrate(34)
    print(FtoC, CtoF, timestamp)