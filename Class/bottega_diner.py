# 	- User selects an entree.
# 	- “Waitress” makes a comment based on their selection
# 	- Tell them the price
# 	- repeat the above options for side choices (suggestion and a price, don’t repeat chef suggestion)
# 	- total up the cost

# BONUS
# Have a breakfast, lunch and dinner menu.  Breakfast has different items, lunch and dinner have the same items but are different prices.
# BONUS: Allow for item customization (how items are prepared, decide additional cost implications)
# EXTRA BONUS: 3D print out actual food and eat it.

def diner():
    diner_menu = {
        "breakfast" : {
            "entrees" : {
                "oatmeal" : 3.00,
                "pancakes" : 5.00,
                "crepes" : 5.50,
            },
            "sides" : {
                "bacon" : 2.00,
                "banana" : .50,
                "eggs" : 2.00
            },
            },
        "lunch" : {
            "entrees" : {
                "turkey sandwich" : 6.99,
                "chicken fingers" : 6.00,
                "ham sandwich" : 6.99,
                "grilled cheese" : 3.99,
                "burger" : 6.99,
            },
            "sides" : {
                "fries" : 2.00,
                "fruit" : 3.00,
            },
            },
        "dinner" : {
            "entrees" : {
                "turkey sandwich" : 7.99,
                "chicken fingers" : 7.00,
                "ham sandwich" : 7.99,
                "grilled cheese" : 4.99,
                "burger" : 8.99, 
            }  , 
            "sides" : {
                "fries" : 2.50,
                "fruit" : 3.50,
            },
            },
        "drinks" : {
            "soda" : 1.50,
            "orange juice" : 2,
            "chocolate milk" : 2,
            "water" : 0,
        }
    }
    while True:
        menu = input("Welcome to the diner! Would you like to see our breakfast, lunch, or dinner menu today?\nMenu:")
        if menu.lower() in diner_menu and menu.lower() != "drinks":
            print("=========")
            for key, value in diner_menu[menu.lower()]["entrees"].items():
                print(f"{key.title()} - ${'{:.2f}'.format(value)}")
            print("=========")
        else:
            print("Come again?")
            continue
        while True:
            choice = input("What can I get for you?\nEntree:")
            if choice.lower() in diner_menu[menu.lower()]["entrees"]:
                print("Good choice! Would you like a side with that?")
                print("=========")
                for key, value in diner_menu[menu.lower()]["sides"].items():
                    print(f"{key.title()} - ${'{:.2f}'.format(value)}")
                print("=========")
            else:
                print("That sounds good, but it's not an entree on the menu!")
                continue
            while True:
                side_choice = input("Side:")
                if side_choice.lower() in diner_menu[menu.lower()]["sides"]:
                    print("=========")  
                    for key, value in diner_menu["drinks"].items():
                        print(f"{key.title()} - ${'{:.2f}'.format(value)}")
                    print("=========")
                    print("Great! What would you like to drink?")
                else:
                    print("That sounds good, but it's not a side!")
                    continue
                while True:
                    drink = input("Drink:")
                    if drink.lower() in diner_menu["drinks"]:
                        print("Fantastic choices. Your food will be right out!\n...")    
                        total = diner_menu["drinks"][drink.lower()] + diner_menu[menu.lower()]["entrees"][choice.lower()] + diner_menu[menu.lower()]["sides"][side_choice.lower()]
                        print(f"I hope you enjoyed your meal!\nYour total will be ${'{:.2f}'.format(total)}")
                        return False
                    else:
                        print("That sounds good, but it's not a drink on our menu!")
                        continue
                        
diner()