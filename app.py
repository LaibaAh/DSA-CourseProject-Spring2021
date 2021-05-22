from flask import Flask, render_template, request,redirect
from flask import url_for
import os
from flask.globals import session 
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from algorithm import *

inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}



app = Flask(__name__)


DATABASE = 'output.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db




# URL Routing

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',  methods=['GET','POST'])
def login():
    return render_template('login.html')



@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/shop',methods=["GET"])

def shop():
    inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}
    return render_template('shop.html',inventory=inventory)


@app.route('/cart', methods=["GET" , "POST"])
def cart():
    request_data = request.get_json()

    name = request_data['name']
    price = request_data['price']
    print(name,price)

   
    
    return render_template('cart.html')


@app.route('/checkout', methods = ['POST'])
def checkout():
    destination = request.form['destination']
    print("Your destination is '" + destination + "'")
    # calling your distance algo
    result = (getShortestPath(ad_list, "Hu Dukaan", destination))
    delivery_time = (result[len(result)-1][2])
    # printing the result of your shortest time
    print(delivery_time)
    # displaying it in html
    return render_template('checkout.html', output=delivery_time)

    










if __name__=="__main__":
    app.run(debug=True)

