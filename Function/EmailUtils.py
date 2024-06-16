from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from Config.Conf import ConfigYaml
from Function.LogUtils import logger


# 初始化
# smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
class SendEmail:
    def __init__(self, _smtp_address, _username, _password, _receive, title, content=None, file=None):
        self.smtp_address = _smtp_address
        self.username = _username
        self.password = _password
        self.receive = _receive
        self.title = title
        self.content = content
        self.file = file

# 发送邮件方法
    def send_mail(self):
        msg = MIMEMultipart()
        # 初始化邮件信息
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.receive
        # 邮件附件
        if self.file:
            try:
                with open(self.file, 'rb') as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={self.file}",
                    )
                    msg.attach(part)
            except Exception as e:
                logger.error(f"Error reading attachment file {self.file}: {e}")
                return

        # 登录并发送邮件
        try:
            with smtplib.SMTP_SSL(self.smtp_address, port=465) as smtp:
                smtp.login(self.username, self.password)
                smtp.sendmail(self.username, self.receive, msg.as_string())
            logger.info(f"Email sent successfully to {self.receive}")
        except smtplib.SMTPException as e:
            logger.error(f"Error sending email: {e}")


if __name__ == "__main__":
    email_info = ConfigYaml().get_email_info()
    smtp_address = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    receive = email_info["receiver"]
    email = SendEmail(smtp_address, username, password, receive, "测试",
                      content="This is a test email", file="D:\\files\\123test.txt")
    email.send_mail()


