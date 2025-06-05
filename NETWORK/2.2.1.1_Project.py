import time
import requests
import json
import sys
key_names = ["id", "brand", "model", "year", "convertible"]
key_widths = [10, 15, 10, 7, 12]


#check server status
def check_server(cid=None):
   
    try:
        reply  = requests.get('http://localhost:3000/cars')
        
    except requests.RequestException:
        return False
    else:
        return True
    

#main menu
def print_menu():
    print("+", "-" * 47, "+")
    print("|\t\t", "Vintage Cars Database", "\t\t", " |")
    print("+", "-" * 47, "+")
    print("M E N U")
    print("=" * 7)
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("0. Exit")



def read_user_choice():
    choice = ""
    while True:
        choice = input("Enter your choice (0..4): ")

        if choice.isnumeric():
            if int(choice) < 5:
                return choice
            else:
                print("***Invalid option try [0..4] number***") 
        else:
            print("***Invalid option try [0..4] number***")


#print header of car list [id, brand, model, year, convertible]
def print_header():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


#print all stored cars
def print_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()
    



def list_cars(flag):
    
    try:
        #acessa o servidor para carregar json
        reply  = requests.get('http://localhost:3000/cars', headers={'Connection': 'Close'})

    except requests.RequestException:
        print('***Communication error***')
    else:
        #if json load ok
        if reply.status_code == requests.codes.ok:
            #if list is not empty
            if reply.json() !=[]:
                #print header and cars
                print_header()
                for car in reply.json():
                    print_car(car)
                    
            else:
                #reply is not ok the list is empty
                print("***Empty list***")
        elif reply.status_code == requests.codes.not_found:
            print("***Empty list***")
        if flag:
            input("***Press Enter key to exit***")

def name_is_valid(name):
    
    if name.find(" ") != -1:
        name.replace(" ", "")
   
    if name.isalnum():
        return True
    else:
        return False

def enter_name(type):
    while True:
        name = input(f"Car {type} (empty string to exit):")   

        if name_is_valid(name):
            return name
        elif name!="":
            print(f"**Enter a valid {type}**")
        else:
            return None
        
def enter_id():

    while True:
        id = input("Car ID (empty string to exit):")

        if id.isnumeric():
            return id
        elif id != "":
            print("**Incorrect Option**")
        else:
            return None


def enter_production_year():

    while True:
        production_year = input("Car production year (empty string to exit):")

        if production_year.isnumeric():
            
            if int(production_year) >= 1900 and int(production_year) <= 2000:
                return int(production_year)
            else:
                print("**Enter a valid year from 1900 to 2000]**")
        elif production_year != "":
            print("**Please enter just numeric string**")
        else:
            return None

    pass


def enter_convertible():
    while True:
        convertible = input("Is this car convertible? [y/n] (empty string to exit):").lower()
        #convert n and y to false and true
        if convertible[0] == "y":
            return True
        elif convertible[0] == "n":
            return False
        elif convertible !="":
            print("***Incorrect Option***")

        else:
            return None


def delete_car():

    while True:
        id = enter_id()
        if id != None:
            try:
                reply = requests.delete(f'http://localhost:3000/cars/{id}')
            except requests.RequestException:
                print('Communication error')
                break
            else:
                if reply.status_code == requests.codes.ok:
                    print("***Vintage Car Deleted***") 
                    input("***Press Enter key to exit***")
                    break      
                elif reply.status_code == requests.codes.not_found:
                    print("***Car not found, please enter a valid ID***")
        else: 
            break




def get_car_data(num):
    flag = False
    if num == 0:
        while True:
            id = enter_id()
            try:
                reply  = requests.get(f'http://localhost:3000/cars/{id}')
                
            except requests.RequestException:
                print('***Communication error***')
            else:
                if reply.status_code == requests.codes.ok:
                    print("***ID already exists***")
                    time.sleep(1.5)
                    flag = True
                elif reply.status_code == requests.codes.not_found:
                    flag = False
                    break

    else: 
        id = num
        reply  = requests.get(f'http://localhost:3000/cars/{id}')
        sys.argv[0] = reply.json()['brand']
    if id !=None and not flag:
        car_brand = enter_name("brand")
        if car_brand !=None:
            car_model = enter_name("model")
            if car_model != None:
                car_year = enter_production_year()
                if car_year !=None:
                    convertible = enter_convertible()
                    if convertible != None:
                        return {'id': id, 
                                'brand': car_brand,
                                'model': car_model,
                                'year':car_year,
                                'convertible':convertible}

    return None

def add_car():
    list_cars(False)
    new_car =  get_car_data(0)
    if new_car != None:
        
        try: 
            reply = requests.post('http://localhost:3000/cars', headers={'Content-Type': 'application/json'}, data=json.dumps(new_car))
        except requests.RequestException:
            print('Communication error')
        else:
            print("***Vintage Car Stored***")
            input("***Press Enter key to exit***")
    

def update_car():

    list_cars(False)
    while True:
        id = enter_id()
        if id !=  None:
            try:
                reply  = requests.get(f'http://localhost:3000/cars/{id}')
                
            except requests.RequestException:
                print('Communication error')
                break
            else:
                if reply.status_code == requests.codes.ok:
                    car = get_car_data(id)
                    if car != None:
                        try:
                            reply  = requests.put(f'http://localhost:3000/cars/{id}', headers={'Content-Type': 'application/json'}, data=json.dumps(car))
                        except requests.RequestException:
                            print('Communication error')
                        else:
                            print("***Car update successful***")
                            input("***Press Enter key to exit***")
                            break
                            
                    else:
                        break

                elif reply.status_code == requests.codes.not_found:
                    print("***Car not found, please enter a valid ID***")

        else:
            break

def main():
    while True:
        if not check_server():
            print("***Server is not responding - quitting...***")
            time.sleep(3)
            exit(1)

        print_menu()
        choice = read_user_choice()

        if choice == '0':
            print("Bye!")
            exit(0)
        elif choice == '1':
            list_cars(True)
        elif choice == '2':
            add_car()
        elif choice == '3':
            delete_car()
        elif choice == '4':
            update_car()

main()