import operator
import mods
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
with open('wordle-answers-alphabetical.txt','r') as wlist:
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
depth = 6
start_word = mods.getwords(depth,words,p_sorted)
print(f'Your Starting word is: {start_word}')

put = input('Enter inpos letters with positions: ')
put = put.split()
inpos={}
for i in range(0,len(put),2):
	inpos[put[i]] = int(put[i+1])
put = input('Enter inword letters with positions: ')
put = put.split()
inword={}
for i in range(0,len(put),2):
	inword[put[i]] = int(put[i+1])
print(inpos,inword)
bans = input('Input grey letters: ')
bans = bans.split()
suggested_word,p_sorted,words = mods.stage(inpos,inword,bans,p_list,words)
print(suggested_word)
print(p_sorted)
print(words)
print('________________START_______________')
put = input('Enter inpos letters with positions: ')
put = put.split()
inpos={}
for i in range(0,len(put),2):
	inpos[put[i]] = int(put[i+1])
put = input('Enter inword letters with positions: ')
put = put.split()
inword={}
for i in range(0,len(put),2):
	inword[put[i]] = int(put[i+1])
print(inpos,inword)
bans = input('Input grey letters: ')
bans = bans.split()
suggested_word,p_sorted,words = mods.stage(inpos,inword,bans,p_list,words)
print(suggested_word)


