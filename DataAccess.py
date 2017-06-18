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


    def commit(self):
        self.connection.commit()

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
    userid   = 4



    ins_query = """INSERT INTO USERS (FirstName, LastName, UserName, PassWord,Email)VALUES('%s', '%s', '%s', '%s', '%s') """ %(fname, lname, uname, passwd, email)

    db.cursor.execute(ins_query)
    db.connection.commit()



if __name__ == '__main__':
    main()
