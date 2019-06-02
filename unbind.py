print("Server Unbinder (c) Growtopia Noobs")
try:
	f = open("C:\\Windows\\System32\\drivers\\etc\\hosts","r")
	lines = f.readlines()
	f.close()
	f = open("C:\\Windows\\System32\\drivers\\etc\\hosts","w")
	for line in lines:
		if line!="127.0.0.1 growtopia1.com":
			f.write(line)
	print("Unbind successful!")
except:
	try:
		print("Windows hosts failed... Trying linux version (Maybe wine?)")
		f = open("\\etc\\hosts","r")
		lines = f.readlines()
		f.close()
		f = open("\\etc\\hosts","w")
		for line in lines:
			if line!="\n127.0.0.1 growtopia1.com":
				f.write(line)
		print("Unbind successful!")
	except:
		print("Unbind failed...")