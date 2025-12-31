#!C:/python3/python
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()

name=form.getvalue("name")
pswd=form.getvalue("pswd")

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='sweetcratecake_db')
cursor=conn.cursor()

cursor.execute("SELECT * FROM admin_tbl WHERE name= %s",(pswd,)) 
 
data = cursor.fetchall()

a=1

for row in data:
    a += 1
    
b=a-1

login_success = f'''
        <div class="admin-section">

            <h1>Welcome to Our System!</h1>

            <a href="admin_index.html">
                <button class="btn-return">
                    Enter Admin Control
                </button>
            </a>
        </div>
    '''

login_failed = '''
        <div class="admin-section">

            <h1>Oops! Something when wrong, please try again!</h1>

            <a href="login.html">
                <button class="btn-return">
                    Try Again!
                </button>
            </a>
        </div>
'''

def generateWebsite(value):
    print(f'''
        <html>
            <head>
                <title>
                    Sweetcrate - Admin
                </title>
                <link rel="stylesheet" href="css/body.css">
                <link rel="stylesheet" href="css/header.css">
                <link rel="stylesheet" href="css/admin.css">
                <link rel="stylesheet" href="css/button.css">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
            </head>
            <body>
                <div class="header">
                    <div class="header-logo">
                        <a href="index.html">Sweetcrate</a> 
                    </div>
                    <div class="header-login">
                        <a href="index.html">End Section?</a>
                    </div>
                </div>
                {value}
            </body>
        </html>
    ''')


if b:
    generateWebsite(login_success)
else:
    generateWebsite(login_failed)
    

conn.commit()        
cursor.close()
conn.close()