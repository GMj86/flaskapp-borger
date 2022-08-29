## FoodInfo
class FoodItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return self.name + ' : '+ str(self.get_price())        


class Burger(FoodItem):
    # def __init__(self, name, price, extras: list) -> None:
    #     super().__init__(name, price)
    #     self.extras = extras
    pass

class Drink(FoodItem):
    # def __init__(self, name, price, extras: list, ice: bool) -> None:
    #     super().__init__(name, price)
    #     self.extras = extras
    #     self.ice = ice
    pass
class Side(FoodItem):
    pass

class Combo(FoodItem):
    pass


class Order:
    def __init__(self,customer):
        self.name = customer
        self.struct = []

    def add(self,item: FoodItem):
        self.struct.append(item)

    def cancel(self):
        self.struct.clear()

    def get_items(self):
        return self.struct

    def get_item(self, index: int) -> FoodItem:
        return self.struct[index]
    
    ##
    def get_total(self) -> float:
        x = 0
        for item in self.struct:
            x += item.get_pPrice()
        return x


# def user_input_burger():
#     b = Burger()
#     #ask user for input and store it in burger object 
#     return b

# def user_input_drink():
#     d = Drink()
# #ask user for input and store it in drink object 
#     return d

# def user_input_side(): 
#     s = Side()
#     #ask user for input and store it in side object 
#     return s

# def user_input_combo():
#     c = Combo()
#     #ask user for input and store it in combo object
#     #a combo must include one burger, one side, and one drink 
#     return c

# def take_order():
#     # UI
#     # ask user for name for the order
#     # repeat taking order until client is done 
#     # #display order details
#     # display a thank you message print("Welcome to Burger Shop")
#     pass
# take_order()