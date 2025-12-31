#!C:/python3/python
print("Content-type: text/html")
print()

import mysql.connector

conn=mysql.connector.connect(user='root', password='', host='localhost', database='sweetcratecake_db')
cursor=conn.cursor()
 
conn.commit()

cursor.execute('SELECT * FROM sweetcratecake_tbl')

data = cursor.fetchall()

def generateWebsite(value, value2):
    print(f'''
        <html>
            <head>
                <title>
                    Sweetcrate - Admin
                </title>
                <link rel="stylesheet" href="css/body.css">
                <link rel="stylesheet" href="css/header.css">
                <link rel="stylesheet" href="css/tool.css">
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
                    <h1>View Record</h1>
                    <div class="record-table-grid">
                        <div class="record-table-title">
                            No.
                        </div>
                        <div class="record-table-title">
                            Order ID
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
                        {value}
                    </div>
                    {value2}
                </div>
            </body>
        </html>
    ''')

generateHTML = ''

a=1
for row in data:
    flavour = row[2]
    size = row[3]
    topping = row[4]
    icing = row[5]
    theme = row[6]
    filename = row[7]

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
    
    if row[7] != "No Customisation":
        filename = f'''<img class="record-image" src="images/{row[7]}">'''

    generateHTML += f'''
            <div class="record-table-content">
                {a}
            </div>
            <div class="record-table-content">
                {row[0]}
            </div>
            <div class="record-table-content">
                {row[1]}
            </div>
            <div class="record-table-content">
                {row[2]}
            </div>
            <div class="record-table-content">
                {row[3]}
            </div>
            <div class="record-table-content">
                {row[4]}
            </div>
            <div class="record-table-content">
                {row[5]}
            </div>
            <div class="record-table-content">
                {row[6]}
            </div>
            <div class="record-table-content">
                {filename}
            </div>
            <div class="record-table-content">
                RM{total}
            </div>
          '''
    a += 1

generateReport = f'''
            <h2>Number of Records: {a-1}</h2>
                <a href="admin_index.html">
                    <button class="btn-return">
                        Return
                    </button>
                </a>
    '''
    
generateWebsite(generateHTML, generateReport)
    
cursor.close()
conn.close()