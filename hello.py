from flask import Flask,render_template,request
from werkzeug.datastructures import ImmutableMultiDict
import sqlite3
taal_dict={
    '1':'Dhaa',
    '2':'Dhin',
    '3':'Ga',
    '4':'Ka',
    '5':'Kat',
    '6':'Naa',
    '7':'Na',
    '8':'Taa',
    '9':'Tak',
    '10':'Tee',
    '11':'TiraKita',
    '12':'Tita',
    '13':'Tin',
    '14':'Too'
}
app = Flask(__name__)
@app.route('/register',methods = ['POST', 'GET'])
def register():
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS Registered_Users(NAME TEXT, EMAIL TEXT,PASSWORD TEXT)")
    def data_entry(name,email,password):
        c.execute("INSERT INTO Registered_Users (NAME, EMAIL, PASSWORD) VALUES (?, ?, ?)",
            (name, email, password))
        conn.commit()
        c.close()
        conn.close()
    if request.method == 'POST' :
        name= request.form['namevar']
        email=request.form['emailid']
        password=request.form['passwd']
        conn = sqlite3.connect('registrations.db')
        c = conn.cursor()
        create_table()
        data_entry(name,email,password)
    return render_template("register.html")

@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        email_id=request.form['emailid']
        password=request.form['password']
        conn = sqlite3.connect('registrations.db')
        c = conn.cursor()
        def read_from_db(email):
            users=[]
            c.execute('SELECT * FROM Registered_Users WHERE EMAIL = ?',(email,))
            data = c.fetchall()
            for row in data:
                users.append(row)
            return users
        users_list=read_from_db(email_id)
        if users_list == []:
            return render_template("login.html",msg=str("User not found!"))
        else:
            if password == users_list[0][2]:
                return render_template("login.html",msg=str("Login Successful!"))
            else:
                return render_template("login.html",msg=str("Password Incorrect"))
        c.close()
        conn.close()
    return render_template("login.html",msg=str(""))
@app.route("/home")
def home():
    return render_template("page2.html")
@app.route("/taal")
def taal():
    return render_template("page3.html")
@app.route("/taal/teentaal")
def teentaal():
    return render_template("page4.html")
@app.route("/taal/ektaal")
def ektaal():
    return render_template("ektaal.html")
@app.route("/taal/jhaptaal")
def jhaptaal():
    return render_template("jhaptaal.html")
@app.route("/taal/keherwa")
def keherwa():
    return render_template("keherwa.html")
@app.route("/taal/dadra")
def dadra():
    return render_template("dadra.html")
@app.route("/taal/rupak")
def rupak():
    return render_template("rupak.html")
@app.route("/types")
def types():
    return render_template("types.html")
@app.route("/types/6beats")
def _6beats():
    return render_template("6beats.html")
@app.route("/types/8beats")
def _8beats():
    return render_template("8beats.html")
@app.route("/types/10beats")
def _10beats():
    return render_template("10beats.html")
@app.route("/types/12beats")
def _12beats():
    return render_template("12beats.html")
@app.route("/types/16beats")
def _16beats():
    return render_template("16beats.html")   
@app.route('/types/result',methods = ['POST', 'GET'])
def result():
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
       program_input="" 
       result = request.form
       print("Hello World")
       print(result)
       program_input+=taal_dict[result['beat1']]+" "
       program_input+=taal_dict[result['beat2']]+" "
       program_input+=taal_dict[result['beat3']]+" "
       program_input+=taal_dict[result['beat4']]+" "
       program_input+=taal_dict[result['beat5']]+" "
       program_input+=taal_dict[result['beat6']]+" "
       program_input+=taal_dict[result['beat7']]+" "
       program_input+=taal_dict[result['beat8']]+" "
       program_input+=taal_dict[result['beat9']]+" "
       program_input+=taal_dict[result['beat10']]+" "
       program_input+=taal_dict[result['beat11']]+" "
       program_input+=taal_dict[result['beat12']]+" "
       program_input+=taal_dict[result['beat13']]+" "
       program_input+=taal_dict[result['beat14']]+" "
       program_input+=taal_dict[result['beat15']]+" "
       program_input+=taal_dict[result['beat16']]
       print(program_input)
    return "Hello W"
@app.route("/laykari")
def laykari():
    return render_template("laykarigun.html")
@app.route("/laykari/dugun")
def dugun():
    return render_template("dugun.html")
@app.route("/laykari/tigun")
def tigun():
    return render_template("tigun.html")
@app.route("/laykari/chaugun")
def chaugun():
    return render_template("chaugun.html")

if __name__ == "__main__":
    app.run()