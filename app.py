#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/Pickled_LR_Model', 'rb') as f:
    logistic = pickle.load(f)




def get_predictions(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal, req_model):
    mylist = [age,sex,cp,trestbps]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]

    
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        price = request.form['age']
        Tax = request.form['sex']
        Driver_Age = request.form['cp']
        Licence_Length_Years = request.form['trestbps']
        req_model = request.form['req_model']

        target = get_predictions(age, sex,cp,trestbps, req_model)

        if target==1:
            heart_disease = 'Patient is likely to get heart disease'
        else:
            heart_disease = 'Patient is unlikely to get heart disease'

        return render_template('home.html', target = target, sale_making = heart_disease)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
