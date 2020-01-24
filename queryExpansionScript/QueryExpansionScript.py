import sys
from whoosh import qparser
from whoosh.analysis import RegexTokenizer
from whoosh.lang.porter import stem
from whoosh.lang.morph_en import variations
from whoosh.analysis import StopFilter

from MeSH import MeSH

data = MeSH("desc2020.xml").map

def findPreferredTerm(concept):
    for term in concept["termlist"]:
        if term["preferred"] == "Y":
            return term["name"]
    print("ERROR: preferred term in " + concept["name"] + " not found !!!")
    return None


def findPreferredConcept(descriptor):
    for concept in descriptor:
        if descriptor[concept]["preferred"] == "Y":
            return descriptor[concept]["name"]
    print("ERROR: preferred concept in " + descriptor["name"] + " not found !!!")
    return None

def mesh(word):
    termsToAdd = []      # Array to fill with terms to add to query (point 3)
    conceptsToAdd = []   # Array to fill with concepts to add to query (point 4)

    for descriptor in data.keys():

        findConcept = False
        for concept in data[descriptor]:
            findTerm = False
            # word is in TermList ?
            for term in data[descriptor][concept]["termlist"]:
                if term["name"].startswith(word):
                    findTerm = True

            if findTerm == True:
                prefTerm = findPreferredTerm(data[descriptor][concept])
                for part in prefTerm.replace(",", "").split(" "):
                    termsToAdd.append(part)
                                     
                # word is also in concept name ?
                if word in data[descriptor][concept]["name"]:
                    findConcept = True
                    

        if findConcept == True:
            prefConcept = findPreferredConcept(data[descriptor])
            for part in prefConcept.replace(",", "").split(" "):
                conceptsToAdd.append(part)
    '''
    print("--> " + word)
    print("TERMS:")
    for term in termsToAdd:
        print("\t" + term)

    print("CONCEPTS:")
    for concept in conceptsToAdd:
        print("\t" + concept)
    '''
    return (termsToAdd, conceptsToAdd)

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
    return return_list

def doExpansion(query):
    words = queryindex(query)
    terms = []
    concepts = []
    for word in words:
        termsToAdd, conceptsToAdd = mesh(word)
        terms = terms + termsToAdd
        concepts = concepts + conceptsToAdd
    return ' '.join(list(set(terms)))


def main():
    print("\n\n")
    newFile = open("queryExpansioned","w")
    with open("testquery", "r") as fp:
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
    
