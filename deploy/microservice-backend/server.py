import datetime
import json

import numpy as np
from flask import Flask, request
from flask_cors import CORS
from model_utils import CycleTransformer, load_model_pipeline

MODEL_PATH = "../../models/random_forest_model.joblib"

app = Flask(__name__)
CORS(app)

model = load_model_pipeline(MODEL_PATH)


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Crete 14 dates from date passed by user
    base = datetime.datetime(data['year'], data['month'], data['day'])
    date_list = [base - datetime.timedelta(days=x) for x in range(14)]
    date_list_prepared = np.array(
        [[date.day, date.month, date.year] for date in date_list])

    # Make prediction using model loaded from disk as per the data.
    predictions = model.predict(date_list_prepared)

    # Jsonify predictions
    js = {"predictions": list(predictions)}
    json_object = json.dumps(js, indent=4)
    # return json response
    return json_object


if __name__ == '__main__':
    # Load the model
    app.run(port=8020, debug=True)
