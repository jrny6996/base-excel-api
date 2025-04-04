from flask import Flask, request, jsonify, render_template, send_file
import json
from flask_cors import CORS
import sqlite3
from flask import g
import os
import random
import inflect
import markdown

app = Flask(__name__)
CORS(app)

DATABASE = './db/base_excel.db'

p = inflect.engine()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Enable dictionary-like access
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def make_messy(data):
    messy_data = {}
    for key, value in data.items():
        if random.random() < 0.2:  # 1 in 5 chance to modify
            if isinstance(value, int):
                # Convert number to words
                # messy_data[key] = p.number_to_words(value)  

                #temp ignore for pilot
                messy_data[key] = value
            elif isinstance(value, str):
                if random.choice([True, False]):
                    messy_data[key] = value + "/"  # Add trailing backslash
                else:
                    messy_data[key] = f'"{value}"'  # Wrap string in quotes
            else:
                messy_data[key] = value
        else:
            messy_data[key] = value  # Keep original value
    return messy_data

def purchase_by_mon(data):
    purchases_by_month = {}
    for purchase in data:
        if "purchase_date" in purchase:
            try:
                date_str = purchase["purchase_date"]
                year_month = date_str.split("-")[0] + "-" + date_str.split("-")[1]

                if year_month not in purchases_by_month:
                    purchases_by_month[year_month] = []
                purchases_by_month[year_month].append(purchase)
            except IndexError:
                print(f"Warning: Invalid date format in purchase: {purchase}") # Handle bad data.
            except AttributeError:
                print(f"Warning: purchase_date is not a string: {purchase}")
        else:
            print(f"Warning: purchase_date missing in purchase: {purchase}")

    return purchases_by_month

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/guides", methods=["GET"])
def guides():
    with open('guides.json') as f:
        guide_data = json.load(f)
    return render_template("guides.html", guides = guide_data)

# API routes
@app.route("/api/january", methods=["POST"])
def monthly_data():
    print(request.json)
    if request.json["key"] == "1234ajsdhfkja12838":
        purchase_data = query_db("SELECT * FROM Purchases WHERE strftime('%m', purchase_date) = '01';")
        employee_data = query_db("SELECT * FROM Employees;")
        customer_data = query_db("SELECT * FROM Customers;")
        
        purchases = [make_messy(dict(row)) for row in purchase_data]
        employees = [make_messy(dict(row)) for row in employee_data]
        customers = [make_messy(dict(row)) for row in customer_data]

        
        return jsonify({"purchases": purchases, "employees": employees, "customers": customers})
    else:
        return jsonify({"message": "Sorry, there was an error accessing your material"}), 403

@app.route("/api/2024", methods=["POST"])
def yearly_data():
    print(request.json)
    if request.json["key"] == "1234ajsdhfkja12838":
        purchase_data = query_db("SELECT * FROM Purchases;")
        employee_data = query_db("SELECT * FROM Employees;")
        customer_data = query_db("SELECT * FROM Customers;")
        
        purchases = [make_messy(dict(row)) for row in purchase_data]
        employees = [make_messy(dict(row)) for row in employee_data]
        customers = [make_messy(dict(row)) for row in customer_data]
        purchases = purchase_by_mon(purchases)

        
        return jsonify({"purchases": purchases, "employees": employees, "customers": customers})
    else:
        return jsonify({"message": "Sorry, there was an error accessing your material"}), 403


import markdown



@app.route("/guides/workshop-one") 
def guide_one():
    markdown_file_path = os.path.join(app.root_path, 'ws1.md') # Get the absolute path

    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code']) #Add extensions
        return render_template('workshop.html', content=html_content, video = "https://www.youtube.com/embed/YGKm_c3Yajk?si=EYL2KQBEXz47xh0R")
    except FileNotFoundError:
        return "Markdown file not found.", 404

@app.route("/guides/workshop-two") 
def guide_two():
    markdown_file_path = os.path.join(app.root_path, 'ws2.md') # Get the absolute path

    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code']) #Add extensions
        return render_template('workshop.html', content=html_content, additional_materials = "https://drive.google.com/drive/folders/174nR9kG8rFyEF-zsoapn75Pye9BzR12L?usp=sharing")
    except FileNotFoundError:
        return render_template('workshop.html', content="Guide not found 404")   
    

@app.route("/guides/workshop-three") 
def guide_three():
    markdown_file_path = os.path.join(app.root_path, 'ws3.md') # Get the absolute path

    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code']) #Add extensions
        return render_template('workshop.html', content=html_content)
    except FileNotFoundError:
        return render_template('workshop.html', content="Guide not found 404") 


@app.route('/download')
def download():
    path = './Week 2 Adv. Excel Data-20250312T215324Z-001.zip'
    return send_file(path, as_attachment=True)

@app.route("/submit-form", methods = ["GET","POST"])
def handle_form_submit():
    return "<h2 class = 'text-green-500 text-lg'>Success! We'll reach out to you with events</h2>"

if __name__ == "__main__":
    app.run(port=8080, debug=True)