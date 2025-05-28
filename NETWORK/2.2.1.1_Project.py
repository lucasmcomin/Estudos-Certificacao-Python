import requests
import json



def check_server(cid=None):
    global reply
    try:
        reply  = requests.get('http://localhost:3000/cars2')
        return True
    except requests.RequestException:
        return False

def print_menu():
    print_header()
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
                print("Invalid option try [0..4] number") 
        else:
            print("Invalid option try [0..4] number")


def print_header():
    print("+", "-" * 47, "+")
    print("|\t\t", "Vintage Cars Database", "\t\t", " |")
    print("+", "-" * 47, "+")

def print_car(car):
    pass

def list_cars():
    
    if reply:
        pass
    else:
        print("Lista Vazia")

def name_is_valid(name):
# checks if name (brand or model) is valid;
# valid name is non-empty string containing
# digits, letters and spaces;
# returns True or False;
    pass
def enter_id():
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);
    pass

def enter_production_year():
# allows user to enter car's production year and checks if it's valid;
# valid production year is an int from range 1900..2000;
# returns int or None  (if user enters an empty line);
    pass

def enter_name(what):
# allows user to enter car's name (brand or model) and checks if it's valid;
# uses name_is_valid() to check the entered name;
# returns string or None  (if user enters an empty line);
# argument describes which of two names is entered currently ('brand' or 'model');
    pass
def enter_convertible():
# allows user to enter Yes/No answer determining if the car is convertible;
# returns True, False or None  (if user enters an empty line);
    pass
def delete_car():
# asks user for car's ID and tries to delete it from database;
    pass

def input_car_data(with_id):
# lets user enter car data;
# argument determines if the car's ID is entered (True) or not (False);
# returns None if user cancels the operation or a dictionary of the following structure:
# {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    pass

def add_car():
# invokes input_car_data(True) to gather car's info and adds it to the database;
    pass

def update_car():
# invokes enter_id() to get car's ID if the ID is present in the database;
# invokes input_car_data(False) to gather new car's info and updates the database;
    pass

while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)

    print_menu()
    choice = read_user_choice()

    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
