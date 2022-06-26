#获取excel中的数据
#导包
import xlrd
import os
#创建类
class ReadExcle():
    #创建初始化方法
    def __init__(self):
        #获取文件路径
        self.file_name=os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        #打开excel文件
        self.readbook=xlrd.open_workbook(self.file_name)
        #获取指定的sheet页
        self.sheet=self.readbook.sheet_by_index(0)
        #获取最大行数和列数
        self.max_row=self.sheet.nrows
        self.max_col=self.sheet.ncols
        #定义一个空列表，用于存储数据
        self.res_list=[]
        #读取表格中的第一个数据，作为字典的key值
        self.first_row=self.sheet.row_values(0)
    #创建读取数据的方法
    def read(self):
        #从excel中的第二行开始
        for i in range(1,self.max_row):
            #循环读取每行数据
            each_row=self.sheet.row_values(i)
            #用列表推导式，将表头和数据组装成字典格式的数据
            dict_row={self.first_row[j]:each_row[j] for j in range(self.max_col)}
            #将组装好的字典数据添加至列表中
            self.res_list.append(dict_row)
        #返回列表
        return self.res_list

if __name__ == '__main__':
    excel_obj=ReadExcle()
    print(excel_obj.read())