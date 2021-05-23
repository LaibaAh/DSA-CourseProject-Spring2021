# DSA-CourseProject-Spring2021
Habib University E-Dukaan
## Introduction:
Habib University has a Dukaan located at the ground floor in the university premises that sells all necessary stationary items you may need while you are in the University. We Aim to bring the dukaan on your computer. While you are busy and suddenly notice that you would need a set of pencils before your class begins, we provide you a deliery service. 
All you have to do Place your order, estimated time of delivery would be provided and your problem would be solved. 

You can acsess the web application at: https://hu-edukaan.herokuapp.com/checkoutone

## Data Structures and Algorithms Used:
* The main Algoritm used in this project is Dijikstra's Algorithm to find the shortest path from HU-Dukaan to Your selected destination from the dropdown menu 
* Data Structures Used Are: 
   1. Dictionary, Stack
   2. Graph 
* The dictionary and stacks is used to store the inventory and update items in the cart, while the graph data structures helps create the map of the university. 

## How to get the Code Running? 
You can simply click on  https://hu-edukaan.herokuapp.com/checkoutone to see the output frontend, however to get this file running on your computer you would have to:
* pip install flask 
* Run file: app.py 
* here finally the app runs, cntrl+enter runs the file and outputs 
       * Debug mode: on
       * Restarting with stat
       * Debugger is active!
       * Debugger PIN: 184-775-028
       * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#this is a local link that you can host on your local server and will open the file on your browser


## How the Application works:
As you land on the page you will see; 
![image](https://user-images.githubusercontent.com/75496144/119269430-19e78000-bc11-11eb-9156-ec4c6c3376d1.png)

this is a drop down menu that has all the possible destinations. After selecting, click submit. Your estimated display time would be displayed. 

### Additional Features of the Application and Challenges: 
* There are alot of additional features on the web application, suchas the add to cart button (this is a known bug) on the console even after getting the request from the button their is no display on the front-end server. So to show the working, the code is written in the @app.route('/cart) function and in the inventory.py file that shows how the cart is updated as we recieve orders. 
* Login/sign Up feature: As this feature was neither in our proposal nor a main feature and required data base sytems to store and get ids of users we have routed the files but you can still see them on the page as a dummy feature to add the feel of a real-world e-commerce web application. 









