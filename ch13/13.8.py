import random
import string
from collections import defaultdict


def analysis1 (filename, skip_header):
	""" Perform markov analysis on the read file

	structure - dict[prefix] = suffix

	Return markov dict
	"""

	d = defaultdict(list)
	with open(filename, encoding = "utf8") as fd:
		if skip_header:
			skip_gutenberg_header(fd)

		for line in fd:
			line = line.replace('-', '')
			line_split = line.split()
			for i in range(0, len(line_split)-1):
				strippables = string.punctuation + string.whitespace
				word = line_split[i]
				word = word.strip(strippables).lower()
				d[word].append(line_split[i+1])

		return d

def generate_random_words(l, prefix_len = 2, text_len = 50):
	""" Generate random text from the markov dict
	
	Starts again if raised error
	"""
	random_list = []
	word_list = []
	for word in list(l.keys()):
		if len(word) == prefix_len:
			word_list.append(word)
	first = random.choice(word_list)
	random_list.append(first)
	first_s = l[first]
	index2 = random.randint(0, len(first_s)-1)
	for i in range(text_len):
		previous = first_s[index2]
		sub = l[previous]
		random_index = random.randint(0, len(sub) -1)
		random_list.append(sub[random_index])

	print(' '.join(random_list))

def skip_gutenberg_header(fp):
	"""Reads from fp until it finds the line that ends the header.

	fp: open file object
	"""
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
			break

def main():

	x = analysis1("emma.txt", skip_header= True)
	print("Print Random Text")
	generate_random_words(x)

main()
