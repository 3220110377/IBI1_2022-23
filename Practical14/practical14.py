from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd


def childnodes(child_id):
    number = 0
    for term_child in terms:
        id_node_child = term_child.getElementsByTagName("id")[0]
        is_a_nodes = term_child.getElementsByTagName("is_a")
        for is_a_node in is_a_nodes:
            is_a_value = is_a_node.firstChild.nodeValue
            if child_id == is_a_value:
                number += childnodes(id_node_child.firstChild.nodeValue) + 1
    return number  # A recursive algorithm is used to calculate the number of childNodes


data = {'id': [], 'name': [], 'definition': [], 'childNotes': []}
dom = xml.dom.minidom.parse("go_obo.xml")
root = dom.documentElement
terms = root.getElementsByTagName("term")  # Read the file and take out the term
for term in terms:
    id_node = term.getElementsByTagName("id")[0]
    name_node = term.getElementsByTagName("name")[0]
    defstr_node = term.getElementsByTagName("defstr")[0]  # Store id, name and defstr
    childNodes = 0
    if "autophagosome" in defstr_node.firstChild.nodeValue:
        childNodes = childnodes(id_node.firstChild.nodeValue)
        data['id'].append(id_node.firstChild.nodeValue)
        data['name'].append(name_node.firstChild.nodeValue)
        data['definition'].append(defstr_node.firstChild.nodeValue)
        data['childNotes'].append(childNodes)  # If autophagosome exists in defstr,
        # store the above data as temporary data
df = pd.DataFrame(data)
df.to_excel("autophagosome.xlsx", index=False)
