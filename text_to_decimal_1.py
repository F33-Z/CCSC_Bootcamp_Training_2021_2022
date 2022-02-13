msg = "Testing RSA !!"

m = 0
for i in range (len(msg)):
	print(msg[i]+"*256**"+str(len(msg)-(i+1))+" + ", end="")
	m += ord(msg[i])*(256**(len(msg)-(i+1)))

print("\nm=" + str(m))