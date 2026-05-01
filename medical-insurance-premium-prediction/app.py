import numpy as np


from flask import Flask, request, render_template
import pickle
import pandas as pd

#Create an app object using the Flask class.
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('train.pkl', 'rb'))

#Define the route to be home.
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory.
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder.

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def man():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission.
#Redirect to /predict page with the output

@app.route('/predict', methods=['GET','POST'])

def predict():
    if request.method == "POST":
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        if(gender=='male'):
            gender = 0
        elif(gender=='female'):
            gender = 1
        bmi = float(request.form.get('bmi'))
        children = int(request.form.get('children'))
        smoker = request.form.get('smoker')
        if request.form.get('smoker') == 'yes':
            smoker = 0
        else:
            smoker = 1
        region = request.form.get('region')
        if(region=='southeast'):
            region = 0
        elif(region=='southwest'):
            region = 1
        elif(region=='northeast'):
            region = 2
        elif(region=='northwest'):
            region = 3
        # The model was trained on these six features in this order:
        # age, gender, bmi, children, smoker, region
        prediction = model.predict([[
            age,
            gender,
            bmi,
            children,
            smoker,
            region
        ]])

        output=round(prediction[0],2)
   
   
   
   
   
    return render_template('after.html', prediction_text=' Rs. {}'.format(output),data=output)
    #return render_template('after.html', prediction_text='Insurance cost is {}'.format(prediction))



if __name__ == "__main__":
    app.run(debug=True)

'''if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080, threads=2, url_prefix="/my-app")'''
app.run()

