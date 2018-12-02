from xml.etree import ElementTree


def xmlTags(xml):
    tree = ElementTree.fromstring(xml)
    tree_dict = {}
    attrib_dict = {}

    def store_tag(tree, indent):
        if tree.tag:
            if tree.tag not in tree_dict.keys():
                tree_dict[tree.tag] = indent
        if tree.attrib:
            for attrib in tree.attrib:
                if tree.tag not in attrib_dict.keys():
                    attrib_dict[tree.tag] = [attrib]
                else:
                    if attrib not in attrib_dict[tree.tag]:
                        attrib_dict[tree.tag].append(attrib)
                        attrib_dict[tree.tag].sort()
        for child in tree:
            store_tag(child, indent + 2)

    store_tag(tree, 0)

    output = []
    for k, v in tree_dict.items():
        indent = '-' * v
        attrib_list = ''
        if k in attrib_dict.keys():
            attrib_list = ', '.join(attrib_dict[k])
        current_output = indent + k + '(' + attrib_list + ')'
        output.append(current_output)

    return output


xml = "<data><animal name=\"cat\"><genus>Felis</genus><family name=\"Felidae\" subfamily=\"Felinae\"/><similar name=\"tiger\" size=\"bigger\"/></animal><animal name=\"dog\"><family name=\"Canidae\" member=\"canid\"/><order>Carnivora</order><similar name=\"fox\" size=\"similar\"/></animal></data>"

print(xmlTags(xml))
# Expected Output:
#
# ["data()",
#  "--animal(name)",
#  "----genus()",
#  "----family(member, name, subfamily)",
#  "----similar(name, size)",
#  "----order()"]
