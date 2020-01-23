import sys
from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.lang.porter import stem
from whoosh.lang.morph_en import variations
from whoosh.analysis import StopFilter

def searchMESHConcept(word):
    return "plop"

def inMESH(word):
    return True

def queryindex(query):
    tokenizer = RegexTokenizer()
    return_list = []   
    
    #Removing stop words
    with open("../smartStopList.txt", "r") as fp:
        line = fp.readline()
        words=[]
        while line:
            words.append(line.replace('\n', ''))
            line = fp.readline()

    stopper = StopFilter(stoplist=frozenset(words))
    tokens = stopper(tokenizer(query))

    for t in tokens:
        #converting to lower case
        t.text = t.text.lower()
        #stemming
        s=stem(t.text)
        return_list.append(s)
        #adding variations
        #termVariations = variations(t.text)
        #for u in termVariations:
        #   return_list.append(u)
    return return_list

def doExpansion(query):
    words = queryindex(query)
    concepts = []
    for word in words:
        if(inMESH(word)):
            print(word + " --> in MeSH")
            concept = searchMESHConcept(word)
            print("\tConcept: " + concept)
            concepts.append(concept)
        else:
            print(word + " --> NOT in MeSH")
    conceptsString =' '.join(concepts)
    return conceptsString


def main():
    print("\n\n")
    newFile = open(sys.argv[1]+"QueryExpansion","w")
    with open(sys.argv[1], "r") as fp:
        line = fp.readline()
        while line:
            if("<num>" in line):
                newFile.write(line)
                line = fp.readline()
            if("</title>" in line):
                newFile.write(line[:-9])
                print("--> ESPANSIONE TITOLO")
                print(line[8:-9])
                expansion = doExpansion(line[8:-9])
                print(expansion)
                newFile.write("\n" + expansion + line[-9:])
                line = fp.readline()
            if("</desc>" in line):
                newFile.write(line[:-8])
                print("\n--> ESPANSIONE DESCRIZIONE")
                print(line[:-8])
                expansion = doExpansion(line[:-8])
                print(expansion)
                newFile.write("\n" + expansion + line[-8:])
                line = fp.readline()
            else:
                newFile.write(line)
                line = fp.readline()
    newFile.close()
    print("\n\n")
  
    
if __name__=="__main__": 
    main() 
    
