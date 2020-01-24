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
            name_descriptor = descriptor.find('DescriptorName/String').text.lower()
            concepts = {}
            for concept in descriptor.iterfind('ConceptList/Concept'):
                name_concept = concept.find('ConceptName/String').text.lower()
                c_preferred = concept.get('PreferredConceptYN')
                relationtype = None
                if c_preferred != 'Y':
                    relationtype = concept.find('ConceptRelationList/ConceptRelation').get('RelationName')
                termlist = []
                for term in concept.iterfind('TermList/Term'):
                    termlist.append({
                        "name": term.find('String').text.lower(),
                        "preferred": term.get('ConceptPreferredTermYN')
                    })

                concepts[name_concept] = {
                    "name": name_concept,
                    "preferred": c_preferred,
                    "relationtype": relationtype,
                    "termlist": termlist
                }
            data[name_descriptor] = concepts

        self.map = data


    def print(self):
        for descriptor in self.map:
            print(descriptor)
        