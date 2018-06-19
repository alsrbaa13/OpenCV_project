import xml.etree.ElementTree as ET

def getMusicSheet(tempo):

	Music = [] #include chord and pitch
	Sheet = [] #include time

	doc = ET.parse('Hes_a_pirate.mscx')

	root = doc.getroot() #load xml

	version_Test = root.findtext("programVersion")

	num = 0
	code = 0x00
	pitch = 0
	time = 0

	for child in root.iter():

		if child.get("number") is not None:
			print("=============================")
			print("Measure: ",child.get("number"))
			num = num+1

		if child.findtext("Chord") is not None:
			print("chord")
			code = code + 0x10

		elif child.findtext("Rest") is not None:
			print("rest")
			code = code + 0x00		

		if child.findtext("pitch") is not None:
			print("pitch: ",child.findtext("pitch"))
			pitch = int(child.findtext("pitch"))
			code = code + pitch
			print("code:",hex(code))
			Music.append(code)
			code = 0x00

		if child.findtext("durationType") is not None:
			print("durationType: ",child.findtext("durationType"))
			i = child.findtext("durationType")
			if i == 'quarter':
				time = tempo / 4
			elif i == 'half':
				time = tempo / 2
			elif i == 'eighth':
				time = tempo / 8
			else:
				time = tempo
			print("second: ", time)
			Sheet.append(time)

	file = open("D:/download/microprocess_teamproject/sheet.txt", 'w')
	
	data = "chord\n"
	file.write(data)
	for i in Music:
		data = "%d\n" % i
		file.write(data)

	data = "time\n"
	file.write(data)	
	for i in Sheet:
		data = "%d\n" % i
		file.write(data)

	file.close()

if __name__ == "__main__":
	tempo = int(input("enter the tempo: "))
	print(type(tempo))
	getMusicSheet(tempo)
	
