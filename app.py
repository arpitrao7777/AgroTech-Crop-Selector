from flask import Flask, render_template, request
# Importing Flask and related functions:
# Flask - main framework to create the web app
# render_template - to render HTML templates
# request - to handle incoming data from forms

import pickle
# To load your saved machine learning model and scaler

import numpy as np
# For numerical operations, especially to create numpy arrays for prediction

import pandas as pd
import sklearn
# Imported but not directly used here; pandas and sklearn might be needed elsewhere

import os

# To interact with the operating system, here used to list static files


# Loading the saved trained model and StandardScaler object from disk
model = pickle.load(open('model.pkl', 'rb'))  # Load the trained ML model
sc = pickle.load(open('sc.pkl', 'rb'))  # Load the scaler used to standardize inputs

# Create a Flask web app instance
app = Flask(__name__)


# Define the home page route ("/") which accepts GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    # List all files inside the 'static' folder of the app root directory
    static_files = os.listdir(os.path.join(app.root_path, 'static'))

    # Render the "index.html" template and pass the list of static files to it
    return render_template("index.html", lookup_static_files=static_files)


# Define the '/predict' route which only accepts POST requests from the form submission
@app.route("/predict", methods=['POST'])
def predict():
    # Extract input values from the submitted form by their field names
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    # Again, get list of static files (for passing to the template)
    static_files = os.listdir(os.path.join(app.root_path, 'static'))

    # Input validation: check if inputs are within expected ranges
    if not (1 <= ph <= 14):
        # If pH is out of range, return to homepage with an error message
        return render_template("index.html", result="Error: pH must be between 1 and 14.",
                               lookup_static_files=static_files)
    if humidity > 100:
        # If humidity exceeds 100%, return error message
        return render_template("index.html", result="Error: Humidity cannot exceed 100%.",
                               lookup_static_files=static_files)
    if temp > 55:
        # If temperature exceeds 55°C, return error message
        return render_template("index.html", result="Error: Temperature cannot exceed 55°C.",
                               lookup_static_files=static_files)

    # Prepare the feature list in the order expected by your model
    feature_list = [N, P, K, temp, humidity, ph, rainfall]

    # Convert list into 2D numpy array (required input shape for scikit-learn models)
    single_pred = np.array(feature_list).reshape(1, -1)

    # Scale the input features using the previously loaded scaler (same scaling as training data)
    scaled_input = sc.transform(single_pred)

    # Use the trained model to predict the crop label for the given input
    prediction = model.predict(scaled_input)

    # Mapping numerical labels back to crop names for displaying results
    crop_dict = {
        1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
        8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
        14: "Pomegranate", 15: "Lentil", 16: "Black gram", 17: "Mung bean", 18: "Moth beans",
        19: "Pigeon peas", 20: "Kidney beans", 21: "Chickpea", 22: "Coffee"
    }

    # Check if predicted numeric label exists in dictionary
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]  # Get the crop name
        # Render the homepage with the predicted crop result and static files list
        return render_template("index.html", result=crop, lookup_static_files=static_files)
    else:
        # If prediction is unknown, return 'Unknown' result message
        return render_template("index.html", result="Unknown", lookup_static_files=static_files)


# Main function: Run the Flask app when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode to show errors and auto-reload
