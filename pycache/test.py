import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
#
# sender = '5724924@qq.com'  # 发件邮箱
# passwd = 'rtccbnjnydebbigg'  # 发送人邮箱授权码
# receivers = '5724924@qq.com'  # 收件邮箱
# subject = 'sb110问卷网激活账号'  # 主题
# content = """
# <p>欢迎注册sb110问卷网几号, 离注册完成还有最后一步</p>
# <p><a href="http://127.0.0.1:8000">点击此处以激活账号</a></p>
# <p>如果这并不是你本人操作, 请忽略这封邮件</p>
# """
# msg = MIMEText(content, 'html', 'utf-8')
# #msg['Subject'] = subject
# msg['Subject'] = Header(subject, 'utf-8')
# msg['From'] = formataddr(['sb110问卷网',sender])
# #msg['From'] = Header('sb110问卷网', 'utf-8')
# # msg['To'] = receivers
# msg['To'] = Header("testtest", 'utf-8')
# try:
#     s = smtplib.SMTP_SSL('smtp.qq.com', 465)
#     s.login(sender, passwd)
#     s.sendmail(sender, receivers, msg.as_string())
#     print('Send Success')
# except:
#     print('Send Failure')



my_sender='5724924@qq.com'    # 发件人邮箱账号
my_pass = 'rtccbnjnydebbigg'              # 发件人邮箱密码
my_user='5724924@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret = True
    try:
        content = """
        <p>欢迎注册sb110问卷网几号, 离注册完成还有最后一步</p>
        <p><a href="http://127.0.0.1:8000">点击此处以激活账号</a></p>
        <p>如果这并不是你本人操作, 请忽略这封邮件</p>
        """
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = "SB110Rigiseter <5724924@qq.com>"  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "激活你的sb110账号"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
mail()