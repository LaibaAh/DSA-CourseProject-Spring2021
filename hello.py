from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('home.html', name=name)