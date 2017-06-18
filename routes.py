from app import app
from flask import render_template
from flask import url_for
from flask import request

from DataAccess import dbConnect

#from tkinter import messagebox


@app.route('/')
def welcome():
    #url = "<a href='"+url_for('create')+"'> Create a Link</a>"
    url = url_for('create')
    #messagebox.showinfo('url')
    print(url)
    return render_template('welcome.html', create=url)
    # return """
    # <html><body>
    #  """ +url+"""
    #  </body></html>
    # """


@app.route('/home')
def home():
    return "Home"

@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'GET':
        return render_template('createAccount.html')
    if request.method == 'POST':
        print('Reached POST method ')
        fname    = request.form['firstname']
        lname    = request.form['lastname']
        uname   = request.form['userid']
        passwd   = request.form['password']
        email    = request.form['email']
        userid   = 1

        cnx    = dbConnect()

        ins_into_users =   "INSERT INTO USERS VALUES("+3+","+fname+","+lname+","+uname+","+passwd+","+email+")"

        cnx.cursor.execute('SELECT * FROM USERS')
        print(cnx.cursor.fetchall())

        return render_template("accountCreated.html")
