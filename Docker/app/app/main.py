from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import mysql.connector


mydb = mysql.connector.connect(
  host="mariadb",
  port=3306,
  user="root",
  password="root-pwd",
  database="personstore"
)

mycursor = mydb.cursor()

app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>Cours DEV Docker</title>
        </head>
        <body>
            <h1>Hey! Do you want to safe some person into the DB ?</h1>
            <form action="/person" method="POST">
            <label for="fname">First name:</label><br>
            <input type="text" id="fname" name="fname"><br>

            <label for="lname">Last name:</label><br>
            <input type="text" id="lname" name="lname"><br>

            <label for="street">Street:</label><br>
            <input type="text" id="street" name="street"><br>

            <label for="snumber">Street NB:</label><br>
            <input type="text" id="cap" name="snumber"><br>

            <label for="cap">CAP:</label><br>
            <input type="text" id="cap" name="cap"><br>

            <label for="city">City:</label><br>
            <input type="text" id="city" name="city"><br>

            <label for="city">Phone:</label><br>
            <input type="text" id="phone" name="phone"><br>

            <input style="margin-top:20px; width:200px" type="submit" value="Submit">
            </form>
            <form method="get" action="/persons">
                <button type="submit" style="margin-top:20px; width:200px">To the persons list</button>
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/persons")
def read_item():
    mycursor.execute("SELECT * FROM persons")
    items = mycursor.fetchall()
    html_content = """
    <head>
    <style>
        table, th, td {
            border: 1px solid black;
        }
    </style>
    </head>
    <body>
        <table>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Street</th>
                <th>Street Nbr</th>
                <th>CAP</th>
                <th>City</th>
                <th>Phone</th>
            </tr>
    """
    for item in items : 
        html_content += "<tr>"
        for field in item :
            html_content += f"<td>{field}</td>"
        html_content += "</tr>" 
    html_content += "</table><a href=/> Back to form</a></body></html>"        
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/person")
async def save(fname: str = Form(...), \
               lname: str = Form(...), \
               street: str = Form(...), \
               snumber: str = Form(...), \
               cap: str = Form(...), \
               city: str = Form(...), \
               phone: str = Form(...)):
    sql = "INSERT INTO persons (name, firstname, street, streetNbr, CAP, city, phone) \
           VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (fname, lname, street, snumber, cap, city, phone)
    mycursor.execute(sql, val)
    mydb.commit()
    return RedirectResponse(url="/", status_code=303)