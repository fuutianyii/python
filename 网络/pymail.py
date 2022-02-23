import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='fuutianyii@foxmail.com' #wbinaegbqbddjbjf
my_user='fuutianyii@foxmail.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
# my_pass="name_fu040529"
my_pass="wbinaegbqbddjbjf"
#fty1587873181@163.com  DQFBSITQOLQPIVED
#fuutianyii@163.com EKYBQZDKANDPISHR
#Gmail sdyxpitqlfvcfdzw
def mail(name): 
   msg=MIMEText(f'是时候去续费你的{name}了','plain','utf-8') #正文
   msg['Subject']="autosend" #邮件的主题，也可以说是标题
   msg['From']=formataddr(["fty",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
   msg['To']=formataddr(["you",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
   # smtps=MIMEText("我是内容","plain","utf-8")
   # smtps['Subject']=Header("我是标题",'utf-8')
   # smtps['From']="fty@test1.com"
   # smtps['To']="user1@test1.com" 
   server=smtplib.SMTP("smtp.qq.com",25)  #发件人邮箱中的SMTP服务器，端口是25
   server.login(my_sender,"oyyvaowcepmdiabf")    #括号中对应的是发件人邮箱账号、邮箱密码
   server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
   server.quit()   #这句是关闭连接的意思
   print("发送完毕")

mail("vps")







