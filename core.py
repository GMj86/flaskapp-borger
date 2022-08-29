

class FoodInfo:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : '+ str(self.getprice())


menu = []
def makingmenu(name,costs):
    for i in range(len(name)):
        menu.append(FoodInfo(name[i],costs[i]))
    return menu
    
    



name = ["Cheeseburger","Double Cheeseburger","Bacon Cheeseburger","Chicken Burger","French Fries","Sweet Potato Fries","Curly Fries", "Coke Products", "Lemonade","Sweet Tea","Bubble Tea","Combo"]
costs = [6,7,8,7,3,4,4.50,3,3.50,2,5,17]
print(type(costs))


FoodOrder = makingmenu(name,costs)


n = 1
for el in FoodOrder:
    print(n,'. ',el)
    n = n+1

makingmenu(menu,costs)
men = makingmenu(name,costs)


def cus_order():
    current_order = []
    total = ([])
    tax = total * 2
    while True:
        print("What would you like today? ")
        order = input()
        if order in name:
            current_order.append(order)
        else:
            print("We don't have that")
            continue
        if is_order_complete():
            return current_order
            total = current_order + FoodOrder
            for current_order in FoodOrder:
                print(total)
            
            
        
        

#arr = makingmenu(name,costs)
#cus_order = arr


def is_order_complete():
    print("anything else? yes/no" )
    addfood = input()
    if addfood == "no":
        return True
    elif addfood == "yes":
        return False
    else:
        raise Exception ("invalid input")


def output_order(order_list):
    print("You ordered: ")
    for order in order_list:
        print(order)
    
    
def output_total():
    print("your total is: ")
    for order in menu:
        return order * menu
        print(output_total)
        
        
        
        
def main():
    order = cus_order()
    output_order(order)
    
    
   
if __name__ == "__main__":
    main()
        
        

