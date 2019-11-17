# ######################################
# 导入所需模块
# ######################################
from flask import Flask, render_template, redirect, request
from flask_login import \
    (LoginManager, current_user,UserMixin, login_required,
     login_user, logout_user)

import sys
sys.path.append(r'D:\Work\CodeSpace\PythonSpace\flask_demo\demo05')
from db import *

from wtforms import Form,TextField,PasswordField,validators

# ######################################
# 用户登陆管理设置内容
# ######################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ijaswe'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.session_protection = 'strong'   # 防止恶意用户篡改 cookies

user_dict = {}

# ######################################
# 定义相关的类
# ######################################
class User(UserMixin):
    def load_by_user_id(self, user_id):
        """
        在实际项目中，这个方法应该从数据库中根据user_id来查询用户信息
        为了演示方便，我这里省略了从数据库查询数据的过程
        如果数据库中没有user_id这个用户，你应该返回False
        :param user_id: 用户唯一标识
        :return:
        """
        self.user_id = 1
        self.username = user_dict.get(self.user_id)
        return True

    def get_id(self):
        return self.user_id

class LoginForm(Form):
	username = TextField("username",[validators.Required()])
	password = PasswordField("password",[validators.Required()])


# ######################################
# 定义IP首页， 如果已经登陆进出首页，否则进入登陆界面
# ######################################
@app.route('/')
@login_required
def index():
    if current_user.is_active:
        return render_template('index.html', user=current_user)
    else:
        return redirect('/login')

# ######################################
# 用户注册界面
# ######################################
@app.route("/regist",methods=['GET','POST'])
def regist():
	myForm=LoginForm(request.form)
	if request.method=='POST':
		insert(myForm.username.data,myForm.password.data)
		return redirect('/login')
	return render_template('regist.html',form=myForm)

# ######################################
# 用户登陆界面
# ######################################
# 用户登陆界面
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        # 实际项目中，你应该根据username和 password查询数据库，以确定用户能否登录
        # 这里为了演示方便，只要密码是123456就可以登录了
        if password == '123456':
            user = User()
            user.user_id = 1
            user.username = username
            user_dict[user.user_id] = username
            login_user(user, True)
            return redirect('/')
        else:
            return redirect('/regist')
            # return redirect('/regist')

# @app.route("/login",methods=['GET','POST'])
# def login():
# 	myForm=LoginForm(request.form)
# 	if request.method =='POST':
# 		if (isExisted(myForm.username.data,myForm.password.data)):
#             user = User()
#             user.user_id = 1
#             user.username = myForm.username
#             user_dict[user.user_id] = myForm.username
#             login_user(user, True)
# 			return redirect("/")
# 		else:
# 			return "Login Failed"
# 	return render_template('regist.html',form=myForm)

# ######################################
# /logout 用户权限跟踪设置
# ######################################
# /logout 用户权限跟踪设置
@login_manager.user_loader
def load_user(user_id):
    user = User()
    if user.load_by_user_id(user_id):
        return user
    else:
        return None

# ######################################
# /logout 用户退出界面
# ######################################
# /logout 用户退出界面
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# ######################################
# 登录后--展示界面
# ######################################
# /echart01 界面
@app.route('/echart01', methods=['GET','POST'])
@login_required
def Echart01():
    if current_user.is_active:
        return render_template('html_echart_001.html', user=current_user)
    else:
        return redirect('/login')

# /echart02 界面
@app.route('/echart02', methods=['GET','POST'])
@login_required
def Echart02():
    if current_user.is_active:
        return render_template('html_echart_002.html', user=current_user)
    else:
        return redirect('/login')

# /echart03 界面
@app.route('/echart03', methods=['GET','POST'])
@login_required
def Echart03():
    if current_user.is_active:
        return render_template('html_echart_003.html', user=current_user)
    else:
        return redirect('/login')


# ######################################
# 设置运行IP和运行端口
# ######################################
if __name__=="__main__":
    app.run(port=8083)




