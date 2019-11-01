from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('Add'))

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

@app.route('/web01', methods=['GET','POST'])
# @auth.route('/echart03', methods=['GET','POST'])
def web01():
    return render_template('web01.html', title='测试', message=url_for('Add'))

# @app.route('/Add2', methods=['GET','POST'])
# def Add():
#     if request.method == 'POST':
#         a = request.form['adder1']
#         b = request.form['adder2']
#         a = int(a)
#         b = int(b)
#         c = a + b
#         return render_template('web01.html', message=str(c))
#     return render_template('web01.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8081)