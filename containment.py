#See that time variable? That's what time it currently is, at least for this test. 
#But, when you submit your code, the time might change!
#I need you to make an if condition that sets store_open to True if time is in the store_hours list. 
#Otherwise, if time isn't in store_hours, set store_open to False. 
#You'll probably have to use if, else, and in to solve this one.

time = 15

store_open = None
store_hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

if time in store_hours:
  store_open = True
else:
  store_open = False
