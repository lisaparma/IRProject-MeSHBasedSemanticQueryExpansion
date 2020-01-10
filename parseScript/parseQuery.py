def parse(filepath):
	newFile = open(filepath+"Parsed","w")
	with open(filepath, "r") as fp:
		line = fp.readline()
		while line:
			if("<num>" in line):
				newFile.write(line.rstrip("\n")+"</num>\n")
				line = fp.readline()
			if("<title>" in line):
				newFile.write(line.rstrip("\n")+"</title>\n")
				line = fp.readline()
			if("<desc>" in line):
				newFile.write(line)
				line = fp.readline()
				newFile.write(line.rstrip("\n") + "</desc>\n")
				line = fp.readline()
			else:
				newFile.write(line)
				line = fp.readline()
	newFile.close()

def main():
	path=input("Enter filepath: ")
	parse(path)

if __name__ == '__main__':
    main()
