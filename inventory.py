item_list = ["Pencil", "Pen", "Sharpner", "Eraser", "Markers", 
        "Tape", "Classwiz-Calculator", "Corrector", "Stapler",
        "Scale","color-changing-mug", "Acrylic Shield", "card-keychain", 
        "white-notepad","world-map-penset", "HU-spiral-Notebook"]

def insertion_sort(item_list):
    for i in range(len(item_list)):
        j=i
        for j in range(i,0,-1):
            if item_list[j]<item_list[j-1]:
                item_list[j],item_list[j-1]=item_list[j-1],item_list[j]
    return item_list

sorted_list = insertion_sort(item_list)

inventory = {}
for i in sorted_list:
    inventory[i] = 50
print(inventory)





