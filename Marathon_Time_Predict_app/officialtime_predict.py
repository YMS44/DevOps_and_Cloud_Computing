from flask import Flask, request ,jsonify
import joblib
import pandas as pd
import pickle

app = Flask(__name__)

model = joblib.load('final_official_time_model.pkl')
col_names = joblib.load('official_time_column_names.pkl')

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/predict',methods = ['POST'])
def predict():
    #Get JSON request
    user_data = request.json
    # Convert JSON request to pandas DataFrame
    df = pd.DataFrame(user_data)
    # Match Column Names
    df = df.reindex(columns=col_names)
    # Get Predictions
    prediction = list(model.predict(df))
    # return JSON version of prediction
    return jsonify({'prediction': str(prediction)})

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')