import time


def banner(message, border='-'):
    border_line = border*len(message)
    print(border_line)
    print(message)
    print(border_line)

"""
banner("Hello from Earth")
banner("Hello from Earth", '*')

banner("Hello from Earth", border='#')
banner(message='Hello from Earth')

banner(message='Hello from Earth', border='$')
"""
#print(time.ctime())


def default_time(def_time=time.ctime()):
    print(def_time)


"""every time we run the program, it restarts and hence we get new current time value everytime.
    Bit in command line, as long as we are in the current python shell, we get the same value bcz
    def_time is evaluated the 1st time program runs and that value will be the default value unless 
    the python shell is restarted.
"""


def add_spam_menu(menu=[]):
    menu.append("spam")
    print(menu)


breakfast=["apple", "eggs"]
add_spam_menu(breakfast)

lunch = ["beans"]
add_spam_menu(lunch)

add_spam_menu()
""" Appends spam everytime we call this function without passing a parameter coz the program restarts.
    But in python shell, it appends spam everytime to the existing ex: 'spam, 'spam', 'spam'
"""


def add_spam_check(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    print(menu)

