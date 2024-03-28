# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Cherries": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49,
            "Lamb": 9.49,
            "Salmon": 9.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Black": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49,
            "Matcha": 8.99
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried oreos": 4.49
    }
}

# Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to Lish's Awesome Food Truck.")

place_order = True
while place_order:
    print("Let me know which menu you would like to order from? ")

    i = 1
    menu_items = {}

    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        menu_category = int(menu_category)
        if menu_category in menu_items:
            menu_category_name = menu_items[menu_category]
            print(f"You selected {menu_category_name}")
            
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for subkey, subvalue in value.items():
                        print(f"{i}      | {key} - {subkey}{' ' * (24 - len(key + subkey) - 3)}| ${subvalue}")
                        menu_items[i] = {"Item name": f"{key} - {subkey}", "Price": subvalue}
                        i += 1
                else:
                    print(f"{i}      | {key}{' ' * (24 - len(key))}| ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1
            
            item_selection = input("Enter the menu item number you would like to order: ")
            
            if item_selection.isdigit():
                item_selection = int(item_selection)
                if item_selection in menu_items:
                    selected_item = menu_items[item_selection]
                    
                    quantity = input(f"How many of '{selected_item['Item name']}' would you like to order? ")
                    if not quantity.isdigit():
                        print("Invalid quantity. Defaulting to 1.")
                        quantity = 1
                    else:
                        quantity = int(quantity)
                    
                    order.append({
                        "Item name": selected_item["Item name"],
                        "Price": selected_item["Price"],
                        "Quantity": quantity
                    })
                else:
                    print("Invalid selection. Please try again.")
            else:
                print("Please enter a valid number for your selection.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")
    
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
    if keep_ordering == "n":
        print("Thank you for your order!")
        break

print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    print(f"{item_name}{' ' * (26 - len(item_name))}| ${price}{' ' * (7 - len(str(price)))}| {quantity}")

total_cost = sum(item["Price"] * item["Quantity"] for item in order)
print(f"\nTotal Cost: ${total_cost:.2f}")
