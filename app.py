from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app

#import routes file
#from ContactsDir.routes import *;
from routes import *

if __name__ == '__main__':
    app.run()
