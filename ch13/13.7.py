import random
import string

from bisect import bisect

A_tale_book = open('/Users/ivangiang/Downloads/A Tale of Two Cities.txt', encoding = "utf8")

def process_file(file_name, skip_header):
	hist = dict()
	fp = file_name

	if skip_header:
		skip_gutenberg_header(fp)

	for line in fp:
		process_line(line, hist)

	return hist

def skip_gutenberg_header(fp):
	"""Reads from fp until it finds the line that ends the header.
    
    fp: open file object
    """
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
    		 break

def process_line(line, hist):

	"""Adds the words in the line to the histogram.
	Modifies hist.
	line: string
	hist: histogram (map from word to frequency)
	"""

	# replace hyphens with spaces before splitting
	line = line.replace('-', ' ')
	
	stripping = string.punctuation + string.whitespace

	for word in line.split():
		# remove punctuation and convert to lowercase
		word = word.strip(stripping)
		word = word.lower()

		# update the histogram
		hist[word] = hist.get(word, 0) + 1


def random_word(hist):

	"""Chooses a random word from a histogram.

	The probability of each word is proportional to its frequency.

	hist: map from word to frequency
	"""
	# TODO: This could be made faster by computing the cumulative
	# frequencies once and reusing them.

	words = []
	freqs = []
	total_freq = 0

	# make a list of words and a list of cumulative freqencies
	for word, freq in hist.items():
		total_freq += freq
		words.append(word)
		freqs.append(total_freq)

	# choose a random value and find its location in the cumulative list
	x = random.randint(0, total_freq-1)
	index = bisect(freqs, x)
	return words[index]

def main():
	hist = process_file(A_tale_book, skip_header = False)
	print("\n\nHere are some random words from the book")
	for i in range(100):
		print(random_word(hist), end = ' ')

if __name__ == '__main__':
	main()
