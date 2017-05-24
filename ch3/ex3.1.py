def right_justify(s):
	space = ' '
	space_multi = space * 65
	right_justified = space_multi + s
	return right_justified

res = right_justify('monty')
print(res)
print(len(res))


# a more generalised version

def right_justify2(s):
    spaces = ' '
    blank_space_count = 70 - len(s)
    blank_space = blank_space_count * spaces
    full_string = blank_space + s
    return full_string

print(right_justify2('hereissometext'))



