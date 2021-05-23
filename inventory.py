#this is the backend code for the inventory functionality

inventory = {'Acrylic Shield': [1500, 50, "static\images\Acrylic Sheild.jpg"],
     'Card-keychain': [60, 50, "static\images\card-keychain.jpg"], 'Classwiz-Calculator': [2000, 50, "static\images\Casio Classwiz.jpeg"],
     'Color-changing-mug': [600, 50, "static\images\colour changing Mug.jpg"], 'Corrector': [10, 50, "static\images\corrector.jpeg"], 'Eraser': [5, 50, "static\images\eraser.jpeg"],
     'HU-spiral-Notebook': [500, 50, "static\images\HU-Spiral Notebook.jpg"], 'Markers': [250, 50, "static\images\markers.jpeg"],'Pen': [40, 50, "static\images\pen.png"], 'Pencil': [10, 50, "static\images\pencil.jpeg"], 
     'Scale': [5, 50, "static\images\scale.jpeg"], 'Sharpner': [60, 50, "static\images\sharpner.jpeg"], 'Stapler': [60, 50, "static\images\stapelar.jpeg"], 'Tape': [60, 50, "static\images\Tape.jpeg"], 
     'White-notepad':[100, 50, "static\images\White notepad.jpg"], 'World-map-penset': [600, 50, "static\images\world-map pen set.jpg"]}

items = []
for item in inventory.keys():
     items.append(item)

print("here is the list of available items")
print(items)

#please enter one item at a time
name = input("Enter the product you want")
quantity = input("Enter the Amount")

if name not in items:
     print(input("Enter the product you want"))
else:
     total_price=0
     details = inventory[name] 
     details[1] = details[1] - int(quantity) #edits the inventory
     total_price += details[0] #the edited inventory is printed with the total price

          

     print(total_price,inventory)



