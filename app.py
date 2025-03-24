from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3
# 'render_template()' loads and displays an HTML file from the 'templates' folder
# 'request' is used to access data sent by the client (like form inputs)

app = Flask(__name__)  # __name__ tells Flask this file is the main entry point of the app


@app.route('/')  # When the user accesses "http://127.0.0.1:5000/", this function will run
def home():
    return ("Welcome to my Database Webserver! Hope you enjoy this little project!\n    "
            "Hint: /register")


@app.route('/register', methods=['GET', 'POST'])
# This route responds to both GET (show the form) and POST (process submitted data)
def register():
    if request.method == 'POST':
        # If the form was submitted (POST), we get the data
        username = request.form['username']  # Grabs the username from the form (HTML: name="username")
        raw_password = request.form['password']  # Grabs the password from the form (HTML: name="password")
        password = generate_password_hash(raw_password)
        # Hashes the password using a secure algorithm before saving it to the database


        # Connect to the database
        conn = sqlite3.connect('users.db') # Connects to the database, which in this case is called 'users.db'
        cursor = conn.cursor() # Think of a cursor like a little robot inside the database.

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            # "INSERT INTO users (username, password) VALUES (?, ?)"
            # "INSERT INTO users" -> Adds a new row into the users table
            # "(username, password)" -> The columns we are going to fill
            # VALUES (?, ?)" → placeholders for the actual values we're passing in (username, password)

            conn.commit()
            # Saved the database like just like you do with a 'Word Document'

            message = f"User '{username}' registered successfully!"
            # Changes the 'message' variable that will show a message in the webpage in the end of this function
            # Which in this case, will show after the new user gets successfully added

        except sqlite3.IntegrityError:
            # If we find another user with the same name as what was given to us, then this code will run:
            message = f"Username '{username}' is already taken."
            # Changes the 'message' variable that will show a message in the webpage in the end of this function

        finally:
            # After we end one of the blocks above, code below will run
            conn.close()
            # ATTENTION: "conn.close()" is SUPER important! This will close the database, and we helps prevent data loss
            # We should always end our code by closing the database.

        return message
        # Returns the message so it appears in the browser as a plain text response.

    return render_template('register.html')
    # Loads and returns the 'register.html' template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        raw_password = request.form['password']

        # Connect to DB and check credentials
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        # "SELECT * FROM users WHERE username = ? AND password = ?"
        # "SELECT" -> GET data
        # "*" -> means "select all columns" (in our case: id, username, password)
        # "FROM users" -> will look inside 'users' table
        # "WHERE username = ? AND password = ?" -> but will only get a row where the submitted username and password match BOTH in the database

        user = cursor.fetchone()
        # if a user is found this will get the row as a tuple
        conn.close()

        if user:
            stored_hash = user[2]
            # Gets the passwords row
            # 0 -> id
            # 1 -> usernames
            # 2 -> passwords
            if check_password_hash(stored_hash, raw_password):
                # encrypts the "raw_password" attempt and checks if there's any match in the passwords row
                return f"Welcome back, {username}!"
            else:
                return f"Wrong password for {username}!"
        else:
            return "Invalid username or password."

    return render_template('login.html')

if __name__ == '__main__':  # Only run this if the file is executed directly
    app.run(debug=True)  # Start the Flask server with debug mode (auto-reload + error messages)

