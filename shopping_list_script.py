#Shopping list to-do list
# 1. Run the script to start using it.
# 2. Put new things inthe the list, one at a time.
# 3. Enter the word DONE - in all caps - to quit the program


def shopping_list():
    shopping_items = []
    if not shopping_items: 
        print("Your shopping list is currently empty.\n")
        add_to_list = input("Would you like to add an item to your shopping list? Please type 'Yes' or 'no':\n")
        add_to_list = add_to_list.upper()
        if add_to_list == "YES":
            item_to_add = input("Please enter one item to add: \n")
            item_to_add = str(item_to_add)
            shopping_items.append(item_to_add)
            print("Your shopping list contains: " + ', '.join(shopping_items))
            add_more = input("Would you like to add to your list? \n")
            add_more = add_more.upper()
        while add_more == "YES":
            next_item = input("What else would you like to add? \n")
            next_item = str(next_item)
            shopping_items.append(next_item)
            print("Your shopping list now contains: " + ', '.join(shopping_items))
        else:
            print("Goodbye")
                
                
                
    elif add_to_list == "NO":
            print("Goodbye")
    
           
            
shopping_list()
                
        
