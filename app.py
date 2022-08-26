from flask import Flask, render_template, request, url_for, redirect
from multiprocessing import Value

app = Flask(__name__)

struct = []
btn_count = 0
clear_count = 0

@app.route('/', methods=['GET','POST'])
def index():
    # return render_template('index.html', struct=struct, btn_count=btn_count,clear_count=clear_count)
    global btn_count

    if request.method == 'POST':
        val = request.form.get('burger1')
        if request.form.get('drink1') == 'btn':
            print("pressed")
            btn_count += 1
        elif val != 'btn':
            print('pressed in val==btn')
            btn_count += 10
        else:
            print('something not right')
    print(btn_count)
    return render_template('some.html', btn_count=btn_count)

@app.route('/gateway', methods=['GET','POST'])
def gateway():
    global btn_count, clear_count

    if request.method == 'POST':
        title = request.form['title']
        
        if 'burger1' in request.form:
            btn_count += 1
        # if not title:
        #     flash("Title required")

        struct.append(title)

    # if request.method == 'POST':
        if 'clear' in request.form:
            btn_count = 0
            clear_count += 1
            struct.clear()

    return render_template('gateway.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
