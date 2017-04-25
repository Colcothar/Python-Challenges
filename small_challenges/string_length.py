#Create a new function named just_right that takes a single argument, a string.
#If the length of the string is less than five characters, return "Your string is too short".
#If the string is longer than five characters, return "Your string is too long".
#Otherwise, just return True.

def just_right(arg):
    if len(arg) < 5:
        return "Your string is too short"
    if len(arg) > 5:
        return "Your string is too long"
    else:
        return True
