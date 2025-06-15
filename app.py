from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

#Load the trained machine learning model
model = joblib.load('house_price_model.pkl')

@app.route('/', method=['GET','POST'])

def predict():
    prediction = None
    if request.method == 'POST':
        try:
            #Get input values from the form
            feature1 = float(request.form['feature1']) #OverallQual
            feature2 = float(request.form['feature2']) #OverallQual
            feature3 = float(request.form['feature3']) #OverallQual
            feature4 = float(request.form['feature4']) #OverallQual
            
            input_data = np.array([[feature1, feature2, feature3, feature4]])
            
            #Predict
            result = model.predict(input_data)[0]
            prediction = round(result, 2)
        
        except Exception as e:
            prediction = f'Error: {e}'
        
    return render_template("index.html", prediction = prediction)
        
    
if __name__ == '__main__':
    app.run(debug=True)    