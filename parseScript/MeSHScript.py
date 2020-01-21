import xml.etree.ElementTree as ET

#selects the file to parse and sets the root node
tree = ET.parse('desc2020.xml')
root = tree.getroot()

data = {}

for descriptor in root.iter('DescriptorRecord'):
    name = descriptor.find('DescriptorName/String').text
    concepts = []
    terms = []
    for c in descriptor.iterfind('ConceptList/Concept'):
        concepts.append((c.get('PreferredConceptYN'), c.find('ConceptName/String').text))
        for t in c.iterfind('TermList/Term'):
            terms.append(t.find('String').text)
    data[name] = (concepts, terms)

with open('meshParsed.txt', 'w+') as f:
    for k, v in data.items():
        f.write(f'Descriptor: {k}\n')
        f.write('Concepts: '+ str(v[0]) + '\n')
        f.write('Terms: '+str(v[1])+ '\n\n')



