def parse(filepath):
	newFile = open(filepath+"Parsed","w")
	with open(filepath, "r") as fp:
		line = fp.readline()
		while line:
			if(".I" in line):
				newFile.write("<DOC><DOCNO>"+line[3:].rstrip("\n")+"</DOCNO>")
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


def main():
	path=input("Enter filepath: ")
	parse(path)

if __name__ == '__main__':
    main()


					
   

	
	