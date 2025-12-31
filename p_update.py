#!C:/python3/python
print("Content-type: text/html")
print()
import cgi

form=cgi.FieldStorage()

order_id=form.getvalue("order_id")
customer_name=form.getvalue("customer_name")
flavours=form.getvalue("flavours")
sizes=form.getvalue("sizes")
toppings=form.getvalue("toppings")
icing=form.getvalue("icing")
themes=form.getvalue("themes")
fileitem=form.getvalue("filename")

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='sweetcratecake_db')
cursor=conn.cursor()
cursor.execute("""SELECT filename FROM sweetcratecake_tbl WHERE id = %s""", (order_id,))
row = cursor.fetchone()

existing_filename = row[0]

if themes != "Custom":
    filename = "No Customisation"
else:
    if fileitem:
        filename = fileitem
    elif not fileitem and existing_filename != "No Customisation":
        filename = existing_filename
    else:
        filename = "No Customisation"
    
cursor.execute('UPDATE sweetcratecake_tbl SET customer_name=%s,flavours=%s,sizes=%s,toppings=%s,icing=%s,themes=%s,filename=%s WHERE id=%s',
    (customer_name, flavours, sizes, toppings, icing, themes, filename, order_id))
conn.commit()

PRICE = {
    "Chocolate": 5,
    "Vanilla": 1,
    "Strawberry": 10,
    "Big": 300,
    "Medium": 160,
    "Small": 80,
    "Sprinkle": 3,
    "Chocolate Topping": 5,
    "Fruity": 15,
    "Vanilla Cream": 1,
    "Buttercream": 1,
    "Berry Cream": 10,
    "Wedding": 100,
    "Birthday": 100,
    "Custom": 100
}

def get_price(value):
    return PRICE.get(value, 0)

total = (
    get_price(flavours) +
    get_price(sizes) +
    get_price(toppings) +
    get_price(icing) +
    get_price(themes)
)

if filename != "No Customisation":
    picture = f'''<img class="record-image" src="images/{filename}">'''
else:
    picture = "No Customisation"

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
        <div class="header">
            <div class="header-logo">
                <a href="index.html">Sweetcrate</a> 
            </div>
            <div class="header-login">
                <a href="index.html">End Section?</a>
            </div>
        </div>
        <div class="tool-section">
            <h1>Record Updated</h1>
            <div class="record-table-grid">
                <div class="record-table-title">
                    No.
                </div>
                <div class="record-table-title">
                    New Order ID
                </div>
                <div class="record-table-title">
                    Customer Name
                </div>
                <div class="record-table-title">
                    Flavours
                </div>
                <div class="record-table-title">
                    Sizes
                </div>
                <div class="record-table-title">
                    Toppings
                </div>
                <div class="record-table-title">
                    Icing
                </div>
                <div class="record-table-title">
                    Themes
                </div>
                <div class="record-table-title">
                    Customisation
                </div>
                <div class="record-table-title">
                    Total Price
                </div>
                <div class="record-table-content">
                    1
                </div>
                <div class="record-table-content">
                    {order_id}
                </div>
                <div class="record-table-content">
                    {customer_name}
                </div>
                <div class="record-table-content">
                    {flavours}
                </div>
                <div class="record-table-content">
                    {sizes}
                </div>
                <div class="record-table-content">
                    {toppings}
                </div>
                <div class="record-table-content">
                    {icing}
                </div>
                <div class="record-table-content">
                    {themes}
                </div>
                <div class="record-table-content">
                    {picture}
                </div>
                <div class="record-table-content">
                    RM{total}
                </div>
            </div>
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