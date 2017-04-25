import string

def process_file(file_name):
	hist = dict()
	for line in file_name:
		clean_word(line, hist)
	return hist

def clean_word(file, hist):
	file = file.replace('-', ' ')	
	
	for word in file.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word, 0) + 1


def subtract(d1,d2):
	res = dict()
	for key in d1:
		if key not in d2:
			res[key] = None
	return res

file1 = open('A Tale of Two Cities.txt', encoding = "utf8")
file2 = open('words.txt')


hist = process_file(file1)
words = process_file(file2)
diff = subtract(hist, words)
for word in diff:
	print(word, end = ' ')
