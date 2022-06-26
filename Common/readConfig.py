#导包
import os
from configparser import ConfigParser
#创建一个类
class ReadConfig():
    #定义初始化方法
    def __init__(self):
        #获取配置文件的路径
        self.file_name=os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        #实例化configparser
        self.conf=ConfigParser()
        #读取指定为位置下的配置文件
        self.conf.read(self.file_name)

    #定义方法：读取指定section下的所有option
    def get_section(self,section):
        return self.conf.items(section)

    #定义方法：读取指定section下的option
    def get_option(self,section,option):
        return self.conf.get(section,option)

    #定义方法：若上传一个参数，则返回指定section下的option；
    #若上传两个参数，则返回指定section下的所有option
    def get_config(self,section,option='all'):
        if option=='all':
            return self.conf.items(section)
        else:
            return self.conf.get(section,option)
if __name__ == '__main__':
    conf_obj=ReadConfig()
    print(conf_obj.get_config('mysql', 'host'))