import pandas as pd


read1 = pd.read_excel('excelbol_xmlbe/adat1.xlsx')
print(read1)
toxml = pd.DataFrame(read1)

xml_write=open('toxml.xml' 'w').write()
