from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
# 登录模块
# from flask import Blueprint
# from flask.ext.login import LoginManager, login_required
#
app = Flask(__name__)

# # 登录设置
# app.secret_key = 's3cr3t'
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return None
#
# auth = Blueprint('auth', __name__)

@app.route('/', methods=['GET','POST'])
# @auth.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('Echart01'))

@app.route('/echart01', methods=['GET','POST'])
# @auth.route('/echart01', methods=['GET','POST'])
def Echart01():
    return render_template('html_echart_001.html')

@app.route('/echart02', methods=['GET','POST'])
# @auth.route('/echart02', methods=['GET','POST'])
def Echart02():
    return render_template('html_echart_002.html')

@app.route('/echart03', methods=['GET','POST'])
# @auth.route('/echart03', methods=['GET','POST'])
def Echart03():
    return render_template('html_echart_003.html')

if __name__=="__main__":
    app.run(port=8081)