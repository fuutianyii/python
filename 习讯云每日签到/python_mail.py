'''
Author: fuutianyii
Date: 2023-12-22 16:37:30
LastEditors: fuutianyii
LastEditTime: 2023-12-22 17:00:18
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class python_mail:
    def __init__(self,email_provider,sender_email,sender_password):
        self.email_provider=email_provider
        self.sender_email=sender_email
        self.sender_password=sender_password

        
    def send_email(self,receiver_email,subject,body,attachment_path=None):
        self.receiver_email=receiver_email
        self.subject=subject
        self.body=body
        self.attachment_path=attachment_path
        
        # 设置发件人、收件人和邮件主题
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = self.subject

        # 添加邮件正文
        msg.attach(MIMEText(self.body, 'plain'))

        # 添加附件（如果有）
        if self.attachment_path:
            with open(self.attachment_path, 'rb') as attachment:
                part = MIMEApplication(attachment.read())
                part.add_header('Content-Disposition', 'attachment', filename=self.attachment_path)
                msg.attach(part)

        # 根据邮箱类型选择SMTP服务器和端口
        if self.email_provider == 'qq':
            smtp_server = 'smtp.qq.com'  # QQ邮箱SMTP服务器地址
            smtp_port = 465  # QQ邮箱SMTP服务器端口号
        elif self.email_provider == '163':
            smtp_server = 'smtp.163.com'  # 163邮箱SMTP服务器地址
            smtp_port = 25  # 163邮箱SMTP服务器端口号
        else:
            raise ValueError('Unsupported email provider')

        # 连接到SMTP服务器
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        
        # 登录到邮箱账号
        server.login(self.sender_email, self.sender_password)

        # 发送邮件
        server.sendmail(self.sender_email, self.receiver_email, msg.as_string())

        # 关闭连接
        server.quit()

# 使用QQ邮箱发送邮件示例
# mail_qq_sender_email = 'fuutianyii@qq.com'
# mail_qq_sender_password = 'judwfmcrrpdphdee'
# mail_163_sender_password = 'QDPCBBIOZIHPLDVH'
# receiver_email = '1587873181@qq.com'
# email_subject = 'Test Email'
# email_body = 'This is a test email from Python.'

# send_email(mail_qq_sender_email, mail_qq_sender_password, receiver_email, email_subject, email_body, email_provider='qq')

if __name__ == '__main__':
    pymail=python_mail("qq",'fuutianyii@qq.com','judwfmcrrpdphdee')
    pymail.send_email('fuutianyii@qq.com','Test Email','This is a test email from Python.')



# 使用163邮箱发送邮件示例
# 注意：163邮箱的SMTP服务器地址是 smtp.163.com，端口号是 25
# send_email(qq_sender_email, qq_sender_password, receiver_email, email_subject, email_body, email_provider='163')
