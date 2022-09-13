import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    features = [np.array(features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text="This model predicts the flower species is {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
