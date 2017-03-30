#Ugh, I made this list and now it has some invalid pieces in it. Maybe you can help me clean it up.
#Use the .remove() method to remove the last item from the list, please.

states = [
    'ACTIVE',
    ['red', 'green', 'blue'],
    'CANCELLED',
    'FINISHED',
    5,
]

states.remove(5)

#OK, one more removal. See that second item in states? 
#It's a list of colors and doesn't belong here. Can you get rid of it for me? Be sure to use .remove() again.

states.remove(['red', 'green', 'blue'])
