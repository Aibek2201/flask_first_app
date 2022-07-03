from urllib import request
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        return request.form['password']
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
