
class FoodItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Burger(FoodItem):
    def __init__(self, name, price, extras: list) -> None:
        super().__init__(name, price)
        self.extras = extras

class Drink(FoodItem):
    def __init__(self, name, price, extras: list, ice: bool) -> None:
        super().__init__(name, price)
        self.extras = extras
        self.ice = ice
class Side(FoodItem):
    pass

class Combo(FoodItem):
    pass


class Order:
    def __init__(self,customer):
        self.name = customer
        self.struct = []
    def add(self,item):
        self.struct.append(item)
    def cancel(self):
        self.struct.clear()


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