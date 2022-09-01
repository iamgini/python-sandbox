#!/usr/bin/env python3
# A script to manage dictionary items

import json


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
        delete_cars()
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
            db_file = open(database_file, 'r')
            current_car_list = db_file.read()
            db_file.close()
            if current_car_list == "":
                car_list = {}
            else:
                car_list = json.loads(current_car_list)
                
            
            print(car_list)
            #dict2 = {car_model_name.replace(" ","_"):{"model": car_model_name, "year": car_make_year}}


            #dict2 = { "car_list": { "brand1": [ { "model_name": "hello", "year": 2022},{"model_name": "hai", "year": 2021 }]}}
            # car_list = { car_model_name.replace(" ","_"): { "model_name": car_model_name.replace(" ","_"), "year": int(car_make_year), "brand": car_brand_name_selected}}
            # dict2 = { "car_list": { car_brand_name_selected: [ { "model_name": car_model_name.replace(" ","_"), "year": int(car_make_year)}]}}
            # print(car_list)

            # if 'brand1' in car_list:
            #     print("brand1")
            # else:
            #     car_list.update({'brand1':{}})

            # if 'model1' in car_list:
            #     print("model1")
            # else:
            #     car_list['brand1'].update({'model1':{}})
            # print(car_list)
            


            # dict3 = { "car_list": { "newbrand": [ { "model_name": car_model_name.replace(" ","_"), "year": int(car_make_year)}]}}
            # dict2 = { "car_list": { car_brand_name_selected: [ { "model_name": car_model_name.replace(" ","_"), "year": int(car_make_year)}]}}
            #car_list[car_brand_name_selected]["model_name"] = car_model_name.replace(" ","_")
            #car_list[car_brand_name_selected]["year"] = car_make_year
            
            # dict2({ "car_list": { "newbrand": [ { "model_name": car_model_name.replace(" ","_"), "year": int(car_make_year)}]}})
            # new_value = { "brand1": { "model2": { "model_name": "hello", "year": 2022 }}}
            new_value = { car_model_name.replace(" ","_"): { "model_name": car_model_name, "year": int(car_make_year), "brand": car_brand_name_selected}}
            # { "brand1": [{ "model_name": "hello", "year": 2022 }]}
            print(new_value)

            car_list.update(new_value)

            print(car_list)

            # new_value = { "brand1": { "model3": { "model_name": "hello2", "year": 2022 }}}
            # # { "brand1": [{ "model_name": "hello", "year": 2022 }]}
            # print(new_value)
            
            # #car_list1 = car_list | new_value
            # car_list.update(new_value)

            # print(car_list)

            # Write to file
            with open(database_file, 'w') as db_file:
                db_file.write(json.dumps(car_list))
            # db_file = open(database_file, 'w')
            # db_file.write(json_dumps(car_list))
            db_file.close()



    else:
        print("Input is out of range, please re-enter: ")
        add_car()


    
      # what the user wants
    # while True:
    #     item = input("Enter the items you wish to add into the shopping cart: ").title()  # what the user wants
    #     if item not in price_list:  # check for correct input
    #             print("The item is not in the list")
    #     else:
    #         quantity = float(input("How many would you like?: "))  # how many user want
    #         print("{:.0f} of {} has been added to the cart!".format(quantity, item))
    #         item_dict[item] = quantity
    #         more_items = input('Would you like to add more? (y/n): ').lower()
    #         if more_items == 'y':
    #             item = input("Enter the items you wish to add into the shopping cart: ").title()  # what the user wants
    #             quantity = float(input("How many would you like?: "))  # how many user want
    #             print(start_menu())
    #              # check if same item is inside cart
    #             if item in item_dict:
    #                 print('Another {:.0f} of {} has been added to the cart!'.format(quantity, item))
    #             else:
    #                 print("{:.0f} of {} has been added to the cart!".format(quantity, item))
    #                 pass
    #         else:
    #             print(start_menu())

# new_blog = open(blog_git_location + article_published_date_for_file + '-' + article_new_blog_file + '.md', "w")
#       new_blog.write(templated_output)
#       new_blog.close()

# ------- add car ------------------
def view_cars():
    print("Car List")
    # Read file and add items
    db_file = open(database_file, 'r')
    car_list = json.loads(db_file.read())
    #current_car_list = db_file.read()
    db_file.close()

    #for idx, cars in current_car_list:
    for idx, car in enumerate(sorted(car_list)):
        print(idx + 1, ":", car)

def delete_cars():
    view_cars()
    car_to_be_deleted = input("Enter the number to delete the car: ")
    db_file = open(database_file, 'r')
    car_list = json.loads(db_file.read())
    #current_car_list = db_file.read()
    db_file.close()
    print(sorted(car_list)[int(car_to_be_deleted)-1])
    #car_name_to_delete = car_list[int(car_to_be_deleted)-1]
    
    car_list.pop(sorted(car_list)[int(car_to_be_deleted)-1], None)
    #del car_list[sorted(car_list)[int(car_to_be_deleted)-1]]
    print(car_list)

    with open(database_file, 'w') as db_file:
        db_file.write(json.dumps(car_list))
    db_file.close()

start_menu()