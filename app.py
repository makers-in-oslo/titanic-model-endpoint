# import pandas as pd
from flask import Flask, jsonify, request
from data_prep import *
import pickle

# connect to db


with open('models/rf_pipe.pkl','rb') as f:
    MODEL = pickle.load(f)

# get data
DATA = (pd.read_csv('Dataset/titanic.csv')
          .rename(columns=str.lower)
          .drop(columns=['survived','name','ticket','cabin'])
          .set_index('passengerid'))

# app
app = Flask(__name__)

print(DATA.sample(1))
print(MODEL.predict(DATA.sample(1)))

# routes
@app.route('/', methods=['POST'])
def predict():

    print(DATA.sample(1))
    prediction = MODEL.predict(DATA.sample(1))
    #data = clean_data(data)

    #data = data.head()

    #return jsonify(data)
    return str(prediction[0]) #jsonify(results='This will return prepared data. Soon. Hopefully.')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
