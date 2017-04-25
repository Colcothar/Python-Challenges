#Same idea as the last one. My loopy function needs to skip an item this time, though.
#Loop through each item in items again. If the character at index 0 of the current item is the letter "a", continue to the next one. 
#Otherwise, print out the current member.
#Example: ["abc", "xyz"] will just print "xyz".

def loopy(items):
    for things in items:
        if things[0] == 'a':
            continue
        else:
            print(things)
