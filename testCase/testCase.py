import unittest
from ddt import ddt,data,unpack

from Common.readExcel import ReadExcle
from Common.configHttp import ConfigHttp
from Common.log import logger
from Common.writeExcel import WriteExcel

#获取测试数据
data_obj=ReadExcle()
test_data=data_obj.read()

#获取测试数据
@ddt
class TestCase(unittest.TestCase):
    @data(*test_data)
    @unpack
    def test_case(self,id,interfaceUrl,name,method,value,expect,real,status):
        #发送请求，得到响应结果
        ch_obj=ConfigHttp(interfaceUrl,method,value)
        res=ch_obj.run()
        logger.info(f'测试结果为{res}')
        dict_res=res.json()
        real=dict_res['errorCode']
        #将预期结果与实际结果进行比较:相等则pass，否则fail
        if int(expect)==int(real):
            status='pass'
        #将测试结果写入文件中
        else:
            status='fail'
        #将测试结果写入excle中
        write_obj=WriteExcel()
        write_obj.write_excel(int(id),6,real,status)

if __name__ == '__main__':
    unittest.main(verbosity=2)



