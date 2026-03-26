from flask import Flask, render_template, request

# CREATE APP
app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# PREDICTION
@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    condition = request.form['condition']

    # BMI calculation
    bmi = weight / ((height / 100) ** 2)

    if condition == "diabetes":
        exercise = "Brisk Walking + Yoga"
        time = "30–40 minutes"

    elif condition == "bp":
        exercise = "Yoga + Meditation"
        time = "20–30 minutes"

    else:
        if bmi > 25:
            exercise = "Running + Cycling"
            time = "40–50 minutes"
        elif bmi < 18:
            exercise = "Strength Training + Pushups"
            time = "30 minutes"
        else:
            exercise = "Jogging + Plank"
            time = "30–40 minutes"

    # ✅ IMPORTANT CHANGE HERE
    return render_template(
        'result.html',
        bmi=round(bmi, 2),
        exercise=exercise,
        time=time
    )


# RUN APP
if __name__ == '__main__':
    app.run(debug=True)