import operator

inp = 'realo'
ans = 'knife'
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
with open('wordle-allowed-guesses.txt','r') as wlist:
       lines = wlist.readlines()
       for word in lines:
              words.append(word[:-1])
print(len(words))
for w in words:
       for i in range(4):
              p_list[w[i]]+=1
print(p_list)
p_sorted = sorted(p_list.items(),key=operator.itemgetter(1),reverse=True)
print(p_sorted)
print('________________STAGE 1_______________')
#stage1
words_a=[]
words_e=[]
words_o=[]
words_l=[]
words_r=[]
for w in words:
       if w.find('a') >=0:
              words_a.append(w)
for w in words_a:
       if w.find('e') >=0:
              words_e.append(w)
for w in words_e:
       if w.find('o') >=0:
              words_o.append(w)
for w in words_o:
       if w.find('l') >=0:
              words_l.append(w)
for w in words_l:
	if w.find('r') >=0:
		words_r.append(w)

print(len(words_a))
print(len(words_e))
print(len(words_o))
print(len(words_l))
print(words_r)

#stage2
print('________________STAGE 2_______________')
inpos = []
inword={'r':0,'a':2,'o':4}
bans=['e','l']
words_2=words
depth = 5-len(inword)
print(f'Depth: {depth}')

for b in bans:
	t=[]
	for w in words_2:
		if w.find(b) < 0:
			t.append(w)
	words_2=t
	t=[]
for i in inword:
	t=[]
	for w in words_2:
		if w.find(i)>=0 and w.find(i) !=inword[i]:
			t.append(w)
	words_2=t
	t=[]
print(len(p_list))
for b in bans:
	p_list.pop(b)
for i in inword:
	p_list.pop(i)
print(len(p_list))
print(len(words_2))
w_next = words_2
p_sorted = sorted(p_list.items(),key=operator.itemgetter(1),reverse=True)
print(p_sorted[0],p_sorted[1])
for i in range(depth-1):
	t =[]
	for w in words_2:
		if w.find(p_sorted[i][0])>=0:
			t.append(w)
	words_2 = t
	t=[]
print(words_2)



#stage3
print('________________STAGE 3_______________')
inpos = {'a':0,'r':1}
inword={'r':0,'a':2,'o':3}
bans=['i','t']
words_2=w_next
depth = 0
if len(inpos)==0 and len(inword)==0:
	depth=5
if len(inpos)==0 and len(inword)>0:
	depth = 5-len(inword)
if len(inpos)>0 and len(inword)==0:
	depth = 5-len(inpos)
if len(inpos)>0 and len(inword)>0:
	depth = len(inword)+ len(inpos)
	for ip in inpos:
		if ip in inword:
			print(ip)
			depth -=1
	depth= 5- depth
print(f'Depth: {depth}')

for b in bans:
	t=[]
	for w in words_2:
		if w.find(b) < 0:
			t.append(w)
	words_2=t
	t=[]
for i in inpos:
	t=[]
	for w in words_2:
		if w.find(i) == inpos[i]:
			t.append(w)
	words_2=t
	t=[]
for i in inword:
	t=[]
	for w in words_2:
		if w.find(i)>=0 and w.find(i) !=inword[i]:
			t.append(w)
	words_2=t
	t=[]
print(len(p_list))
for b in bans:
	p_list.pop(b,None)
for i in inword:
	p_list.pop(i,None)
print(len(p_list))
print(len(words_2))
print(words_2)
p_sorted = sorted(p_list.items(),key=operator.itemgetter(1),reverse=True)
print(p_sorted)
mem=[]
for i in range(depth):
	t =[]
	for w in words_2:
		for m in range(len(p_sorted)):
			if w.find(p_sorted[m][0])>=0:
				t.append(w)
	words_2 = t
	mem.append(t)
	t=[]
print(mem)



