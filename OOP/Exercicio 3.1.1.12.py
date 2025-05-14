"""class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        print('\tBateries is with {} charge'.format(100/0))
    
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Bateries problem") from e

def circuits_check():
    try:
        print('\Circuits ON'.format(s))
    
    except NameError as e:
        raise RocketNotReadyError("Breaked circuit") from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))"""



class OwnDict(dict):
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
    
    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs):
            self.__setitem__(_key, _val)

    
own_dict = OwnDict()
own_dict[4] = 1
own_dict[2] = 0.5
print(own_dict)