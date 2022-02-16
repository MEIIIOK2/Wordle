import operator
def getwords_mowed(words,move,psorted):


	t = []
	for w in words:
		if w.find(psorted[move][0]) >= 0:
			t.append(w)

	if len(t)==0:

		return getwords_mowed(words,move+1,psorted)
	else:
		words = t


	return words

def getwords(depth,words,psorted):
	for m in range(depth):

		t = []
		for w in words:
			if w.find(psorted[m][0]) >= 0:
				t.append(w)

		if len(t)==0:

			words= getwords_mowed(words,m+1,psorted)

		else:
			words = t

	return words[0]

def stage(inpos,inword,bans,p_list,words_2):
	if len(inpos) == 0 and len(inword) == 0:
		depth = 5
	if len(inpos) == 0 and len(inword) > 0:
		depth = 5 - len(inword)
	if len(inpos) > 0 and len(inword) == 0:
		depth = 5 - len(inpos)
	if len(inpos) > 0 and len(inword) > 0:
		depth = len(inword) + len(inpos)
		for ip in inpos:
			if ip in inword:
				print(ip)
				depth -= 1
		depth = 5 - depth
	print(f'Depth: {depth}')
	for b in bans:
		t = []
		for w in words_2:
			if w.find(b) < 0:
				t.append(w)
		words_2 = t
		t = []
	for i in inpos:
		t = []
		for w in words_2:
			if w.find(i) == inpos[i]:
				t.append(w)
		words_2 = t
		t = []
	for i in inword:
		t = []
		for w in words_2:
			if w.find(i) >= 0 and w.find(i) != inword[i]:
				t.append(w)
		words_2 = t
		t = []
	print(len(p_list))
	for b in bans:
		p_list.pop(b, None)
	for i in inword:
		p_list.pop(i, None)
	print(len(p_list))
	print(len(words_2))
	words_to_next= words_2
	print(words_2)
	psorted = sorted(p_list.items(), key=operator.itemgetter(1), reverse=True)
	print(psorted)
	words_2 = getwords(depth,words_2,psorted)
	return words_2,psorted,words_to_next

