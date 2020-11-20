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