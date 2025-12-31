#!C:/python3/python
print("Content-type: text/html")
print()
import cgi

form=cgi.FieldStorage()

order_id=form.getvalue("order_id")

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='sweetcratecake_db')
cursor=conn.cursor()

cursor.execute('DELETE FROM sweetcratecake_tbl WHERE id= '+order_id)
conn.commit()

website = f'''<html>
    <head>
        <title>
            Sweetcrate - Admin
        </title>
        <link rel="stylesheet" href="css/body.css">
        <link rel="stylesheet" href="css/header.css">
        <link rel="stylesheet" href="css/tool.css">
        <link rel="stylesheet" href="css/button.css">
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
        <div class="tool-section">
            <h1>Order Deleted Successfully</h1>
            <a href="admin_index.html">
                <button class="btn-return">
                    Return
                </button>
            </a>
        </div>
    </body>
</html>'''

print(website)

cursor.close()
conn.close()