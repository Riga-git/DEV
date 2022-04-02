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

@app.get("/api/persons")
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

@app.post("/api/person")
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