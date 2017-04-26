import string

book1 = open('A Tale of Two Cities.txt', encoding = "utf8")
book2 = open('words.txt')

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

def subtract(d1,d2):
	"""Returns a set of all keys that appear in d1 but not d2.

	d1, d2: dictionaries
	"""
	return set(d1) - set(d2)

def main():
	hist = process_file(book1, skip_header = False)
	words = process_file(book2, skip_header = False)
	diff = subtract(hist,words)
	print("The words in the book that aren't in the word list are: ")
	for word in diff:
		print(word, end = ' ')

if __name__ == '__main__':
	main()
