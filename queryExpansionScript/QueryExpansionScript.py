import sys

from whoosh.analysis import RegexTokenizer
from whoosh.lang.porter import stem
from whoosh.analysis import StopFilter

from MeSH import MeSH

data = MeSH("desc2020.xml").map

from Bio import Entrez
Entrez.email = "lisa.parma@studenti.unipd.it"

def isMeSH(word):
    find = False
    handle = Entrez.esearch(db="mesh", term=word)
    record = Entrez.read(handle)

    if u'TranslationStack' in record:
        for x in record[u'TranslationStack']:
            for y in x:
                if y == 'Field':
                    if x[y] == 'MeSH Terms':
                        find = True
    handle.close()
    return find


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
    synonymTermsToAdd = []
    preferredTermsToAdd = []      # Array to fill with terms to add to query (point 3)
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
                for term in data[descriptor][concept]["termlist"]:
                    synonymTermsToAdd.append(term["name"])

                prefTerm = findPreferredTerm(data[descriptor][concept])
                for part in prefTerm.split(", "):
                    preferredTermsToAdd.append(part)
                                     
                # word is also in concept name ?
                if word in data[descriptor][concept]["name"]:
                    findConcept = True

        if findConcept == True:
            prefConcept = findPreferredConcept(data[descriptor])
            for part in prefConcept.split(", "):
                conceptsToAdd.append(part)

    return (synonymTermsToAdd, preferredTermsToAdd, conceptsToAdd)


def queryIndex(query):
    tokenizer = RegexTokenizer()
    return_list = []   
    
    # Removing stop words
    with open("../smartStopList.txt", "r") as fp:
        line = fp.readline()
        words = []
        while line:
            words.append(line.replace('\n', ''))
            line = fp.readline()

    stopper = StopFilter(stoplist=frozenset(words))
    tokens = stopper(tokenizer(query))

    for t in tokens:
        t.text = t.text.lower()  # Converting to lower case
        s = stem(t.text)  # stemming
        if len(s) > 2:
            return_list.append(s)
    return return_list


def doExpansion(query):
    words = queryIndex(query)
    sTerms = []
    pTerms = []
    pConcepts = []
    for word in words:
        find = isMeSH(word)
        if find is True:
            syn_termsToAdd, pref_termsToAdd, pref_conceptsToAdd = mesh(word)
            sTerms = sTerms + syn_termsToAdd
            pTerms = pTerms + pref_termsToAdd
            pConcepts = pConcepts + pref_conceptsToAdd
        else:
            print("NOT")
    listRun2 = ' '.join(list(set(sTerms)))
    listRun3 = ' '.join(list(set(pTerms)))
    listRun4 = ' '.join(list(set(pConcepts)))
    listRun5 = ' '.join(list(set(pTerms + pConcepts)))
    return (listRun2, listRun3, listRun4, listRun5)

def main():
    # Create 3 different file with queries expanded in three different way
    QErun2 = open("QueriesExp-run2", "w")
    QErun3 = open("QueriesExp-run3", "w")
    QErun4 = open("QueriesExp-run4", "w")
    QErun5 = open("QueriesExp-run5", "w")

    with open(sys.argv[1], "r") as fp:

        line = fp.readline()
        while line:
            if "</title>" in line:
                QErun2.write(line[:-9])
                QErun3.write(line[:-9])
                QErun4.write(line[:-9])
                QErun5.write(line[:-9])

                expansion = doExpansion(line[8:-9])
                QErun2.write("\n" + expansion[0] + line[-9:])
                QErun3.write("\n" + expansion[1] + line[-9:])
                QErun4.write("\n" + expansion[2] + line[-9:])
                QErun5.write("\n" + expansion[3] + line[-9:])

                line = fp.readline()
            if "</desc>" in line:
                QErun2.write(line[:-8])
                QErun3.write(line[:-8])
                QErun4.write(line[:-8])
                QErun5.write(line[:-8])

                expansion = doExpansion(line[:-8])
                QErun2.write("\n" + expansion[0] + line[-8:])
                QErun3.write("\n" + expansion[1] + line[-8:])
                QErun4.write("\n" + expansion[2] + line[-8:])
                QErun5.write("\n" + expansion[3] + line[-8:])

                line = fp.readline()
            else:
                QErun2.write(line)
                QErun3.write(line)
                QErun4.write(line)
                QErun5.write(line)
                line = fp.readline()
    QErun2.close()
    QErun3.close()
    QErun4.close()
    QErun5.close()

if __name__== "__main__":
    main()
