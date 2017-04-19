#Write a function named even_odd that takes a single argument, a number.
#return True if the number is even, or False if the number is odd.
#You can use % 2 to find out the remainder when dividing a number by 2. Even numbers won't have a remainder....

def even_odd(num):
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False
