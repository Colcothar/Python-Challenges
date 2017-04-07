# I need you to help me finish my loopy function. Inside of the function, I need a for loop that prints each thing in items.
# Reminder: Check your syntax and indenting!

def loopy(items):
    for things in items:
        print(things)
        
# Oops, I forgot that I need to break out of the loop when the current item is the string "STOP". Help me add that code!

def loopy(items):
    for things in items:
        if things == "STOP":
            break
        print(things)
