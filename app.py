import numpy as np
#import pyttsx3
import sqlite3
import MySQLdb
import os
#from playsound import playsound
from flask import Flask,render_template,request,redirect,url_for,session
import pestdetector as pestde
import exceltest as detailsfrom
app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'secret!'
mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='pestdetection')
UPLOAD_FOLDER = 'static/uploads/'


@app.route("/")
def home():
    return render_template("index.html")
@app.route('/logon')
def logon():
        return render_template('signup.html')
@app.route('/login')
def login():
	session.clear()
	return render_template('signin.html')

@app.route('/uhome')
def uhome():
    return render_template('home.html')
@app.route('/upload',methods=['GET', 'POST'])
def upload():
    file = request.files['file'] # fet input
    filename = file.filename        
    print("@@ Input posted = ", filename)
        
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    pred_class=pestde.process(file_path)
    final_res=list(pred_class)[0]
    c,a,p=detailsfrom.process(final_res)
    return render_template('result.html',final_res=final_res ,c=c,a=a,p=p,img_src=UPLOAD_FOLDER+file.filename)

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    #con = sqlite3.connect('signup.db')
    cur = mydb.cursor()
    cur.execute("insert into reg (user,email,password,mobile,name) VALUES (%s, %s, %s, %s, %s)",(username,email,password,number,name))
    mydb.commit()
    mydb.close()
    return render_template("signin.html")


@app.route("/signin",methods=['POST','GET'])
def signin():

    mail1 = request.args.get('user','')
    print("user name==",mail1)
    password1 = request.args.get('password','')
    print("password==",password1)
    #mydb = sqlite3.mydbnect('signup.db')
    cur = mydb.cursor()
    cur.execute("select user, password from reg where user =%s  AND password = %s",(mail1,password1,))
    data = cur.fetchone()
    print("Data==",data)

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("home.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
            session['cid'] = mail1
            return render_template("home.html")
    else:
        return render_template("signin.html")

@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/logout")
def logout():
    session.clear()
    return render_template('signin.html')




  
if __name__ == "__main__":
    app.run(debug=True)
    