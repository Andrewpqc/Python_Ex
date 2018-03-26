from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'  # 邮件服务器地址
app.config['MAIL_PORT'] = 25  # 邮件服务器端口
app.config['MAIL_USE_TLS'] = True  # 启用 TLS
app.config['MAIL_USERNAME'] = "3480437308@qq.com"#os.environ.get('MAIL_USERNAME') or 'me@example.com'
app.config['MAIL_PASSWORD'] = "授权码"#os.environ.get('MAIL_PASSWORD') or '123456'

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hi', sender='3480437308@qq.com', recipients=['3480437308@qq.com'])
    msg.html = '<b>Hello Web</b>'
    msg.body = 'The first email!'
    mail.send(msg)
    return '<h1>OK!</h1>'


if __name__ == '__main__':
    app.run()
