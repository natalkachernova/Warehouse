import csv

items = {}

sold_items = {}

def get_items():
    print("Name\t\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t\t--------\t----\t----------")
    for item in items:
        print(item, "\t\t\t", items[item][0], "\t\t", items[item][1], "\t", items[item][2])

def get_sold_items():
    print("Name\t\t\tQuantity\tUnit\tSum (PLN)")
    print("----\t\t\t--------\t----\t----------")
    for sold_item in sold_items:
        print(sold_item, "\t\t\t", sold_items[sold_item][0], "\t\t", sold_items[sold_item][1], "\t", sold_items[sold_item][2])

def add_item(name, quantity, unit, unit_price):
    items[name] = [quantity, unit, unit_price]
    get_items()

def sell_item(name, quantity_for_sale):
    if quantity_for_sale <= items[name][0]:
        items[name][0] -= quantity_for_sale;
        print(f"Successfully sold {quantity_for_sale} {items[name][1]} of {name} !")
        sold_items[name] = [quantity_for_sale, items[name][1], round(items[name][2] * quantity_for_sale)]
        get_items()
    else:
        print("There are not enough goods in stock to sell!")

def get_costs():
    items_list = []
    for item in items:
        items_list.append(round(items[item][0] * items[item][2]))
    return sum(items_list)

def get_income():
    items_list = []
    for sold_item in sold_items:
        items_list.append(sold_items[sold_item][2])
    return sum(items_list)

def save_items_to_csv():
    with open('warehouse.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            tmp_items = items[item]
            writer.writerow({'name': item, 'quantity': tmp_items[0], 'unit': tmp_items[1], 'unit_price': tmp_items[2]})

def load_items_from_csv():
    with open('warehouse.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            quantity = int(row['quantity'])
            unit = row['unit']
            unit_price = float(row['unit_price'])
            items[name] = [quantity, unit, unit_price]
    get_items()
        
command_string = ""
while command_string != 'exit':
    command_string = input ("What would you like to do? (Enter ""help"" to get a list of commands): ")

    if command_string in ('exit', 'help', 'show', 'showsold', 'add', 'sell', 'show_revenue', 'load', 'save'):
        if command_string == 'exit':
            print("Exiting... Bye!")
        if command_string == 'help':
            print("\nAvalaible commands:\nhelp - this help\nexit - stop running a programm\n" + 
                  "show - a list of items in the warehouse\nshowsold - a list of items sold from the warehouse\n" + 
                  "add - adding a new item to the warehouse\nsell - selling items from the warehouse\n" +
                  "show_revenue - to get a sum\nload - load data from a file\nsave - save the data to a file\n")
        if command_string == 'show':
            get_items()
        if command_string == 'showsold':
            get_sold_items()
        if command_string == 'add':
            print("Adding to the warehouse...")
            name_item = input ("Item name: ")
            quantity_item = int(input ("Item quantity: "))
            unit_item = input ("Iem unit of measure. Eg. l, kg, pcs: ")
            price_item = float(input ("Item price in PLN: "))
            add_item(name_item, quantity_item, unit_item, price_item)
        if command_string == 'sell':
            print("Selling from the warehouse...")
            name_item_to_sale = input ("Item name: ")
            quantity_item_to_sale = int(input ("Quantity to sell: "))
            sell_item(name_item_to_sale, quantity_item_to_sale)
        if command_string == 'show_revenue':
            print("Revenue breakdown (PLN)")
            income = get_income()
            costs = get_costs()
            print("Income: ", income)
            print("Costs: ", costs)
            print("----------")
            print("Revenue: ", (income - costs))
        if command_string == 'save':
            save_items_to_csv()
        if command_string == 'load':
            items = {}
            load_items_from_csv()