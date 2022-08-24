from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

struct = []
btn_count = 0
clear_count = 0

@app.route('/')
def index():
    return render_template('index.html', struct=struct, btn_count=btn_count,clear_count=clear_count)

@app.route('/gateway', methods=['GET','POST'])
def gateway():
    # btn_count = 0
    # clear_count = 0
    if request.method == 'POST':
        title = request.form['title']
        
        if 'submit' in request.form:
            btn_count = btn_count + 1
        # if not title:
        #     flash("Title required")

        struct.append(title)

    # if request.method == 'POST':
        if 'clear' in request.form:
            # btn_count = 0
            # clear_count += 1
            struct.clear()

    return render_template('gateway.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
