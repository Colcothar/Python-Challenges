#Write a function named squared that takes a single argument.
#If the argument can be converted into an integer, convert it and return the square of the number (num ** 2 or num * num).
#If the argument cannot be turned into an integer (maybe it's a string of non-numbers?), return the argument multiplied by its length. 
#Look in the file for examples.

def squared(arg):
    try:
        arg = int(arg)
    except ValueError:
        return arg * len(arg)
    else: 
        return arg * arg
        
        
