# import pandas as pd
from flask import Flask, jsonify, request
import pandas as pd
import pickle

with open('models/rf_pipe.pkl','rb') as f:
    MODEL = pickle.load(f)

# app
app = Flask(__name__)


# routes
@app.route("/", methods=["POST"])
def predict():
    try:
        json_row = request.get_json()
        print(f"payload: {json_row}")

        df_row = (
            pd.DataFrame(json_row, index=[0])
            .rename(columns=str.lower)
            .drop(columns=["name", "ticket", "cabin"])
            .set_index("passengerid")
        )

        prediction = MODEL.predict(df_row)[0]
        print(f"prediction for {df_row}: {prediction}")

        return str(prediction)
    except:
        raise WrongInput(
            "Payload should be json with all titanic headers except"
            " survived as keys")


class WrongInput(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(WrongInput)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
