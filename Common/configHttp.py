#功能：根据测试数据发送请求
#导包
import requests

#定义一个类
class ConfigHttp():
    #定义初始化方法，传入所需数据：url，请求方式，数据
    def __init__(self,url,method,value):
        self.url=url
        self.method=method
        self.value=value
    #定义方法，不同的请求方式，调用不同的方法
    def run(self):
        if self.method=='get':
            res=self.__get()
            return res
        elif self.method=='post':
            res=self.__post()
            return res
    #定义方法：get请求方式
    def __get(self):
        res=requests.get(url=self.url,params=self.url)
        return res
    #定义方法：post请求方式
    def __post(self):
        res=requests.post(url=self.url,data=self.url)