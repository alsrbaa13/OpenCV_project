import xml.etree.ElementTree as ET
import sys
import numpy

def getMusicSheet(name, tempo):

	Music = [] #include chord and pitch
	Sheet = [] #include time
	note_length = ["whole", "half", "quarter", "eighth", "16th", "32nd", "64th"]


	doc = ET.parse(name)

	root = doc.getroot() #load xml

	version_Test = root.findtext("programVersion")

	num = 0
	code = 0x00
	pitch = 0
	time = 0
	tempo = int(tempo)

	for child in root.iter():

		if child.get("number") is not None:
			print("=============================")
			print("Measure: ",child.get("number"))
			num = num+1

		if child.tag == "Chord" is not None:
			print("chord")
			code = code + 0x80

		elif child.tag == "Rest" is not None:
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
			if i == "measure":
				i = "whole"
			time = tempo / pow(2, note_length.index(i))
			if child.findtext("dots") is not None:
				time *= 1.5
			print("second: ", time)
			Sheet.append(int(round(time * 1000, 4)))

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
	
	if len(sys.argv) is 1:
  		print("you enter few option")
  		print("1. file name, 2.song's tempo")

	name = sys.argv[1]
	tempo = sys.argv[2]
	getMusicSheet(name, tempo)
	
