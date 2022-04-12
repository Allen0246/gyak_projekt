from sqlite3 import Row
import pandas as pd

# beolvassa az excel file-t
df = pd.read_excel('adat1.xlsx')
print(df)

#csinál egy függvényt amiben betölti az adatok egy xml fájlba
def to_xml(df):
    def row_xml(row):
        xml = ['<item>']
        for i ,col_name in enumerate(row.index):
            xml.append(' <{0}>{1}</{0}>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)
    res='\n'.join(df.apply(row_xml, axis=1))
    return(res)
to_xml(df)

    # elvileg létrekéne hozza az xml fájlt
with open('df.XML','w') as file:
     file.write(to_xml(df))
