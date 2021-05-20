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