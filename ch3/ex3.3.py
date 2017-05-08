def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def print_post():
    print("+ - - - - ", end = '')

def print_bar():
    print("|         ", end = '')


def top_bar():
    do_twice(print_post)
    print("+")

def mid_sect():
    do_twice(print_bar)
    print("|")

def whole_mid_sect():
    do_four(mid_sect)

def grid_form():
    top_bar()
    whole_mid_sect()
    top_bar()
    whole_mid_sect()
    top_bar()

grid_form()
