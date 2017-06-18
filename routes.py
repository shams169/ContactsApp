from app            import app
from flask          import render_template
from flask          import url_for
from flask          import request
from DataAccess     import dbConnect
import mysql.connector


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

        #INSERT into the database
        ins_into_users = """INSERT INTO USERS (FirstName, LastName, UserName, PassWord, Email) \
                            VALUES('%s', '%s', '%s', '%s', '%s') """ \
                            % ( fname, lname, uname, passwd, email)
        try:
            db = dbConnect()
            db.cursor.execute(ins_into_users)
            db.commit()
            db.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        return render_template("accountCreated.html")
