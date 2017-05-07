def do_twice(f,freq):
	count = 0
	while count < freq:
		f()
		count += 1

def print_spam():
	print('spam')

do_twice(print_spam, 2)


# 4)
def print_twice(word):
	print(word)
	print(word)


def do_twice(func,arg):
	func(arg)

do_twice(print_twice, 'spam')

print('')

# 5)

def do_four(func, arg):
	do_twice(func,arg)
	do_twice(func,arg)

do_four(print_twice, 'spam')
