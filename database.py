import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor to execute SQL commands
# Think of a cursor like a little robot inside the database.
# Without the cursor, Python scripts can’t talk to the database.
cursor = conn.cursor()

# Create a table called "users" if there's none
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
# "CREATE TABLE IF NOT EXISTS users": creates a table called "users" if there's none with that name

# "id INTEGER PRIMARY KEY AUTOINCREMENT":
# "id" -> column name
# "INTEGER" -> data type
# "PRIMARY KEY" -> main identifier of each user
# "AUTOINCREMENT" -> starts at 1 and adds up from there (1, 2, 3, 4...).
#                    Can only be used if it has "PRIMARY KEY" identifier.

# "username TEXT NOT NULL UNIQUE":
# "username" -> column name
# "TEXT" -> data type
# "NOT NULL" -> This field MUST be filled
# "UNIQUE" -> no two users can have the same username

# "password TEXT NOT NULL"
# "password" -> column name
# "TEXT" -> data type
# "NOT NULL" -> field MUST be filled


# Save and close connection
conn.commit() # saves the database like you save a 'Word Document'
conn.close() # IMPORTANT: database MUST close at the end to prevent errors and DATA-LOSS

print("Database created and 'users' table is ready!")
