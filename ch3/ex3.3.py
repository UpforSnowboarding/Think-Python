def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def print_line():
	print("+ - - - -", end = ' ')

def print_bar():
	print("|        ", end = ' ')

def print_plus_minus():
	do_twice(print_line)
	print("+")

def print_middle():
	do_twice(print_bar)
	print("|")

def print_grid():
	print_plus_minus()
	do_four(print_middle)
	print_plus_minus()
	do_four(print_middle)
	print_plus_minus()

print_grid()
