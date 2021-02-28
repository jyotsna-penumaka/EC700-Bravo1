import os
base="https://giantpanda.gtisc.gatech.edu/malrec/newpcaps/"
xx=[]
aa=open("part_a.txt")
for a in aa:
	a=a.rstrip()
	xx.append(a)	
cc=0
for x in xx:
	url=base+x+".pcap"
	print(url)
	os.system("wget "+url)
	cc+=1
	print(cc)
