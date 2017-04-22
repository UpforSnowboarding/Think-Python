import string

with open('Alice2.txt', encoding="utf8") as fin:
	Alice = fin.readlines()

#remove punctuation, spaces, uppercase

def clean_word(file):
	clean_list = []

	for line in file:
		line = line.replace('-', ' ')		
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()
			clean_list += [word]
	return clean_list

print(clean_word(Alice))
