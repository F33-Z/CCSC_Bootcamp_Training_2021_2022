m = 0
hexa = hex(m)[2:]
msg = ""

for i in range(len(hexa)//2):
	msg += chr(int(hexa[i*2:i*2+2],16))

print(msg)