# AgroTech-Crop-Selector
**🌱 AgroTech Crop Selector**

AgroTech Crop Selector is a Flask-based web application that predicts the most suitable crop to cultivate based on key agricultural parameters like soil nutrients (N, P, K), temperature, humidity, pH, and rainfall. It utilizes a machine learning model trained on agricultural datasets to assist farmers and agriculturalists in making data-driven decisions.

**🚀 Features**
Predicts the best crop based on soil and climate conditions.
Uses a trained Machine Learning model with feature scaling for accurate results.
Displays relevant crop image dynamically based on prediction.
Clean, responsive UI with Bootstrap and animated transitions.
Input validation for realistic values (e.g., pH, temperature, humidity).

**🧠 Tech Stack**
Backend: Python, Flask
Frontend: HTML5, CSS3, Bootstrap 5
Machine Learning: scikit-learn, NumPy, pandas
Model Files:
model.pkl: Trained ML classification model
sc.pkl: StandardScaler object for feature normalization

**📂 Project Structure**

AgroTech-Crop-Selector/
│
├── static/
│   ├── background.jpg
│   ├── default.jpg
│   ├── placeholder.jpg
│   ├── rice.jpg
│   ├── banana.jpg
│   └── ... (images for each crop)
│
├── templates/
│   └── index.html
│
├── model.pkl               # Trained ML model
├── sc.pkl                  # StandardScaler used in training
├── app.py                  # Flask application code
└── README.md               # Project documentation

**🖥️ How to Run the Project**

1. Clone the repository

bash :-
git clone https://github.com/arpitrao7777/AgroTech-Crop-Selector.git

2. Set up a virtual environment (recommended)

bash :-
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3.Install required packages

nginx :-
pip install -r requirements.txt

If requirements.txt is not available, manually install:
nginx :-
pip install flask numpy pandas scikit-learn

4. Run the app

nginx :-
python app.py

5. Access the application

a). Run the main.py file
b). Open your browser and go to http://127.0.0.1:5000

**📊 Model Details**

Type: Classification model
Algorithm: (RandomForestClassifier)
Input Features:
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature (°C)
Humidity (%)
pH
Rainfall (mm)

The model predicts among 22 different crops including Rice, Banana, Cotton, Maize, Apple, and Coffee.

**🧪 Sample Inputs**

Nitrogen	Phosphorus	Potassium	Temp (°C)	Humidity (%)	pH	  Rainfall (mm)
90      	42        	43	      22.5	    80	          6.5	  120

**✅ Input Validations**

Parameter	Validation
pH	Must be between 1 and 14
Humidity	Cannot exceed 100%
Temperature	Cannot exceed 55°C
All others	Must be positive numeric values
