from flask import Flask, request, jsonify,render_template
from insurance import InsurancePredictor

app = Flask(__name__)
predictor = InsurancePredictor()

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    children = request.form.get('children')
    smoker = 'Yes' if 'smoker' in request.form else 'No'
    region = request.form.get('region')

    # Perform prediction using the predictor
    prediction = predictor.predict_insurance(age, sex, bmi, children, smoker, region)

    # Return prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run()