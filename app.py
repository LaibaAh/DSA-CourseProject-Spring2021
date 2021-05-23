from flask import Flask, render_template, request,redirect
from flask import url_for
import os
from flask.globals import session 
from flask_sqlalchemy import SQLAlchemy
import sqlite3


ad_list = {"Hu Dukaan": [("Cafeteria", 2), ("Dhaaba", 2), ("East Street", 3)],
           "East Street": [("Central Street 2", 4), ("Hu Dukaan", 3)],
           "Cafeteria": [("Central Lower Ground", 2), ("Gym", 4), ("Swimming Pool", 4), ("Amphitheater", 2), ("Hu Dukaan", 2), ("Central Street 2", 3)],
           "Central Lower Ground": [("Circuits and Electronic Lab 1", 3), ("Music Room", 2), ("Library", 4), ("Cafeteria", 2)],
           "Circuits and Electronic Lab 1": [("Music Room", 2), ("Central Street 1", 3), ("Central Lower Ground", 3)],
           "Music Room": [("Linux And Networking Lab", 2), ("Central Lower Ground", 2), ("Circuits and Electronic Lab 1", 2)],
           "Linux And Networking Lab": [("Visualization And Graphics Lab", 2), ("Music Room", 2)],
           "Visualization And Graphics Lab": [("Linux And Networking Lab", 2)],
           "Swimming Pool": [("Cafeteria", 4)],
           "Gym": [("Cafeteria", 4)],
           "Dhaaba": [("Zen Garden", 3), ("Multipurpose Sports Courts 1", 3), ("Hu Dukaan", 2)],
           "Zen Garden": [("Multipurpose Sports Courts 1", 2), ("Dhaaba", 3)],
           "Central Street 1": [("Circuits and Electronic Lab 1", 3), ("Wellness Courtyard", 2), ("Office Of Student Life", 2), ("Reception", 3), ("Library", 3), ("Central Street 2", 2)],
           "Wellness Courtyard": [("Central Street 1", 2), ("Office Of Student Life", 1)],
           "Office Of Student Life": [("Central Street 1", 2), ("Wellness Courtyard", 1)],
           "Central Street 2": [("Earth Courtyard", 3), ("Student Lounge", 4), ("Central Street 1", 2), ("Soorty Hall", 3), ("East Street", 4), ("East Zone", 2), ("Cafeteria", 3)],
           "Earth Courtyard": [("Central Street 2", 3), ("Learn Courtyard", 2), ("Arif Habib Classroom", 1), ("Air Courtyard", 1), ("Water Courtyard", 1)],
           "Air Courtyard": [("Earth Courtyard", 1), ("Arif Habib Classroom", 2), ("Water Courtyard", 1)],
           "Water Courtyard": [("Earth Courtyard", 1), ("Fire Courtyard", 1), ("Air Courtyard", 1)],
           "Fire Courtyard": [("Water Courtyard", 1), ("Chemistry Lab", 1), ("Digital Systems and Instrumentation Lab", 1), ("Student Lounge", 4)],
           "Chemistry Lab": [("Fire Courtyard", 1), ("Digital Systems and Instrumentation Lab", 1)],
           "Digital Systems and Instrumentation Lab": [("Fire Courtyard", 1), ("Chemistry Lab", 1)],
           "Arif Habib Classroom": [("Earth Courtyard", 1), ("Air Courtyard", 2)],
           "Learn Courtyard": [("Earth Courtyard", 2)],
           "Student Lounge": [("Amphitheater", 2), ("Central Street 2", 4), ("Multipurpose Sports Courts 1", 3), ("Soorty Hall", 2), ("Fire Courtyard", 4)],
           "Multipurpose Sports Courts 1": [("Student Lounge", 2), ("Zen Garden", 2), ("Dhaaba", 3)],
           "Amphitheater": [("Student Lounge", 2), ("Engineering Workshop", 2), ("Cafeteria", 2)],
           "Engineering Workshop": [("Amphitheater", 2)],
           "Soorty Hall": [("Student Lounge", 2), ("Central Street 2", 3), ],
           "Library": [("Central Lower Ground", 3), ("Central Street 1", 3), ("Reception", 1)],
           "Reception": [("Central Street 1", 3), ("Student Center", 1), ("Library", 1), ("Elevator", 1)],
           "Student Center": [("Reception", 1), ("Elevator", 1)],
           "Elevator": [("Student Center", 1), ("Reception", 1), ("West Zone 1", 3), ("Auditorium Hall", 3), ("Playground", 4), ("Prayer Area", 5)],
           "East Zone": [("West Zone 1", 3), ("Tariq Rafi Lecture Theater", 2), ("Film Studio", 4), ("West Zone 2", 2), ("Central Street 2", 2)],
           "Tariq Rafi Lecture Theater": [("Film Studio", 2), ("East Zone", 4), ("Mehfil", 4)],
           "Film Studio": [("Tariq Rafi Lecture Theater", 2), ("East Zone", 4)],
           "Mehfil": [("Tariq Rafi Lecture Theater", 4)],
           "West Zone 1": [("East Zone", 3), ("Faulty Pod", 4), ("Playground", 2), ("West Zone 2", 2), ("Elevator", 3)],
           "West Zone 2": [("East Zone", 2), ("West Zone 1", 2), ("Baithak", 3), ("Amin Issa Tai Classroom", 3), ("Design Studio", 3)],
           "Amin Issa Tai Classroom": [("Design Studio", 1), ("West Zone 2", 3), ("Baithak", 2)],
           "Design Studio": [("West Zone 2", 3), ("Amin Issa Tai Classroom", 1)],
           "Baithak": [("Amin Issa Tai Classroom", 2), ("West Zone 2", 3)],
           "Auditorium Hall": [("Elevator", 3)],
           "Playground": [("Elevator", 4), ("West Zone 1", 2)],
           "Faulty Pod": [("West Zone 1", 4)],
           "Prayer Area": [("Elevator", 5), ("Faculty Cafeteria", 2), ("Day Care", 1)],
           "Faculty Cafeteria": [("Prayer Area", 2)],
           "Day Care": [("Prayer Area", 1)]}

