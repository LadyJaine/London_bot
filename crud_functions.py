import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()


def get_all_product():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    cur_f = cursor.fetchall()
    cursor.close()
    connection.close()
    return cur_f


def add_user(username, email, age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        cursor.execute(f'''
        INSERT INTO Users (username,email,age,balance) VALUES ('{username}','{email}','{age}', 1000)
        ''')
        connection.commit()
        cursor.close()
        connection.close()


def is_included(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    check_user = cursor.fetchone()
    # print(check_user)
    if check_user:
        connection.close()
        return True
    else:
        connection.close()
        return False


if __name__ == '__main__':
    print(get_all_product())
    print(is_included('Urban'))
    # add_user('Urban','fdr@mail.ru',20)
