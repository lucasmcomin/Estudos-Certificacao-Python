import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})


w2 = copy.deepcopy(warehouse)

print('Source list of candies')
for item in warehouse:
    print(item)



print('***********************')

for item in w2:
    price = item['price']
    if item['weight'] > 300:
        item['price'] = price - (price * 0.2)
        
    print(item)