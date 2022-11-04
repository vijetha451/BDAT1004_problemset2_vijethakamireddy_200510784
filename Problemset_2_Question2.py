def fileLength(filename):
	#reading data
	try:
		f=open(filename,'r')
		#reading all lines as a list of list
		data=f.readlines()
		#creating a single line from all lines
		line=""
		for i in data:
			line+=i
		result=len(line)
		return result
	except FileNotFoundError:
		return ("File {} not found.".format(filename))

print(fileLength('question2.py'))
print(fileLength('question2_1.py'))

