from flask import Flask, render_template, request
from core import FoodInfo
from bOrgor import *
app = Flask(__name__)

struct = []
btn_count = 0
clear_count = 0

@app.route('/', methods=['GET','POST'])
def index():
    # return render_template('index.html', struct=struct, btn_count=btn_count,clear_count=clear_count)
    global btn_count

    if request.method == 'POST':
        # if request.form['btTxt submit'] == 'btn':
        #     btn_count+=1

        if 'drink1' in request.form:
            btn_count += 1
            print('drink1 pressed')
        elif 'drink2' in request.form:
            print('drink2 pressed')
        elif 'drink3' in request.form:
            print('drink3 pressed')
        elif 'drink4' in request.form:
            print('drink4 pressed')

        elif 'side1' in request.form:
            btn_count += 1
            print('side1 pressed')
        elif 'side2' in request.form:
            print('side2 pressed')
        elif 'side3' in request.form:
            print('side3 pressed')
        elif 'side4' in request.form:
            print('side4 pressed')

        elif 'burger1' in request.form:
            btn_count += 1
            print('burger1 pressed')
        elif 'burger2' in request.form:
            print('burger2 pressed')
        elif 'burger3' in request.form:
            print('burger3 pressed')
        elif 'burger4' in request.form:
            print('burger4 pressed')

        else:
            print('something not right')
            
    print(btn_count)
    return render_template('some.html', value1=btn_count)

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

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
