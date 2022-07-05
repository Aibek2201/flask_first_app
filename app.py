from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
import yaml, secrets

app = Flask(__name__)
Bootstrap(app)
secret = secrets.token_urlsafe(32)

#DB config
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key = secret
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            form = request.form
            name = form['name']
            age = form['age']
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO employee(name, age) VALUES(%s, %s)",(name,age))
            mysql.connection.commit()
            flash("You data is succesfully added", "success")
        except:
            flash("The inserting is failed!", "danger")
    return render_template('index.html')

@app.route('/employees')
def employees():
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT * FROM employee")
    if result_value > 0:
        employees = cursor.fetchall()

        return render_template('employees.html', employees = employees)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
