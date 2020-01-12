"""
Python script that trasforms a text file
with lines with the following format:

	query-id document-id relevance

in a file in which every line has this format:

	query-id 0 document-id relevance

"""

import sys

def parse(filepath):
	newFile = open(filepath+"Parsed","w")
	with open(filepath, "r") as fp:
		line = fp.readline()
		while line:
			str = line.split('\t')
			newLine = str[0] + "\t0\t" + str[1] + "\t" + str[2]
			newFile.write(newLine)
			line = fp.readline()
	newFile.close()

def main(argv):
	path=sys.argv[1]
	parse(path)

if __name__ == '__main__':
    main(sys.argv)

