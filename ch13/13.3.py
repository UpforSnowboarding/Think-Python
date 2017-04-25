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


def most_common(book):
	data1 = clean_word(book)
	dict1 = {}
	for word in data1:
		if word not in dict1:
			dict1[word] = 1
		else:
			dict1[word] += 1
	return dict1

word_count = most_common(A_tale_book)
sorted_count = sorted([(v, k) for k, v in word_count.items()], reverse = True)
top_20 = sorted_count[:20]

for count, word in top_20:
	print (word + " : " + str(count))
