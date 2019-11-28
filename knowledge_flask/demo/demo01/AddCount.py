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

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8082)