#导包
import os
import xlrd
from xlutils.copy import copy
#创建类
class WriteExcel():
    #定义初始化方法
    def __init__(self):
        #获取文件路径
        self.file_name=os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        #打开文件
        self.rb=xlrd.open_workbook(self.file_name)
        #复制文件
        self.wb=copy(self.rb)
        #指定sheet页
        self.sheet=self.wb.get_sheet(0)
    #定义写入的方法,将实际结果及测试结论写入
    def write_excel(self,x,y,value1,value2):
        #写入数据
        self.sheet.write(x,y,value1)
        self.sheet.write(x,y+1,value2)
        #保存
        self.wb.save(self.file_name)

if __name__ == '__main__':
    write_obj=WriteExcel()
    write_obj.write_excel(2,3,0,'fail')