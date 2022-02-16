p_list = {
       'a':0,
	'b':0,
	'c':0,
	'd':0,
	'e':0,
	'f':0,
	'g':0,
	'h':0,
	'i':0,
	'j':0,
	'k':0,
	'l':0,
	'm':0,
	'n':0,
	'o':0,
	'p':0,
	'q':0,
	'r':0,
	's':0,
	't':0,
	'u':0,
	'v':0,
	'w':0,
	'x':0,
	'y':0,
	'z':0}
words= []
import operator
with open('wordle-allowed-guesses.txt', 'r') as wlist:
    lines = wlist.readlines()
    for word in lines:
        words.append(word[:-1])
print(len(words))
for w in words:
	for i in range(4):
		p_list[w[i]] += 1



depth = 6
words_2=words

def getwords_mowed(words,move):


	t = []
	for w in words:
		if w.find(p_sorted[move][0]) >= 0:
			t.append(w)

	if len(t)==0:

		return getwords_mowed(words,move+1)
	else:
		words = t


	return words

def getwords(depth,words,psorted):
	for m in range(depth):
		print(m)
		print(p_sorted[m][0])
		t = []
		for w in words:
			if w.find(p_sorted[m][0]) >= 0:
				t.append(w)
		print(f't len - {len(t)}')
		if len(t)==0:
			print('calling recursion')
			words= getwords_mowed(words,m+1)

		else:
			words = t

	return words


p_sorted = sorted(p_list.items(),key=operator.itemgetter(1),reverse=True)
print(getwords(depth,words_2))