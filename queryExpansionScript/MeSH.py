import xml.etree.ElementTree as ET

class MeSH:

    def __init__(self, file):
        """
        :param file: path of xml mesh file to parse
        """
        tree = ET.parse(file)
        root = tree.getroot()
        data = {}
        for descriptor in root.iter('DescriptorRecord'):
            id_descriptor = descriptor.find('DescriptorName/String').text.lower()
            concepts = {}
            for concept in descriptor.iterfind('ConceptList/Concept'):
                id_concept = concept.find('ConceptName/String').text
                c_preferred = concept.get('PreferredConceptYN')
                termlist = []
                for term in concept.iterfind('TermList/Term'):
                    termlist.append({
                        "name": term.find('String').text.lower(),
                        "preferred": term.get('ConceptPreferredTermYN')
                    })

                concepts[id_concept] = {
                    "name": id_concept,
                    "preferred": c_preferred,
                    "termlist": termlist
                }
            data[id_descriptor] = concepts

        self.map = data


    def print(self):
        for descriptor in self.map:
            print(descriptor)
        