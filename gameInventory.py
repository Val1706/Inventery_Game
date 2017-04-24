import operator
import csv

inventory = {}
added_items = []
# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("\nInventory: ")
    num_items = []
    for keys in inventory:
        print(inventory[keys], keys)
        num_items.append(inventory[keys])
    print("\nTotal number of items: ", sum(num_items))

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for new_it in added_items:
        if new_it in inventory.keys():
            inventory[new_it] += 1
        if new_it not in inventory.keys():
            inventory[new_it] = 1
    display_inventory(inventory)
    return inventory



# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    if order == "count,desc":
        a = sorted(inventory.items(), key=operator.itemgetter(1))
    elif order == "count,asc":
        a = sorted(inventory.items(), reverse=True, key=operator.itemgetter(1))
    elif order==None:
        a = inventory.items()

    d = dict(a)
    num_items = []
    print("-----------------------")
    print("Count:    Item name: \n")
    for keys in d:
        num_items.append(d[keys])
        length = len(str(d[keys]))
        spc = " "
        if length > 1 and length < 3:
            len_space = spc * 6
        elif length > 2 :
            len_space = spc * 5
        else:
            len_space = spc * 7
            print(spc * 1, d[keys], len_space,keys)
    print("-----------------------")
    print("Total number of items: ", sum(num_items))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).



def import_inventory(inventory, filename="test_inventory.csv"):
    add_to_inventory(inventory, added_items)
    with open("test_inventory.csv", "r") as csv_file:
        import_items = []
        for row in csv_file:
            import_items.append(row)
        for object in import_items:
            one_object = object.split(",")
            list_objects = one_object[0:]
            for words in list_objects:
                added_items.append(words)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="test_inventory_export.csv"):
    import_inventory(inventory, filename="test_inventory.csv")
    with open("test_inventory_export.csv", "w") as csv_file:
        csv_write = csv.writer(csv_file, delimiter=',')
        csv_write.writerow(added_items)




