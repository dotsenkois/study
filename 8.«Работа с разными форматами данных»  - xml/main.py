import xml.etree.ElementTree as ET

from collections import Counter
temp = []

parser = ET.XMLParser(encoding='UTF-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_items = root.findall("channel/item")
for xmli in xml_items:
    for i in xmli.find('description').text.split():
        if len(i) > 6:
            temp.append(i)

sorted_temp = sorted(temp)
count_of_entres = Counter(sorted_temp)
print('Топ-10 самых употребляемых слов в ленте новостей длиннее 6 символов:')
for i in count_of_entres.most_common(10):
    print(i[0])
