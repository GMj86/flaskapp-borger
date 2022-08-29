## GG Solutions INC
# 8/27
##
from flask import Flask, render_template, request
from core import *
from bOrgor import *
app = Flask(__name__)

struct = []

# Where order is declared/created
order = Order("bob")
btn_count = 0
clear_count = 0
"""

< Menu List >
1  .  Cheeseburger : 6
2  .  Double Cheeseburger : 7
3  .  Bacon Cheeseburger : 8
4  .  Chicken Burger : 7
5  .  French Fries : 3
6  .  Sweet Potato Fries : 4
7  .  Curly Fries : 4.5
8  .  Coke Products : 3
9  .  Lemonade : 3.5
10 .  Sweet Tea : 2
11 .  Bubble Tea : 5
12 .  Combo : 17

"""
@app.route('/', methods=['GET','POST'])
def index():
    # return render_template('index.html', struct=struct, btn_count=btn_count,clear_count=clear_count)
    global btn_count, struct, order

    if request.method == 'POST':
## DRINKS
        if 'drink1' in request.form:
            # btn_count += 1
            # print('drink1 pressed')
            order.add(Drink('Coke Products',3))

        elif 'drink2' in request.form:
            # print('drink2 pressed')
            order.add(Drink('Lemonade',3.5))
        elif 'drink3' in request.form:
            # print('drink3 pressed')
            order.add(Drink('Sweet Tea',3))

        elif 'drink4' in request.form:
            # print('drink4 pressed')
            order.add(Drink('Bubble Tea',5))

## SIDES
        elif 'side1' in request.form:
            # btn_count += 1
            # print('side1 pressed')
            order.add(Side('French Fries', 3))
        elif 'side2' in request.form:
            # print('side2 pressed')
            order.add(Side('Sweet Potato Fires',4))
        elif 'side3' in request.form:
            # print('side3 pressed')
            order.add(Side('Curly Fries', 4.5))
        elif 'side4' in request.form:
            # print('side4 pressed')
            order.add(Side('Apple Slices', 2.5))
## BURGERS
        elif 'burger1' in request.form:
            # btn_count += 1
            # print('burger1 pressed')
            order.add(Burger('Cheeseburger',6))
        elif 'burger2' in request.form:
            # print('burger2 pressed')
            order.add(Burger('Double Cheesburger',7))
        elif 'burger3' in request.form:
            # print('burger3 pressed')
            order.add(Burger('Bacon Cheesburger',8))
        elif 'burger4' in request.form:
            # print('burger4 pressed')
            order.add(Burger('Chicken Burger',7))
## CANCEL
        elif 'button2' in request.form:
            order.cancel()
        else:
            print('something not right')
            
    # print(order.get_items())


    ## Where update values will be displayed
    return render_template('some.html', value_1=order.get_printable_items(), value_2=order.get_total(), value_3=order.cancel())

## IGNORE ## For testing
# @app.route('/gateway', methods=['GET','POST'])
# def gateway():
#     global btn_count, clear_count

#     if request.method == 'POST':
#         title = request.form['title']
        
#         if 'burger1' in request.form:
#             btn_count += 1
#         # if not title:
#         #     flash("Title required")

#         struct.append(title)

#     # if request.method == 'POST':
#         if 'clear' in request.form:
#             btn_count = 0
#             clear_count += 1
#             struct.clear()

#     return render_template('gateway.html')
## ###
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
