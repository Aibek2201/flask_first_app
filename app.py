from unittest import result
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
Bootstrap(app)

#DB config
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    # cursor.execute("insert into user values(%s)",(['As']))
    # mysql.connection.commit()
    result_value = cursor.execute("select * from user")
    if result_value > 0:
        users = cursor.fetchall()
        print(users)
    return render_template("index.html")
    # return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/css')
def css():
    return render_template("css.html")

if __name__ == '__main__':
    app.run(debug=True,port=5000)
