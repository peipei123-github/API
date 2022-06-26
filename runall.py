import os
import unittest
import time
from HTMLTestRunner import HTMLTestReportCN
from Common.log import logger
from Common.sendEmail import SendEmail
#查找测试用例，生成测试套件
def create_suite():
    #获取testCase路径
    case_dir=os.path.dirname(__file__)+'/testCase'
    logger.info(f'testcase路径{case_dir}')
    # 实例化TestLoader # 调用discover方法
    suite=unittest.TestLoader().discover(start_dir=case_dir,pattern='test*')
    #返回结果
    return suite

#清理测试报告：方法1-全部删除
def clear1():
    #获取目录下的所有文件,列表类型
    dir_name=os.path.dirname(__file__)+'/testReport'
    file_name=os.listdir(dir_name)
    #遍历删除
    for i in file_name:
        os.remove(dir_name+'/'+i)

#清理测试报告：方法2-保留最新3个
def clear2():
    #获取目录下的所有文件,列表类型
    dir_name=os.path.dirname(__file__)+'/testReport'
    file_name=os.listdir(dir_name)
    #遍历删除,保留最新的3个
    for i in file_name[0:-3]:
        os.remove(dir_name+'/'+i)

#清理测试报告：方法3-按照生成时间保留最新3个
def clear3():
    #获取目录下的所有文件,列表类型
    dir_name=os.path.dirname(__file__)+'/testReport'
    file_name=os.listdir(dir_name)
    #定义一个列表，存放文件的生成时间
    list_filetime=[]
    # 获取生成时间
    for i in range(len(file_name)):
        file_time = os.path.getctime(dir_name + '/'+file_name[i])
        list_filetime.append(file_time)
    #使用字典推导式：得到文件名称：文件生成时间
    dict_file={list_filetime[j]:file_name[j] for j in range(len(file_name))}
    #按照时间将时间列表进行排序
    list_filetime.sort()
    #除最新的3个文件，其余遍历删除
    for i in list_filetime[:-3]:
        os.remove(dir_name+'/'+dict_file[i])


if __name__ == '__main__':
    #获取测试套件
    suite=create_suite()
    #获取时间
    cur_time=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
    #创建报告文件名称t
    report_name=os.path.dirname(__file__)+'/testReport/'+cur_time+'report.html'
    #以写入方式打开文件
    with open(report_name,'wb') as fp:
        #实例化HTMLTestRunner得到runner
        runner=HTMLTestReportCN(stream=fp, verbosity=1,title='api测试报告',description='api测试结果',tester='wpp')
        #调用实例方法运行测试套件
        runner.run(suite)
    # 发送邮件
    re = SendEmail()
    re.send(report_name)
    #删除报告
    clear3()


