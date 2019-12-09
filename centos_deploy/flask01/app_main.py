
# ######################################################################################################################
# 导入所需要的模块
# ######################################################################################################################
# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import url_for, Flask, render_template, redirect, request
from flask_login import (LoginManager, current_user, UserMixin, login_required, login_user, logout_user)

import json
import sqlalchemy
import pandas as pd
import numpy as np

from flask_cors import *  # 跨域名

# 数据库连接配置~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sql_type = ['mssql+pymssql', 'mysql+pymysql', 'postgresql']
username = 'postgres'
password = '123456'
host = '47.100.173.196'
port = '5432'
dbname = 'test'

engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, dbname),
                                             pool_size=20, max_overflow=5)

# 初始化平台~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)

# 运行跨域名~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
app.debug = True
CORS(app, supports_credentials=True)  # 设置参数
# CORS(app, resources=r'/*')

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

# ######################################################################################################################
# 用户登录设置
# ######################################################################################################################
# 用户登录设置~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.config['SECRET_KEY'] = 'ijaswe'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.session_protection = 'strong'   # 防止恶意用户篡改 cookies

user_dict = {}

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

# 用户登录路由~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            return redirect('/login')

@login_manager.user_loader
def load_user(user_id):
    user = User()
    if user.load_by_user_id(user_id):
        return user
    else:
        return None

# 用户退出路由~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# ######################################################################################################################
# 定义视图，一个界面设定为一个视图
# ######################################################################################################################

# 视图'/'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/', methods=['GET','POST'])
@login_required
def index():
    if current_user.is_active:
        return redirect(url_for('Add'))
    else:
        return redirect('/login')

# 视图'/echart01'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart01', methods=['GET','POST'])
@login_required
def Echart01():

    aa = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']  # 中文报错，需要用axjx获取
    xiaoliang = [5,20,36,10,10,20]
    chengben = [5,20,36,10,10,20]
    jsondata = {'aa':aa, 'xiaoliang':xiaoliang, 'chengben':chengben}
    j = json.dumps(jsondata, ensure_ascii=False)

    return render_template('html_echart_001.html',j=j, aa=aa, xiaoliang=xiaoliang, chengben=chengben, ensure_ascii=False)

# 视图'/echart02'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart02', methods=['GET','POST'])
@login_required
def Echart02():
    return render_template('html_echart_002.html')

# 视图'/echart03'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart03', methods=['GET','POST'])
@login_required
def Echart03():
    return render_template('html_echart_003.html')

# 视图'/web01'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/web01', methods=['GET','POST'])
@login_required
def web01():
    return render_template('web01.html', title='测试', message=url_for('Add'))

# ######################################################################################################################
# 定义数据接口（接收前端数据，运算后返回前端）
# ######################################################################################################################
# 定义数据接口（接收前端数据，运算后返回前端）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/Add', methods=['GET','POST'])
def Add():
    if request.method == 'POST':
        a = request.form['adder1']
        b = request.form['adder2']
        a = int(a)
        b = int(b)
        c = a + b
        return render_template('index.html', message=str(c))
    return render_template('index.html')

# ######################################################################################################################
# 定义数据接口（读取数据库数据，接收后返回前端）
# ######################################################################################################################

# 数据'/echart01_data'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart01_data')
@login_required
def get_data_01():

    # 从数据库中获取数据，数据表echart01
    table_name = 'echart01'
    sql = '''select * from public."%s"  ''' % (table_name)
    with engine_postgresql.connect() as conn:
        echart01 = pd.read_sql_query(sql, conn)

    # 将数据处理为JSON格式，返回给前端
    echart01 = {'aa': list(echart01.aa), 'xiaoliang': list(echart01.xiaoliang), 'chengben': list(echart01.chengben)}
    data = json.dumps(echart01, ensure_ascii=False, cls=NpEncoder)
    data.headers['Access-Control-Allow-Origin'] = '*'

    return (data)

# 数据'/echart02_data'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart02_data')
@login_required
def get_data_02():

    # 从数据库中获取数据，数据表echart02
    table_name = 'echart02'
    sql = '''select * from public."%s"  ''' % (table_name)
    with engine_postgresql.connect() as conn:
        echart02 = pd.read_sql_query(sql, conn)

    data_legend = ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']

    # 将数据处理为JSON格式，返回给前端
    echart02 = {'data_legend': list(data_legend), 'data_xAxis': list(echart02.data_xAxis),
                'data_yAxis_01': list(echart02.data_yAxis_01), 'data_yAxis_02': list(echart02.data_yAxis_02),
                'data_yAxis_03': list(echart02.data_yAxis_03), 'data_yAxis_04': list(echart02.data_yAxis_04),
                'data_yAxis_05': list(echart02.data_yAxis_05)}
    data = json.dumps(echart02, ensure_ascii=False, cls=NpEncoder)  # 如果有中文的话，就需要ensure_ascii=False
    data.headers['Access-Control-Allow-Origin'] = '*'

    return (data)

# 数据'/echart03_data'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart03_data')
@login_required
def get_data_03():

    # 从数据库中获取数据，数据表echart03
    table_name = 'echart03'
    sql = ''' select * from public."%s"  ''' % (table_name)
    with engine_postgresql.connect() as conn:
        echart03 = pd.read_sql_query(sql, conn)

    # 将数据处理为JSON格式，返回给前端
    echart03 = {'data_name': list(echart03.data_name), 'data_value': list(echart03.data_value)}
    data = json.dumps(echart03, ensure_ascii=False, cls=NpEncoder)
    data.headers['Access-Control-Allow-Origin'] = '*'

    return (data)

# ######################################################################################################################
# 定义错误界面
# 错误时，返回指定界面
# ######################################################################################################################

@app.errorhandler(404)
def miss(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def error(e):
    return render_template('index.html'), 500

# ######################################################################################################################
# 产品界面运行
# ######################################################################################################################

if __name__=="__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0", port=8080)
