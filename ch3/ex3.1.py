def right_justify(s):
	space = ' '
	space_multi = space * 65
	right_justified = space_multi + s
	return right_justified

res = right_justify('monty')
print(res)
print(len(res))
