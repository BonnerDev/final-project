from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import pandas as pd
import json
from config import username
from config import password
from config import database

app = Flask(__name__)

#create connection to databse
engine = create_engine(f"postgresql://{username}:{password}@localhost:5432/{database}")
conn=engine.connect()

@app.route("/data")
def datatest():
    data = pd.read_sql("select * from placement_type", conn)
    #print(data)
    datatojson = data.to_json(orient = "index")
    parsed = json.loads(datatojson)
    return parsed

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/buttons")
def buttons():
    return render_template('buttons.html')

@app.route("/charts")
def charts():
    return render_template('charts.html')

@app.route("/tables")
def tables():
    return render_template('tables.html')

if __name__ == "__main__":
    app.run(debug=True)