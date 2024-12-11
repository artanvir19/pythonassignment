from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the trained model and scaler
with open('rf_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Route to the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data from the user
    open_price = float(request.form['Open'])
    high_price = float(request.form['High'])
    low_price = float(request.form['Low'])
    close_price = float(request.form['Close'])
    volume = float(request.form['Volume'])
    day = int(request.form['Day'])
    month = int(request.form['Month'])
    year = int(request.form['Year'])

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Close': [close_price],
        'Volume': [volume],
        'Day': [day],
        'Month': [month],
        'Year': [year]
    })

    # Scale the input data using the pre-trained scaler
    scaled_input = scaler.transform(input_data)

    # Predict using the pre-trained Random Forest model
    prediction = rf_model.predict(scaled_input)

    # Convert the prediction (0 or 1) to a readable result
    if prediction[0] == 1:
        prediction_result = "Buy"
    else:
        prediction_result = "Sell"

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
