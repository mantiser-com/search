from gsearch import searchGoogle


first = 'first.txt'
secound = 'secund.txt'  

with open(first) as fp:  
	fline = fp.readline()
	cnt = 1
	while fline:
		with open(secound) as sp:  
			sline = sp.readline()
			scnt = 1
			while sline:
				sline = sp.readline()
				scnt += 1
				searchGoogle(fline.strip()+" "+sline.strip())
		fline = fp.readline()
		cnt += 1