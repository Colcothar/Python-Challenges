#Use .split() to break the available string apart on the semi-colons (;). Assign this to a new variable sundaes.

available = "banana split;hot fudge;cherry;malted;black and white"

sundaes = available.split(';')

#Let's add a new string variable for displaying our menu items.
#Make a new variable named menu that's set to "Our available flavors are: {}.".

menu = "Our available flavors are {}."

#Alright, let's finish making our menu. Combine the sundaes list into a new variable named display_menu, where each item in the list is rejoined together by a comma and a space (", ").
#Then reassign the menu variable to use the existing variable and .format() to replace the placeholder with the new string in display_menu.
#If you're really brave, you can even accomplish this all on the same line where menu is currently being set.

menu = "Our available flavors are {}.".format(', '.join(sundaes))
