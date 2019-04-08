"""
Author: Krista Kinnard

Contents:
	This is a very basic flask application that demonstrates the basic capability of 
    connection to a firebase MongoDB. We will grow this application to serve as the 
    serverside code for our street sweeper application. As we grow the application, we
    should also grow the documenation here.

Usage:
	run `python app.py`

	Open your browser. Go to http://127.0.0.1:5000/

    Add your name as a user. Currently, any string will be accepted. If you are in the firebase UI, you will
    see your name added to the DB.

"""

# import necessary packages
from flask import *
from config import firebase_config 

# instantiate firebase
db = firebase_config.firebase_connection()


# code if the server can't find something
HTTP_NOT_FOUND = 404

# Tell python we are using Flask to create a web application
app = Flask(__name__)

# decorate this function so that flask knows that calls to <base_url>/ will come here
@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Return a basic message from the base url
    """
    if request.method == 'POST':
        name = request.form['name']
        db.child("users").push(name)
        user = db.child("users").get()
        print(user)
        user_name = user.val()
        return render_template('index.html', user_name=user_name.values())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)