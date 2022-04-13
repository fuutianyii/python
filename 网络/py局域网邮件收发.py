import smtplib
from email.mime.text import MIMEText
from email.header import Header
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################调DNS####################
################放第一个！####################
sender = 'fty@test1.com'
receivers = ['user1@test1.com']
message = """From: 111 <fty@test1.com>
To: 123 <user1@test1.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('172.16.1.101')###服务器
    smtps=MIMEText("我是内容","plain","utf-8")
    smtps['Subject']=Header("我是标题",'utf-8')
    smtps['From']="fty@test1.com"
    smtps['To']="user1@test1.com"
    smtpObj.sendmail(sender, receivers, smtps.as_string())
    print("发送完毕")
except:
    print('无法发送邮件')

# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr,formataddr
# import smtplib

# def _format_addr(s):
#     name,addr =parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))
# '''加密发送邮件'''
# def sendEmail(from_addr,password,to_addr,smtp_server):
#     try:
#         msg =MIMEText('你好，来自火星的问候','plain','utf-8')#文本邮件

#         msg['FROM'] = _format_addr('2271479796@qq.com<%S>'%from_addr)
#         msg['TO'] = _format_addr('1587873181@qq.com<%S>'%to_addr)
#         msg['SUBJECT'] =Header('邮件主题：来自火星的问候','utf-8').encode()
#     server = smtplib.SMTP(smtp_server,25)
#     #server.starttls#调用starttls()方法，创建了安全连接  
#     server.set_debuglevel(1)#记录详细信息
#     password='wyr189135'
#     server.login(from_addr,password)#登录邮箱
#     server.sendmail(from_addr,[to_addr],msg.as_string())#发送信息
#     server.quit()
#     print('邮件加密发送成功')
#     except Exception as e:
#         pritn('发送失败' + e)
#     if __name__ =='__main__':
#         sendEmail('邮箱地址：','2271479796@qq.com','1587873181@qq.com','smtp.si-tech.com.cn')






#         '''from_addr是发送的邮件'''
#         '''password是发送邮件邮箱的密码'''
#         '''to_addr是接受的邮箱名'''
#         '''smtp_server:smtp.qq.com是smtp服务器的端口号'''


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# '''第三方服务'''
# mail_host="mail.qq.com"
# mail_user='2271479796@qq.com'#用户名
# mail_pass='wyr189135'#口令/密码

# sender = '2271479796@qq.com'
# receivers = ['1587873181@qq.com']#接收邮箱，可设置为QQ邮箱或者其他邮箱

# '''
#     # smtpObj = smtplib.SMTP([host [, port [, locla_hostname]]])#创建SMTP对象语法

#     host：SMTP服务器主机 可以指定主机的IP或域名  可选参数
#     port：如果你提供了host参数，你需要指定SMTP服务使用的端口号，一般情况下SMTP端口为25
#     local_hostname：如果smtp在你的本机上，只需要指定服务器地址为localhost就行

#     # SMTP.sendmail(from_addr,to_addrs,mgs[, mail_options,rcpt_options])#使用SMTP对象sendmail方法发送邮件

#     from_addr:邮件发送者的地址
#     to_addrs:字符串列表，邮件发送地址
#     msg:发送消息
# '''
# message =MIMEText('python 发送邮件...','plain','utf-8')#文本内容
# message['From'] = Header('来自火星的问候','utf-8')#发送者
# message['To'] = Header('测试...','utf-8')#接收者

# subject = 'Python SMTP 邮件测试...'
# message['Subject'] = Header(subject,'utf-8')

# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host,25)
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print('邮件发送成功')
# except smtplib.SMTPException:
#     print('Error:无法发送邮件')


