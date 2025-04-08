from django.shortcuts import render
from .models import HealthRecords

# Create your views here.

def insertRecords(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        age = request.POST['age']
        hypertension = request.POST['hypertension']
        heartdisease = request.POST['heart_disease']
        evermarried = request.POST['ever_married']
        worktype = request.POST['work_type']
        residencetype = request.POST['Residence_type']
        glucoselevel = request.POST['avg_glucose_level']
        bmi = request.POST['bmi']
        smokingstatus = request.POST['smoking_status']
        strokestatus = request.POST['stroke_status']

        records = HealthRecords(
            Gender=gender,
            Age=age,
            Hypertension=hypertension,
            Heartdisease=heartdisease,
            Evermarried=evermarried,
            Worktype=worktype,
            Residencetype=residencetype,
            Glucoselevel=glucoselevel,  # Will be encrypted in the model
            Bmi=bmi,  # Will be encrypted in the model
            Smokingstate=smokingstatus,
            Strokestatus=strokestatus
        )
        records.save()

    return render(request, 'healthrecords.html')


def view_records(request):
   records = HealthRecords.objects.all()
   for record in records:
        record.decrypt_fields()  # Decrypt sensitive fields before displaying

        return render(request, 'records.html', {'records': records})

