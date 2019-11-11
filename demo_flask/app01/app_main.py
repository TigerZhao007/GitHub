
# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import json
from flask import url_for, Flask, render_template, redirect, request
from flask_login import (LoginManager, current_user, UserMixin, login_required, login_user, logout_user)


# 初始化平台~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = Flask(__name__)

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

# 用户登录退出路由~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# 数据库中导入数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import setup
import pandas as pd

# -----数据表echart01----- #
table_name = 'echart01'
sql = '''select * from public."%s"  ''' % (table_name)
with setup.engine_postgresql00.connect() as conn:
    echart01 = pd.read_sql_query(sql, conn)

echart01 = {'aa':list(echart01.aa), 'xiaoliang':list(echart01.xiaoliang), 'chengben':list(echart01.chengben)}

# -----数据表echart02----- #
table_name = 'echart02'
sql = '''select * from public."%s"  ''' % (table_name)
with setup.engine_postgresql00.connect() as conn:
    echart02 = pd.read_sql_query(sql, conn)

data_legend = ['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']

echart02 = {'data_legend':list(data_legend), 'data_xAxis':list(echart02.data_xAxis),
            'data_yAxis_01':list(echart02.data_yAxis_01), 'data_yAxis_02':list(echart02.data_yAxis_02),
            'data_yAxis_03':list(echart02.data_yAxis_03), 'data_yAxis_04':list(echart02.data_yAxis_04),
            'data_yAxis_05':list(echart02.data_yAxis_05)}

# -----数据表echart03----- #
table_name = 'echart03'
sql = '''select * from public."%s"  ''' % (table_name)
with setup.engine_postgresql00.connect() as conn:
    echart03 = pd.read_sql_query(sql, conn)

echart03 = {'data_name':list(echart03.data_name), 'data_value':list(echart03.data_value)}

# 定义视图，一个界面设定为一个视图~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/', methods=['GET','POST'])
@login_required
def index():
    if current_user.is_active:
        return redirect(url_for('Add'))
    else:
        return redirect('/login')

@app.route('/echart01', methods=['GET','POST'])
@login_required
def Echart01():

    aa = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']  # 中文报错，需要用axjx获取
    xiaoliang = [5,20,36,10,10,20]
    chengben = [5,20,36,10,10,20]
    jsondata = {'aa':aa, 'xiaoliang':xiaoliang, 'chengben':chengben}
    j = json.dumps(jsondata, ensure_ascii=False)

    return render_template('html_echart_001.html',j=j, aa=aa, xiaoliang=xiaoliang, chengben=chengben, ensure_ascii=False)

@app.route('/echart02', methods=['GET','POST'])
@login_required
def Echart02():
    return render_template('html_echart_002.html')

@app.route('/echart03', methods=['GET','POST'])
@login_required
def Echart03():
    return render_template('html_echart_003.html')

@app.route('/web01', methods=['GET','POST'])
@login_required
def web01():
    return render_template('web01.html', title='测试', message=url_for('Add'))

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

# 定义数据接口（读取数据库数据，接收后返回前端）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/echart01_data')
def get_data_01():
    # aa = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
    # xiaoliang = [5,20,36,10,10,20]
    # chengben = [5,20,36,10,10,20]
    # jsondata = {'aa':aa, 'xiaoliang':xiaoliang, 'chengben':chengben}
    # data = json.dumps(jsondata, ensure_ascii=False)  # 如果有中文的话，就需要ensure_ascii=False
    data = json.dumps(echart01, ensure_ascii=False)
    return (data)

@app.route('/echart02_data')
def get_data_02():
    # data_legend = ['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
    # data_xAxis = ['周一','周二','周三','周四','周五','周六','周日']
    # data_yAxis_01 = [120, 132, 101, 134, 90, 230, 210]
    # data_yAxis_02 = [220, 182, 191, 234, 290, 330, 310]
    # data_yAxis_03 = [150, 232, 201, 154, 190, 330, 410]
    # data_yAxis_04 = [320, 332, 301, 334, 390, 330, 320]
    # data_yAxis_05 = [820, 932, 901, 934, 1290, 1330, 1320]
    #
    # jsondata = {'data_legend':data_legend, 'data_xAxis':data_xAxis, 'data_yAxis_01':data_yAxis_01,
    #             'data_yAxis_02': data_yAxis_02, 'data_yAxis_03': data_yAxis_03, 'data_yAxis_04': data_yAxis_04,
    #             'data_yAxis_05': data_yAxis_05 }
    # data = json.dumps(jsondata, ensure_ascii=False)  # 如果有中文的话，就需要ensure_ascii=False

    data = json.dumps(echart02, ensure_ascii=False)  # 如果有中文的话，就需要ensure_ascii=False
    return (data)

@app.route('/echart03_data')
def get_data_03():
    # data_name = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
    #            'District of Columbia', 'Florida', 'Georgia','Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    #            'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan','Minnesota',
    #            'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    #            'New Mexico', 'New York', 'NorthCarolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
    #            'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
    #            'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']
    # data_value = [4822023, 731449, 6553255, 2949131, 38041430, 5187582, 3590347, 917092, 632323, 19317568, 9919945,
    #               1392313, 1595728, 12875255, 6537334, 3074186, 2885905, 4380415, 4601893, 1329192, 5884563, 6646144,
    #               9883360, 5379139, 2984926, 6021988, 1005141, 1855525, 2758931, 1320718, 8864590, 2085538, 19570261,
    #               9752073, 699628, 11544225, 3814820, 3899353, 12763536, 1050292, 4723723, 833354, 6456243, 26059203,
    #               2855287, 626011, 8185867, 6897012, 1855413, 5726398, 576412, 3667084]
    # jsondata ={'data_name':data_name, 'data_value':data_value}
    # data = json.dumps(jsondata, ensure_ascii=False)  # 如果有中文的话，就需要ensure_ascii=False

    data = json.dumps(echart03, ensure_ascii=False)
    return (data)

# 定义错误界面~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 错误时，返回指定界面
@app.errorhandler(404)
def miss(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def error(e):
    return render_template('index.html'), 500

# 产品界面运行~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__=="__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0", port=8080)
    # context = ('../zhengshu/1_bundle.crt', '../zhengshu/2_key.key')
    # app.run(host="0.0.0.0", port=8080, threaded=True, ssl_context=context)