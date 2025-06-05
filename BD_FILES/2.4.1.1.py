
import xml.etree.ElementTree as et

root = et.Element('shop')

category = et.SubElement(root,'category', {'name': 'Vegan Products'})
product1 = et.SubElement(category,'product', {'name': 'Good Morning Sunshine'})
type = et.SubElement(product1, 'type')
type.text = 'Good Morning Sunshine'
producer = et.SubElement(product1, 'producer')
producer.text = 'OpenEDG Testing Service'
price = et.SubElement(product1, 'price')
price.text = '9.90'
currency = et.SubElement(product1, 'currency')
currency.text = 'USD'


product2 = et.SubElement(category,'product', {'name': 'Fantastic Almond Milk'})
type = et.SubElement(product2, 'type')
type.text = 'beverages'
producer = et.SubElement(product2, 'producer')
producer.text = 'Drinks4Coders Inc.'
price = et.SubElement(product2, 'price')
price.text = '19.75'
currency = et.SubElement(product2, 'currency')
currency.text = 'USD'


tree = et.ElementTree(root)
tree.write('store.xml', 'UTF-8', True)
print(tree)