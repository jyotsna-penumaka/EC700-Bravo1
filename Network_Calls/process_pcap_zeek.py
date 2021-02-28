import os
xx=open("files.txt")
cc=0
for x in xx:
	x=x.rstrip()
	root=x[:-4]
	os.system("zeek -r "+x)
	os.system("mv conn.log "+root+".conn")
	os.system("rm *.log")
	cc=cc+1
	print(cc)
