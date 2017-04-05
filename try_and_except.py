#I need you to make a new function, add.
#add should take two arguments, add them together, and return the total.

def add(param_one, param_two):
    total = param_one + param_two
    return total
    
#Let's make sure we're always working with floats. 
#Convert your arguments to floats before you add them together. 
#You can do this with the float() function.
    
def add(param_one, param_two):
    total = float(param_one) + float(param_two)
    return total
    
    
#You're doing great! Just one more task but it's a bigger one.
#Right now, we turn everything into a float. That's great so long as we're getting numbers or numbers as a string. 
#We should handle cases where we get a non-number, though.
#Add a try block before where you turn your arguments into floats.
#Then add an except to catch the possible ValueError. Inside the except block, return None.
#If you're following the structure from the videos, add an else: for your final return of the added floats.

def add(param_one, param_two):
    try:
        param_one = float(param_one)
        param_two = float(param_two)
    except ValueError:
        return None
    else:
        total = param_one + param_two
        return total
