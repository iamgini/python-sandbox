#!/usr/bin/env python3
# A script to manage dictionary items

database_file = "car_database.db"
database_dict = {}
car_brands = ['Toyota', 'Audi', 'BMW'] 

# -------------- menu ------------------
def start_menu():
    print("\nPlease select the menu")
    print("1. View Cars")
    print("2. Add Car")
    print("3. Delete Car")
    print("q. Quit the program safely")
    menu_selected = input("\nMake your selection: ")
    if menu_selected == "1": 
        view_cars()
        start_menu()
    elif menu_selected == "2":
        add_car()
        start_menu()
    elif menu_selected == "3":
        delete_car()
        start_menu()
    elif menu_selected == "q":
        print("\nThank you!\n")
        exit()
    else:
        print("Input is out of range, please re-enter: ")
        start_menu()

# ------- add car ------------------
def add_car():

    print("Available Models:")
    for idx, car_brand in enumerate(sorted(car_brands)):
        print(idx + 1, ":", car_brand)
    car_brand_selected = input("Select Car Brand: ")
    
    if int(car_brand_selected) < len(car_brands) and int(car_brand_selected) > 0:
        # print("ok")
        
        car_brand_name_selected = sorted(car_brands)[int(car_brand_selected) - 1]
        print("\nEnter more details for the selected brand " + car_brand_name_selected)
        car_model_name = input("Car Model Name: ")
        if car_model_name != "":
            car_make_year = input("Year of make: ")

            # Read file and add items
            # db_file = open(database_file, 'r')
            # print(db_file.read())
            # db_file.close()


    else:
        print("Input is out of range, please re-enter: ")
        add_car()

# ------- add car ------------------
def view_cars():
    print("Car List")

start_menu()