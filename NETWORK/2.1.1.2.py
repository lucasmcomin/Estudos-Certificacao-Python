import json

class Vehicle:

    def __init__(self, rn, year, passanger, mass):
        self.rn = rn
        self.year = year
        self.passanger = passanger
        self.mass = mass
    

    

def encode(v):
        if isinstance(v, Vehicle):
            return v.__dict__
        
    
def decode(j):
    return Vehicle(j['rn'], j['year'], j['passanger'], j['mass'])

print("WHat can I do for you?")
print("1 - Produce a JSON string describing a vehicle")
print("2 - Decode a JSON string into data")

response = input("Your choice:")

if response == "1":
    rn = input("Registration number: ")
    year = input("Year: ")
    passanger = input("Passanger [y/n]: ")
    if passanger == "y":
        passanger = True
    elif passanger =="n":
        passager = False
    
    mass = input("Vehicle mass: ")

    new_car = Vehicle(rn, year, passanger, mass)
    js = json.dumps(new_car, default=encode)
    print(js)

if response == "2":
    jstring = input("Enter a vehicle JSON string: ")
    new_car = json.loads(jstring, object_hook = decode)
    print(new_car.__dict__)

