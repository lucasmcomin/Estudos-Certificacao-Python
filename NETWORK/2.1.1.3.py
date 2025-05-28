import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('NETWORK/nyse.xml')
quotes = tree.getroot()

print("-" * 104)
print("|COMPANY", " " * 39,"|", "LAST", " " *6,"|",  "CHANGE", " " * 6, "|", "MIN", " " * 6,"|","MAX", " " * 4, "|")
print("-" * 104)

for quote in quotes:
    print("|",quote.text, " " * (45-len(quote.text)),"|",  quote.attrib['last'], " " * (10-len(quote.attrib['last'])), "|",quote.attrib['change'], 
          " " * (12-len(quote.attrib['change'])),"|", quote.attrib['min'],  " " * (9-len(quote.attrib['min'])), "|",quote.attrib['max'], 
          " " * (7-len(quote.attrib['max'])), "|")
          

print("-" * 104)