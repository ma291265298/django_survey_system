import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '5724924@qq.com' #发件邮箱
passwd = 'lkugmgywydhfff' #发送人邮箱授权码
receivers = '5724924@qq.com'   #收件邮箱

subject = 'python发邮Html邮件测试' #主题

content = """         #内容，HTML格式
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
msg = MIMEText(content,'html','utf-8')
# msg['Subject'] = subject
msg['Subject'] = Header(subject,'utf-8')
# msg['From'] = sender
msg['From'] = Header('大傻子','utf-8')
# msg['To'] = receivers
msg['To'] = Header('二愣子','utf-8')
try:
    s = smtplib.SMTP_SSL('smtp.qq.com',465)
    s.login(sender,passwd)
    s.sendmail(sender,receivers,msg.as_string())
    print('Send Success')
except:
    print('Send Failure')
