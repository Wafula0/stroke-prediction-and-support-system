from django.shortcuts import render
from joblib import load
model=load('C:/Users/Admin/Desktop/stroke prediction and support system/predictor/savedmodel/model.joblib')
# Create your views here.
def predict(request):
    return render(request,'predict.html')

def results(request):
    
    gender=request.POST['gender']
    age=request.POST['age']
    hypertension=request.POST['hypertension']
    heart_disease=request.POST['heart_disease']
    ever_married=request.POST['ever_married']
    work_type=request.POST['work_type']
    Residence_type=request.POST['Residence_type']
    avg_glucose_level=request.POST['avg_glucose_level']
    bmi=request.POST['bmi']
    smoking_status=request.POST['smoking_status']

    y_predict=model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
    if y_predict==0:
        y_predict='you are not likely to suffer from stroke'
    else:
    
        y_predict='you are likely to suffer from stroke'


    return render(request,'results.html',{'results':y_predict})

