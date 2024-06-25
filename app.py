# app.py
from flask import Flask, jsonify,render_template
from database import get_data_from_database
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    # You can pass any data you want to the template here
    # For example, fetching data from the database
    data = get_data_from_database()
    
    return render_template('index.html', data=data)


@app.route('/api/data')
def get_data():
    data = get_data_from_database()  # Function to retrieve data from database
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
