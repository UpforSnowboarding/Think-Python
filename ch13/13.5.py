import random

t = ['a', 'a', 'b', 'i', 'p', 't', 'i', 'z']

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

hist = histogram(t)
print(hist)

def choose_from_hist(hist):
	list1 = []
	for i in hist:
		for num in range(0, hist[i]):
			list1.append(i)

		random_sel = random.choice(list1)
		return random_sel

print(choose_from_hist(hist))
