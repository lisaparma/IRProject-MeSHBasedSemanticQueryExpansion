import sys

def parse(filepath):
	newFile = open(filepath+"Parsed","w")
	with open(filepath, "r") as fp:
		line = fp.readline()
		while line:
			if(line == ".U\n"):
				line1 = fp.readline()
				newFile.write("<DOC><DOCNO>"+line1.rstrip("\n")+"</DOCNO>")
				line = fp.readline()
			if(line == ".T\n"):
				line = fp.readline()
				newFile.write("<TITLE>"+line.rstrip("\n")+"</TITLE>")
			if(line == ".W\n"):
				line = fp.readline()
				newFile.write("<ABSTRACT>"+line.rstrip("\n")+"</ABSTRACT></DOC>\n")
			else:
				line = fp.readline()
	newFile.close()


def main(argv):
	path=sys.argv[1]
	parse(path)

if __name__ == '__main__':
    main(sys.argv)