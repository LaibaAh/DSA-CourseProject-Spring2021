from flask import Flask, render_template, request,redirect
from flask import url_for
import os
from algorithm import *

#the items are stored in a dictonary,the format of the dictionary is as follows:
# the key values in the dictionary, store the item names as item ids and the value is a list
# [1500, 50, "static\images\Acrylic Sheild.jpg"] at the index 0 we have the item's price, on the first index we have stored the amount of item in the inventory
# at the 2 index we have passed a string that stores the relative path for the image of the item, this was done so that in the html file
# we can apply a loop that runs through this inventory and displays all the items stored in the inventory automatically  

inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}

#the output.sqlite file in the folder is actually a data base of the this stored inventory

app = Flask(__name__)


# URL Routing

@app.route('/')
def home():
    return render_template('home.html')


#these pages are sample templates than indicate that these features can also be included to our project such as a login system that would
#get a post and get request
@app.route('/login',  methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')

#this is the main function call of the shop page, it displays the shopping elements and the price the given code

@app.route('/shop',methods=["GET"])

def shop():
    inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}
    return render_template('shop.html',inventory=inventory)


#the cart function is connected to the shop html code it helps to fetch element ids from the button and sends them to display on the checkout tag 
total_price = 0 
@app.route('/cart', methods=["POST"])
def cart():
    inventory= {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}
    cart_stack = []
    total_price = 0 
    price_stack = []
    request_data = request.get_json()
    print(request_data) #from this printing we can see that as you press the add to cart button a request would be printed in the format [product, price]
    name = request_data['name']
    price = request_data['details']
    cart_stack.append(name) #we append the added items to a cart which is a stack  and stores the items in the stack 
    # for item in cart_stack: 
    #     details = inventory[item] #this runs a loop
    #     details[1] = details[1] - 1 #edits the inventory
    #     total_price += int(price) 
    print(total_price,inventory)
    
    return render_template('cart.html', inventory=inventory, display_price=price, display_name=name)


@app.route('/checkoutone')
def checkoutone():
    return render_template('checkout.html')


#on the checkout page our final dijikstra's algorithm is applied by importing it from the algorithm.py file 
@app.route('/checkout', methods = ['POST'])
def checkout():
    destination = request.form['destination']
    print("Your destination is '" + destination + "'")
    # calling your distance algo
    result = (getShortestPath(ad_list, "Hu Dukaan", destination))

    if len(result) > 0:
        delivery_time = (result[len(result)-1][2])
        print(delivery_time)
    # printing the result of smallest time taken
    
    # displaying it in html
    return render_template('checkout.html', output=delivery_time)


#here finally the app runs, cntrl+enter runs the file and outputs 
# * Debug mode: on
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 184-775-028
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#this is a local link that you can host on your local server and will open the file on your browser 
if __name__=="__main__":
    app.run(debug=True)

