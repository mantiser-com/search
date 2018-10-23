from gsearch import searchGoogle
import time




time.sleep(15)

def DotheSearch(searchlist):
	for words in searchlist:
		print(words.encode('utf-8'))
		searchGoogle(words)
		time.sleep(10)



first = 'first.txt'
secound = 'secund.txt'  
searchlist_row=[]
with open(first,encoding="utf8") as fp:  
	fline = fp.readline()
	cnt = 1
	while fline:
		with open(secound,encoding="utf8") as sp:  
			sline = sp.readline()
			scnt = 1
			while sline:
				sline = sp.readline()
				scnt += 1
				searchlist_row.append(fline.strip()+" "+sline.strip())
		fline = fp.readline()
		cnt += 1
DotheSearch(searchlist_row)
