from flask import Flask, render_template
from flask import url_for

#render templates --> return 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


if __name__=="__main__":
    app.run()

