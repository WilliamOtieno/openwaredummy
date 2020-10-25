from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'gnulinuxopenware@gmail.com'
app.config['MAIL_PASSWORD'] = 'club09@.com'
app.config['MAIL_DEFAULT_SENDER'] = ('GNU | Linux OpenWare', 'gnulinuxopenware@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mail")
def send_mail():
    msg = Message(subject="Testing",
                  body ="This is just a bloody test",
                  recipients=['jimmywilliamotieno@gmail.com', 'otienosamwel135@gmail.com', 'jamie.william.284@outlook.com'])
    mail.send(msg)
    return "Sent to recipients"


if __name__ == "__main__":
    app.run(debug=True)
