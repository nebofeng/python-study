with open('1.txt','a+') as myfile:
	myfile.seek(0,0)
	for buf in myfile:
		print(buf)
	myfile.write('abc')
#不需要手动的 close

# close()
# flush()