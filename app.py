import joblib
from flask import Flask, render_template, request, redirect, url_for

model = joblib.load('rfr_model.sav')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        num_preg = int(request.form['preg'])
        glucose_conc = float(request.form['gluc'])
        insulin = float(request.form['ins'])
        bmi = float(request.form['bmi'])
        diab_pred = float(request.form['dpf'])
        age = int(request.form['age'])

        prediction = model.predict([[num_preg, glucose_conc, insulin, bmi, diab_pred, age]])
        output = prediction[0]

        if output==0:
            return render_template('index.html', prediction_text="You have low chances of having diabetes...")
        else:
            return render_template('index.html', prediction_text="You have high chances of having diabetes...")
        

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)