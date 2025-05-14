import copy

class Delicacy:
    
    def _init_(self, name, price, weight):
        
        self.name = name
        self.price = price
        self.weight = weight
        
    
    def _str_(self):
        return f'name: {self.name} price: {self.price} weight: {self.weight}'
        
        
d = Delicacy("Brigadeiro", 12, 0.3)

b = copy.deepcopy(d)

b.name = "Cup-cake"
c = copy.copy(d)
print(b)


c.price = 24

print(d)
print(c)