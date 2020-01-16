import re
 
terms = {}
numbers = {}
 
meshFile = 'd2020.bin'
with open(meshFile, mode='rb') as file:
    mesh = file.readlines()
 
outputFile = open('mesh.txt', 'w')
 
for line in mesh:
    meshTerm = re.search(b'MH = (.+)$', line)
    if meshTerm:
        term = meshTerm.group(1)
    meshNumber = re.search(b'MN = (.+)$', line)
    if meshNumber:
        number = meshNumber.group(1)
        numbers[number.decode('utf-8')] = term.decode('utf-8')
        if term in terms:
            terms[term] = terms[term] + ' ' + number.decode('utf-8')
        else:
            terms[term] = number.decode('utf-8')
 
meshNumberList = []
meshTermList = terms.keys()
for term in meshTermList:
    item_list = terms[term].split(' ')
    for phrase in item_list:
        meshNumberList.append(phrase)
 
meshNumberList.sort()
 
used_items = set()
for item in meshNumberList:
    if numbers[item] not in used_items:
        outputFile.write(numbers[item] + '\n' + item)
        used_items.add(numbers[item])
    else:
        outputFile.write(item + '\n')
outputFile.close()