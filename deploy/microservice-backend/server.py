import datetime
import json

import numpy as np
from flask import Flask, request
from flask_cors import CORS
from model_utils import CycleTransformer, load_model_pipeline

NUM_DAYS = 14
RANDOM_FOREST_MODEL_PATH = "../../models/random_forest_model.joblib"
LINEAR_REGRESSION_MODEL_PATH = "../../models/linear_regression_model.joblib"

app = Flask(__name__)
CORS(app)

forest_model = load_model_pipeline(RANDOM_FOREST_MODEL_PATH)
# regression_model = load_model_pipeline(LINEAR_REGRESSION_MODEL_PATH)


@app.route('/api/forest', methods=['POST'])
def predict_forest():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Crete 14 dates from date passed by user
    base = datetime.datetime(data['year'], data['month'], data['day'])
    date_list = [base + datetime.timedelta(days=x) for x in range(14)]
    date_list_prepared = np.array(
        [[date.day, date.month, date.year] for date in date_list])

    # Make prediction using model loaded from disk
    predictions = forest_model.predict(date_list_prepared)

    # Jsonify predictions
    js = {}
    for date, prediction in zip(date_list, predictions):
        js[date.strftime("%m/%d/%Y")] = prediction

    json_object = json.dumps(js, indent=4)
    # return json response
    return json_object


@app.route('/api/regression', methods=['POST'])
def predict_regression():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Crete 14 dates from date passed by user
    base = datetime.datetime(data['year'], data['month'], data['day'])
    date_list = [base + datetime.timedelta(days=x) for x in range(14)]
    date_list_prepared = np.array(
        [[date.day, date.month, date.year] for date in date_list])

    # Make prediction using model loaded from disk
    predictions = forest_model.predict(date_list_prepared)

    # Jsonify predictions
    js = {}
    for date, prediction in zip(date_list, predictions):
        js[date.strftime("%m/%d/%Y")] = prediction

    json_object = json.dumps(js, indent=4)
    # return json response
    return json_object


if __name__ == '__main__':
    # Load the model
    app.run(port=8020, debug=True)
