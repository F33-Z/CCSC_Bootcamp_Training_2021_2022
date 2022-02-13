m = 1851240778082281348450
i = 0
l = []

while m>0:
	x = m//(256**i)%256
	print(str(x)+"*256**"+str(i)+" + ", end="")
	i += 1
	m -= m%(256**i)
	l.append(chr(x))

print("\n"+"".join(l[::-1]))
