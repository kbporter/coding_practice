import xml.etree.ElementTree as ET
tree = ET.parse('countrytest.xml')
root = tree.getroot()
import csv

file_data = open('countrytest.csv', 'w') #, encoding='utf8'
csvwriter = csv.writer(file_data)

level0 = 0
# level2 = 0
while level0 < len(root):
    header = []
    content = []
    level1 = 0 
    fieldname = root[level0].tag
    fieldcontent = root[level0].text
    header.append(fieldname)
    content.append(fieldcontent)
    
    while level1 < len(root[level0]):
        fieldname = root[level0][level1].tag
        fieldcontent = root[level0][level1].text
        header.append(fieldname)
        content.append(fieldcontent)
        level1 += 1
    
    if level0 == 0 & level1 ==0:
        csvwriter.writerow(header)
    
    csvwriter.writerow(content)

    level0 += 1

file_data.close()