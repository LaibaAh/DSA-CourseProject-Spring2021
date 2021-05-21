from flask import Flask, render_template, request,redirect
from flask import url_for
import os
from inventory import * 

from flask.helpers import total_seconds 
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)

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


@app.route('/AddCart', methods=["POST"])
def AddtoCart():
    inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}
    cart_stack = []
    price_stack=[]
    try: 
        product_id = request.form.get("product_name")
        product_amount = request.form.get("amount")
        cart_stack.append(product_id)
        price_stack.append(product_amount)
        total_price = 0 
        for item in cart_stack:
            details = inventory[item]
            details[1] = details[1] - 1
            total_price += details[0]
        print(total_price)
        print(inventory)
        
        

        
    except: 
        print("e")
    finally: 
        return redirect(request.referrer)
    




if __name__=="__main__":
    app.run(debug=True)


