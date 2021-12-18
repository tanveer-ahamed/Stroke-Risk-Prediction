## importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            gender = request.form['gender']
            if(gender=='Male'):
                gender=1
            else:
                gender=0
            age=int(request.form['age'])
            hypertension = request.form['hypertension']
            if(hypertension=='yes'):
                hypertension=1
            else:
                hypertension=0
            heart_disease = request.form['heart_disease']
            if(heart_disease=='yes'):
                heart_disease=1
            else:
                heart_disease=0
            ever_married = request.form['ever_married']
            if(ever_married=='yes'):
                ever_married=1
            else:
                ever_married=0
            work_type = request.form['work_type']
            if(work_type=='Govt_job'):
                work_type=0
            elif(work_type=='children'):
                    work_type = 1
            elif(work_type=='Private'):
                    work_type = 2
            elif(work_type=='Self-employed'):
                    work_type = 3
            else:
                work_type=4   
            Residence_type = request.form['Residence_type']
            if(Residence_type=='Urban'):
                Residence_type=1
            else:
                Residence_type=0
            avg_glucose_level=float(request.form['avg_glucose_level'])
            bmi=float(request.form['bmi'])
            smoking_status = request.form['smoking_status']
            if(smoking_status=="formerly smoked"):
                smoking_status=0
            elif(smoking_status == "never smoked"):
                smoking_status = 1
            else:
                smoking_status = 2
            
            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
                    
                    
         
            

            
               
                 
           
            
            
