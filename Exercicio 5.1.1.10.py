from datetime import datetime
import time

def get_instantiation_time(self):

    return self.instantiation_time


class My_Meta(type):

    list = []

    def __new__(mcs, name, bases, dictionary):
        My_Meta.list.append(name)

        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time

        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now().strftime('%H:%M:%S')
        time.sleep(2)
        return obj
    

class Pessoa(metaclass=My_Meta):

    def __init__(self):
        print("Pessoa nova em folha!!")


class Carro(metaclass=My_Meta):

    def __init__(self):
        print("Carro novo em folha!!!")

class Casa(metaclass=My_Meta):

    def __init__(self):
        print("Casa nova em folha!!!!")


p = Pessoa()
print(p.get_instantiation_time())


c = Carro()
print(c.get_instantiation_time())


ca= Casa()
print(ca.get_instantiation_time())


print(My_Meta.list)