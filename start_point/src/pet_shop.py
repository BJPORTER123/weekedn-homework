# WRITE YOUR FUNCTIONS HERE
# Question 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Question 2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Question 3
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] +=  cash

# Question 4

def get_pets_sold(pet_shop, cash):
    add_or_remove_cash(pet_shop, cash)

# question 5

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# question 6

def increase_pets_sold(pet_shop, sold):
        pet_shop["admin"]["pets_sold"] +=  sold

# question 7

def get_stock_count(pet_shop):
    count = len(pet_shop["pets"])
    return count
            
# Question 8 and 9 
def get_pets_by_breed(pet_shop, breed_of_pet):
    named_breed = []
    for breed in pet_shop["pets"]:
        if breed["breed"] == breed_of_pet:
            named_breed.append(breed)
        
    return named_breed

# Question 10 & # Question 11 (ask question why i had to assign an extra variable)

def find_pet_by_name(pet_shop, name_of_pet):
      for name in pet_shop["pets"]:
        if name["name"] == name_of_pet:
            name_of_pet = name
            return name_of_pet    

# Question 12
def remove_pet_by_name(pet_shop, name_of_pet):
   name_of_pet_to_remove = find_pet_by_name(pet_shop, name_of_pet) 
   pet_shop["pets"].remove(name_of_pet_to_remove)  

# Question 13

def add_pet_to_stock (pet_shop, dict_of_new_pet):
    new_pet_dict = {"name" : "", "pet type" : "", "breed" : "", "price" : ""} 
    dict_copy = new_pet_dict.copy()
    pet_shop["pets"].append(dict_copy)
    get_stock_count(pet_shop)


# Question 14

def get_customer_cash(paying_customer):
    return paying_customer["cash"]

# Question 15

def remove_customer_cash(paying_customer, cash):
    cash_of_customer = get_customer_cash(paying_customer["cash"]) - cash
    return 