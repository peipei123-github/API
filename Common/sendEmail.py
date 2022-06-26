import smtplib, time, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class SendEmail():
    #第一步：配置邮箱属性
    def __init__(self):
        #发送邮箱
        self.sender='1050482001@qq.com'
        #接收邮箱
        self.receiver='13649267590@163.com'
        #发送邮箱主题
        self.t=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
        self.subject='自动化测试结果_'+self.t
        #发送邮箱服务器
        self.smtperver='pop.qq.com'
        #发送邮箱用户名/密码
        self.username='1050482001'
        self.password='cmbxviysaqcwbbcc'
        #邮件内容
        self.content='Python 邮件发送测试'

    #第二步：组装邮件内容和标题
    def content_header(self,file):
        with open(file, 'rb') as f:
            mail_body = f.read()
         # 组装邮件内容和标题
            self.msg = MIMEMultipart()
            # 添加附件内容
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename=report.html'
            self.msg.attach(att)
             # 添加邮件的文本内容
            content = '自动化测试报告详情，请查收附件'
            self.msg.attach(MIMEText(self.content, 'plain', 'utf-8'))
            self.msg['Subject'] = Header(self.subject, 'utf-8')
            self.msg['From'] = self.sender
            self.msg['To'] = self.receiver


        #第三步：登录并发送邮件
    def send(self,file):
        self.content_header(file)
        try:
            #实例化
            s=smtplib.SMTP()
            #链接服务器
            s.connect(self.smtperver)
            #登录邮箱
            s.login(self.username,self.password)
            #设置发件人，收件人，邮件内容
            s.sendmail(self.sender,self.receiver,self.msg.as_string())
        except Exception as msg:
            print(f'邮件发送失败{msg}')
        else:
            print('邮件发送成功')
        finally:
            s.quit()
if __name__ == '__main__':
    ce=SendEmail()
    file=os.path.dirname(os.path.dirname(__file__))+'/testReport/2022_02_12_14_36_36report.html'
    ce.send(file)
