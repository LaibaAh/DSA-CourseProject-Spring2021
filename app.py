from flask import Flask, render_template, request,redirect
from flask import url_for
import os 
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# current_location = os.path.dirname(os.path.abspath(__file__))

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     return render_template('login.html')

# @app.route('/login_action', methods=["POST"])
# def login_action():
#     UN = request.form['Username']
#     PW = request.form['Password']
#     sqlconnection= sqlite3.Connection(current_location + "\login.db")
#     cursor = sqlconnection.cursor()
#     query1 = "SELECT Username, Password from Users from WHERE Username = {un} AND Password={pw}".format(un= UN, pw=PW)
#     rows = cursor.execute(query1)
#     rows = rows.fetchall()
#     if len(rows) == 1: 
#         return render_template('login.html')
#     else: 
#         return redirect("/signup")

# @app.route('/signup_action', )  

# @app.route('/signup', methods=["GET", "POST"])

# def signup():
#     if request.method == "POST": 
#         dUN = request.form['DUsername']
#         dPM = request.form['DPassword']
#         Uemail = request.form["Email"]
#         sqlconnection = sqlite3.Connection(current_location + "\login.db")
#         cursor = sqlconnection.cursor()
#         query1 = "INSERT INTO Users VALUES('{u}', '{p}', '{e}')".format(u=dUN, p=dPM, e=Uemail)
#         cursor.execute(query1)
#         sqlconnection.commit()
#         return redirect("/login")
#     return render_template("signup.html")


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/shop')
def shop():
    inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "image"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}
    return render_template('shop.html',inventory=inventory)


    


if __name__=="__main__":
    app.run(debug=True)


