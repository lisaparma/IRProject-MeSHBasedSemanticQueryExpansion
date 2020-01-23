from MeSH import MeSH

def findPreferredTerm(concept):
    for term in concept["termlist"]:
        if term["preferred"] == "Y":
            return term["name"]
    print("ERROR: preferref term in " + concept["name"] + " not found !!!")
    return None


def findPreferredConcept(descriptor):
    for concept in descriptor:
        if descriptor[concept]["preferred"] == "Y":
            return descriptor[concept]["name"]
    print("ERROR: preferred concept in " + descriptor["name"] + " not found !!!")
    return None


def main():

    mesh = MeSH("desc2020.xml")

    data = mesh.map
    
    with open("moreWordsInQueries", "r") as fp:
        line = fp.readline()
        while line:
            word = line.replace("\n",'')

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
                        termsToAdd.append(prefTerm)
                                             
                        # word is also in concept name ?
                        if word in data[descriptor][concept]["name"]:
                            findConcept = True
                            

                if findConcept == True:
                    prefConcept = findPreferredConcept(data[descriptor])
                    conceptsToAdd.append(prefConcept)

            line = fp.readline()
            print("--> " + word)
            print("TERMS:")
            for term in termsToAdd:
                print("\t" + term)

            print("CONCEPTS:")
            for concept in conceptsToAdd:
                print("\t" + concept)
  
    
if __name__=="__main__": 
    main() 
    
