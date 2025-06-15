from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # get features from form
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        feature4 = float(request.form['feature4'])

        # run model prediction (replace with your model)
        prediction = feature1 + feature2 + feature3 + feature4  # Dummy prediction

    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
