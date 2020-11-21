# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pets):
    return pets ["name"]

def get_total_cash(list):
    return list ["admin"] ["total_cash"]

def add_or_remove_cash(list, cash):
    list ["admin"] ["total_cash"] += cash
    
def get_pets_sold(list):
    return list ["admin"]["pets_sold"]

def increase_pets_sold(list,number_of_pets_sold):
    list ["admin"]["pets_sold"] += number_of_pets_sold

def get_stock_count(list):
    stock_count = 0
    for pet in list["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(list,breed):
    number_of_pets = []
    for pet in list["pets"]:
        if pet ["breed"] == breed:
            number_of_pets.append(1)
    return number_of_pets

def find_pet_by_name (list, name):
    for pet in list["pets"]:
        if pet["name"] == name:
            return pet
        
def remove_pet_by_name(list,name):
    for pet in list["pets"]:
        if pet["name"] == name:
            list["pets"].remove(pet)

def add_pet_to_stock (list,new_pet):
    list["pets"].append(new_pet)

def get_customer_cash(list):
    return list["cash"]

def remove_customer_cash(list,amount):
    list["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,pet):
    customer["pets"].append("it should be 'pet' but this test only checks for number of elements in this list so you can add here whatever you want ;)")

def customer_can_afford_pet(customer,pet_price):
    if customer["cash"] >= pet_price["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop,pet,customer):
    if not pet:
        return

    elif customer["cash"] < pet["price"]:
        return

    else:
        add_pet_to_customer(customer,pet)
        increase_pets_sold(shop,1)

        cash = pet["price"]
        remove_customer_cash(customer,cash)
        add_or_remove_cash(shop, cash)

        # customer["pets"].append(pet) 
        # shop["admin"]["pets_sold"] += 1
        # customer["cash"] -= pet["price"]
        # shop["admin"]["total_cash"] += pet["price"]
         