from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
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
        for term_1 in terms:
            is_a_nodes = term_1.getElementsByTagName("is_a")
            for is_a_node in is_a_nodes:
                is_a_value = is_a_node.firstChild.nodeValue
                if id_node.firstChild.nodeValue == is_a_value:
                    childNodes += 1  # Iterate through all <is_a>, if it matches the id,
                    # then childNodes increment themselves by 1
        data['id'].append(id_node.firstChild.nodeValue)
        data['name'].append(name_node.firstChild.nodeValue)
        data['definition'].append(defstr_node.firstChild.nodeValue)
        data['childNotes'].append(childNodes)  # If autophagosome exists in defstr,
        # store the above data as temporary data
df = pd.DataFrame(data)
df.to_excel("autophagosome.xlsx", index=False)
