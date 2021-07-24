N = int(input())

def count_of_attr(root):
    count = len(root.attrib)
    for child in root:
        count += count_of_attr(child)
    return count

import xml.etree.ElementTree as etree
count = 0
xml = ''
for i in range(N):
    xml += input()

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
count = count_of_attr(root)
    
print(count)