# Helper Functions


def place(previ, lst):
    for i in range(len(lst)):
        place = lst[i][1]
        if previ[1] == lst[i][1]:
            x = i
    return x


def addnodes(ad_list):
    node = []
    for i in ad_list:
        node.append(i)
    return node


def Initilize(lst, start):
    for i in range(len(lst)):
        if lst[i][1] == start:
            lst[i][0] = start
            lst[i][2] = 0
    return lst

# getting minimum distance/time egde


def minimumdistance(lst, visited):
    shortest_time = float('inf')
    pair = []

    for i in range(len(lst)):
        place = lst[i][1]
        time = lst[i][2]
        # shortest distance not in v.
        if place not in visited and time < shortest_time:
            shortest_time = time
            # we get ['node1','node2',time] like this
            pair = lst[i]
    return pair

# getting the weights


def weight(ad_list, previ, s):
    first = previ[1]
    weigh = 0
    u = ad_list[first]
    for i in range(len(u)):
        if u[i][0] == s[0]:
            weigh = u[i][1]
            # print(weigh)
    return weigh

# getting the neighbours of the extracted node.


def getneighbours(ad_list, m, visited):
    # m is the node!
    lst = []
    for i in range(len(ad_list[m[1]])):
        # if the place is not yet visited, append the whole neighbour tuple ('Baithak', 2) to the list.
        if ad_list[m[1]][i][0] not in visited:
            # append the whole neighbour tuple ('Baithak', 2) to the list.
            lst.append(ad_list[m[1]][i])
    return lst


def getShortestPath(ad_list, start, Des):  # Dijkstra
    lst = []

    # Appending the nodes in a list first that is getting list of nodes in graph/Map
    nodes = addnodes(ad_list)

# Initialzation of the nodes other than starting node to infinity
    for i in nodes:
        l = ['', i,  float('inf')]
        lst.append(l)

    lst = Initilize(lst, start)

