# import pandas as pd
from flask import Flask, jsonify, request
from data_prep import *
import pickle

# connect to db


with open('models/rf_pipe.pkl','rb') as f:
    MODEL = pickle.loads(f)

# get data
DATA = pd.read_csv('Dataset/titanic.csv')

# app
app = Flask(__name__)

print(DATA.sample(1))
print(MODEL.predict(DATA.sample(1)))

# routes
@app.route('/', methods=['POST'])
def predict():

    print(DATA.sample(1))
    print(MODEL.predict(DATA.sample(1)))
    #data = clean_data(data)

    #data = data.head()

    #return jsonify(data)
    return jsonify(MODEL.predict())#jsonify(results='This will return prepared data. Soon. Hopefully.')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
