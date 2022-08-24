from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

struct = []


@app.route('/')
def index():
    return render_template('index.html', struct=struct)

@app.route('/gateway', methods=['GET','POST'])
def gateway():
    if request.method == 'POST':
        title = request.form['title']
        
        if not title:
            flash("Title required")

        else:
            struct.append(title)

    if request.method() == 'POST':
        if 'clear' in request.form:
            struct.clear()

    return render_template('gateway.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