# he queue has all the nodes with inf time right now.
# visited list to keep track of the visited nodes.
    visited = []
    q = nodes
    while len(q) != 0:
        # geting the minimum distance pair, lst[i][2]
        m = minimumdistance(lst, visited)
        # getting its neighbours. (tuple of neighbours)
        node = getneighbours(ad_list, m, visited)
        # appending the place/ node visited in the visited list
        visited.append(m[1])
        # Removing it from the queue after extraction.
        q.remove(m[1])

        previ = m
        # starting to update the neighbours in lst, if less weight is found then update.

        x = place(previ, lst)

        while len(node) != 0:
            s = node[0]
            popping = node.pop(0)

            for n in range(len(lst)):
                # if the place is nodes in lst
                if s[0] == lst[n][1]:
                    r = n  # neheighbour index

            weight_n = lst[x][2] + weight(ad_list, previ, s)

            # updating the weight if new weight found is less in the list.
            if lst[r][2] > weight_n:
                # update the node as well.
                lst[r][2] = weight_n
                lst[r][0] = previ[1]

    # got all edges time in list. #print(lst)
# getting the path from Hu Dukaan to the destination!
    lst_it = []
    for i in range(len(lst)):
        # print(sd[i][0])
        places = lst[i][1]
        times = lst[i][0]
        if places == Des and times != start:
            lst_it.append(lst[i])

            while lst[i][0] != start:

                for j in range(len(lst)):
                    # simple comparsion from the value.
                    if lst[j][1] == lst[i][0]:
                        if lst[j][0] != start:
                            lst_it.append(lst[j])
                            lst[i] = lst[j]
                        else:
                            lst.append(lst[j])
                            path = lst_it[::-1]
                            return path
# for directly connected nodes time from the hu dukaan.
        elif lst[i][1] == Des and lst[i][0] == start:
            return [lst[i]]
    path = lst_it[::-1]

    return path


# First as the customer for the proper Destination.

# Your_Destination = input(("Please write your destination for the delivery: "))

# If proper destination not written then print the message Enter valid destination.

# if Your_Destination not in ad_list:
    # print("Invalid Destination")

# running our DA algorithm to get the minimum time from Hu dukaan to customer's destination, simple.
# result = (getShortestPath(ad_list, "Hu Dukaan", Your_Destination))
# print(result) #uncomment to view the traversed path.

# for displaying the minimum delivery time found through our DA algo.


def delivery_time(result, Start):
    lst1 = []
    Start = "Hu Dukaan"
    lst1.append(Start)
    # print(len(result))
    # if result len is greater than 0 getting the hu dukaan then delivery time for that destination from hu Dukaan)
    if len(result) > 0:
        delivery_time = (result[len(result)-1][2])
        print("The Total Delivery Time is: ", delivery_time, "minutes")
    # else this!
    # that is the node is not persent/ destination not valid so result list will be empty!
    elif len(result) == 0:
        delivery_time = 0
        print("Can't determine the delivery time! Please, Enter Valid Destination (Input): ",
              delivery_time, "minutes")
# getting the trasvered path as well for the customer  to see.
    for i in result:
        delivery_place = i[1]
        lst1.append(delivery_place)
    print("The Shortest Path from Hu Dukaan to your destination is: ", lst1)

    # print(lst1)


Start = "Hu Dukaan"

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


@app.route('/cart', methods=["POST"])
def cart():
    request_data = request.get_json()
    print(request_data)
    name = request_data['name']
    price = request_data['details']
    

   
    
    return render_template('cart.html')


@app.route('/checkoutone')
def checkoutone():
    return render_template('checkout.html')

@app.route('/checkout', methods = ['POST'])
def checkout():
    destination = request.form['destination']
    print("Your destination is '" + destination + "'")
    # calling your distance algo
    result = (getShortestPath(ad_list, "Hu Dukaan", destination))

    if len(result) > 0:
        delivery_time = (result[len(result)-1][2])
        print(delivery_time)
    # printing the result of your shortest time
    
    # displaying it in html
    return render_template('checkout.html', output=delivery_time)



if __name__=="__main__":s
    app.run(debug=True)

