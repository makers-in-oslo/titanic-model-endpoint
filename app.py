import pandas as pd
from flask import Flask, jsonify, request
from data_prep import *

# connect to db

# get data
data = pd.read_csv('Dataset/titanic.csv')

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def data_prep():

    #data = clean_data(data)

    #data = data.head()

    #return jsonify(data)
    return jsonify(test_function())#jsonify(results='This will return prepared data. Soon. Hopefully.')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
