import string

with open('A Tale of Two Cities.txt', encoding="utf8") as fin:
	A_tale_book = fin.readlines()

#remove punctuation, spaces, uppercase

def clean_word(file):
	clean_list = []
	flag = False
	sign = "***"

	for line in file:
		if line.startswith(sign):
			flag = True
		if flag:
				line = line.replace('-', ' ')		
				for word in line.split():
					word = word.strip(string.punctuation + string.whitespace)
					word = word.lower()
					clean_list += [word]
		else:
			pass

	return clean_list

print(clean_word(A_tale_book))
