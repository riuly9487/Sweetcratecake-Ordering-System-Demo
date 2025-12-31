#!C:/python3/python
print("Content-type: text/html")
print()

import cgi
form=cgi.FieldStorage()

customer_name=form.getvalue("customer_name")
flavours=form.getvalue("flavours")
sizes=form.getvalue("sizes")
toppings=form.getvalue("toppings")
icing = form.getvalue("icing")
themes = form.getvalue("themes")
fileitem=form["filename"]
if fileitem.filename and themes == "Custom":
    filename = fileitem.filename

else:
    filename = "No Customisation"

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='sweetcratecake_db')
cursor=conn.cursor()
cursor.execute('INSERT INTO sweetcratecake_tbl (customer_name,flavours,sizes,toppings,icing,themes,filename) values(%s,%s,%s,%s,%s,%s,%s)',
    (customer_name, flavours, sizes, toppings, icing, themes, filename))
conn.commit()

order_id = cursor.lastrowid

cursor.execute("""
    SELECT id, customer_name, flavours, sizes, toppings, icing, themes
    FROM sweetcratecake_tbl
    WHERE id = %s
    """,
    (order_id,)
)

row = cursor.fetchone()

if not row:
    print("<h2>No order found</h2>")
    exit()

order_id = row[0]
customer_name = row[1]
flavour = row[2]
size = row[3]
topping = row[4]
icing = row[5]
theme = row[6]

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
    get_price(flavour) +
    get_price(size) +
    get_price(topping) +
    get_price(icing) +
    get_price(theme)
)

from datetime import datetime

order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.close()
conn.close()

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sweetcrate Receipt</title>
    <style>
        body {{
            background: #fde9ef;
            font-family: Arial;
            text-align: center;
        }}
        
    </style>
    <link rel="stylesheet" href="css/body.css">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/receipt.css">
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
        <a href="login.html">Admin Login?</a>
    </div>
</div>

<h2>Thank You For Placing Your Order</h2>
<p>Please keep this receipt for future reference.</p>

<div class="receipt-section">
    <h1>Sweetcrate</h1>
    <p>Custom Cake Ordering System</p>
    <hr>

    <table class="receipt-table">
        <tr><td><b>Order ID</b></td><td>{order_id}</td></tr>
        <tr><td><b>Order Time</b></td><td>{order_time}</td></tr>
        <tr><td><b>Customer Name</b></td><td>{customer_name}</td></tr>
    </table>

    <hr>

    <table class="receipt-table">
        <tr><td class="receipt-data">Flavour</td><td>{flavour}</td><td>RM{get_price(flavour)}</td></tr>
        <tr><td>Size</td><td>{size}</td><td>RM{get_price(size)}</td></tr>
        <tr><td>Topping</td><td>{topping}</td><td>RM{get_price(topping)}</td></tr>
        <tr><td>Icing</td><td>{icing}</td><td>RM{get_price(icing)}</td></tr>
        <tr><td>Theme</td><td>{theme}</td><td>RM{get_price(theme)}</td></tr>
    </table>

    <hr>

    <div>Total Price: RM {total}</div>

    <p><b>Thank you for choosing Sweetcrate</b></p>
</div>

<br>
<a href="order.html">
    <button class="btn-return">
        Place New Order
    </button>
</a>

</body>
</html>
""")
