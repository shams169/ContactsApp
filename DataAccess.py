import mysql.connector

class dbConnect:

    def __init__(self):
        self.connection = mysql.connector.connect( user='root'     , password='shams',
                                                   host='localhost', database='ContactStore'
                                                  )
        self.cursor = self.connection.cursor()
        #print("cursor initalized")

    def query(self, query):
        #print('Query Method')
        self.cursor.execute(query)
        return self.cursor.fetchall()



    def close(self):
        self.cursor.close()
        self.connection.close()

def main():
    db = dbConnect()
    fname    = "John"
    lname    = "Wick"
    uname   = "jwick"
    passwd   = "1234"
    email    = "j@yahoo.com"
    userid   = 1

    ins_into_users =   "INSERT INTO USERS VALUES("+3+","+fname+","+lname+","+uname+","+passwd+","+email+")"
    db.cursor.execute(ins_into_users)



if __name__ == '__main__':
    main()
