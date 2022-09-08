admin_info={"Janeshwar":"J"}
menu_list={1:{'foodId':1,'Name':'Manchurian','Quantity':200,'Price':130,'Discount':9,'Stock':350},
           2:{'foodId':2,'Name':'Pizza','Quantity':175,'Price':1000,'Discount':71,'Stock':125},
           3:{'foodId':3,'Name':'muffins','Quantity':800,'Price':20,'Discount':10,'Stock':80},
           }

def add_food_item():
    item_name=input("Enter food item Name ")
    item_id=int(input("Enter the item idL: "))
    item_quantity = int(input("Enter food item Quantity "))
    item_price = int(input("Enter food item Price "))
    item_discount = int(input("Enter food item Discount "))
    item_stock = int(input("Enter food item Stock "))
    
    menu_list[item_id]={'foodId':item_id,'Name':item_name,
                            'Quantity':item_quantity,
                            'Price':item_price,
                            'Discount':item_discount,
                            'Stock':item_stock
                            }
    print("successfully done")
    

def edit_food_item():
    item_id=int(input("Enter the item_id you want to edit"))
    item_name = input("Enter food item Name ")
    item_quantity = int(input("Enter food item Quantity "))
    item_price = int(input("Enter food item Price "))
    item_discount = int(input("Enter food item Discount "))
    item_stock = int(input("Enter food item Stock "))
    menu_list[item_id]['Name']=item_name
    menu_list[item_id]['Quantity']=item_quantity
    menu_list[item_id]['Price'] = item_price
    menu_list[item_id]['Discount'] = item_discount
    menu_list[item_id]['Stock'] = item_stock
    print("&&&#edited Done&&&")
    return menu_list


def show_menu_item():
    print("***FOOD APP***")
    for i in menu_list:
        print("item Name:",menu_list[i]["Name"])
        print("price:",menu_list[i]["Price"])

def removing_food_item():
    d=int(input("Enter the item id you want to remove"))
    menu_list.pop(d)
    print("remove item successfully")
    return menu_list
        
        

    
        
    
        

    
    
