'''
Author: fuutianyii
Date: 2023-05-11 19:32:41
LastEditors: fuutianyii
LastEditTime: 2023-05-22 18:05:27
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import requests
import json

class FreeIP():
    def __init__(self):
        self.url = "http://proxylist.fatezero.org/proxy.list"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    def check_ip(self, ip_list):
        correct_ip = []
        print("测试后成功的列表为")
        for ip in ip_list:
            if len(correct_ip) > 10: # 可以根据自己的需求进行更改或者注释掉
                break
            ip_port = "{}:{}".format(ip["host"],ip["port"])
            proxies = {'http': ip_port}
            try:
                response = requests.get('http://icanhazip.com/', proxies=proxies,
                                        timeout=3).text  # 如果请求该网址，返回的IP地址与代理IP一致，则认为代理成功
                                                        # 可以更改timeout时间
                if response.strip() == ip["host"]:
                    print("可用的IP地址为：{}".format(ip_port))
                    correct_ip.append(ip_port)
            except:
                print("不可用的IP地址为：{}".format(ip_port))
                pass
        return correct_ip


    def run(self):
        response =  requests.get(url=self.url).content.decode()
        ip_list = []
        proxies_list = response.split('\n')
        print("获取到的列表为")
        for proxy_str in proxies_list:
            try:
                proxy = {}
                proxy_json = json.loads(proxy_str)
                if proxy_json["anonymity"] == "high_anonymous" and proxy_json["type"] == "http":
                    host = proxy_json['host']
                    port = proxy_json['port']
                    proxy["host"] = host
                    proxy["port"] = port
                    ip_list.append(proxy)
                    print("{}符合https和高匿条件".format(host+":"+str(port)))
            except:
                print(proxy_str)

        correct_ip = self.check_ip(ip_list)
        print("可用的IP地址有{}个".format(len(correct_ip)))
        print(correct_ip)


if __name__ == '__main__':
    ip = FreeIP()
    ip.run()

