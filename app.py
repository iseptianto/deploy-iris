from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Periksa apakah file model tersedia sebelum memuat
model_path = "eden.pkl"

if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))
else:
    print("ERROR: File model tidak ditemukan!")
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template("index.html", prediction_text="Model tidak ditemukan!")

    try:
        float_features = [float(x) for x in request.form.values()]
        feature_array = np.array(float_features).reshape(1, -1)  # Pastikan bentuk input sesuai model
        prediction = model.predict(feature_array)

        return render_template("index.html", prediction_text=f"Hasil prediksi: {prediction[0]}")
    
    except Exception as e:
         return render_template("index.html", prediction_text=f"Terjadi kesalahan: {str(e)}")
if __name__ == "__main__":
    app.run(debug=True)