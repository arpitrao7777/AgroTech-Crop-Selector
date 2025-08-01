# AgroTech-Crop-Selector
**🌱 AgroTech Crop Selector**
is a Flask-based web application that predicts the most suitable crop to cultivate based on key agricultural parameters like soil nutrients (N, P, K), temperature, humidity, pH, and rainfall. It utilizes a machine learning model trained on agricultural datasets to assist farmers and agriculturalists in making data-driven decisions.


**🚀 Features**
1. Predicts the best crop based on soil and climate conditions.

2. Uses a trained Machine Learning model with feature scaling for accurate results.

3. Displays relevant crop image dynamically based on prediction.

4. Clean, responsive UI with Bootstrap and animated transitions.

5. Input validation for realistic values (e.g., pH, temperature, humidity).


**🧠 Tech Stack**

**1. Backend:** Python, Flask

**2. Frontend:** HTML5, CSS3, Bootstrap 5

**3. Machine Learning:** scikit-learn, NumPy, pandas

**4. Model Files:**

     model.pkl: Trained ML classification model

     sc.pkl: StandardScaler object for feature normalization


**🖥️ How to Run the Project**

**1.Clone the repository**

    bash:- git clone https://github.com/arpitrao7777/AgroTech-Crop-Selector.git
           cd AgroTech-Crop-Selector

**2.Set up a virtual environment (recommended)**

    bash:- python -m venv venv
           source venv/bin/activate  # On Windows use: venv\Scripts\activate

**3.Install required packages**

    nginx:- pip install -r requirements.txt

If requirements.txt is not available, manually install:

    nginx:- pip install flask numpy pandas scikit-learn

**4.Run the app**

    nginx:- python app.py

**5.Access the application**

Open your browser and go to http://127.0.0.1:5000


**📊 Model Details**

**Type:** Classification model

**Algorithm:** (RandomForestClassifier)

**Input Features:**

1. Nitrogen (N)

2. Phosphorus (P)

3. Potassium (K)

4. Temperature (°C)

5. Humidity (%)

6. pH

7. Rainfall (mm)

The model predicts among 22 different crops including Rice, Banana, Cotton, Maize, Apple, and Coffee.


**✅ Input Validations**

**Validation pH:-**
Must be between 1 and 14

**Humidity:-**
Cannot exceed 100%

**Temperature:-**
Cannot exceed 55°C

**All others:-**
Must be positive numeric values
