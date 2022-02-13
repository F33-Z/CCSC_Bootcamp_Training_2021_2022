msg = ""

hexa = ""
for i in range (len(msg)):
	print(hex(ord(msg[i]))[2:], end="")
	hexa += hex(ord(msg[i]))[2:]

print("\n" + str(int(hexa,16)))