from django.db import models

# Create your models here.

class HealthRecords(models.Model):
    Gender = models.IntegerField()
    Age =models.IntegerField()
    Hypertension = models.IntegerField()
    Heartdisease = models.PositiveIntegerField()
    Evermarried = models.IntegerField() 
    Worktype = models.IntegerField()
    Residencetype = models.IntegerField()
    Glucoselevel = models.FloatField()
    Bmi = models.FloatField()
    Smokingstate = models.IntegerField()
    Strokestatus = models.PositiveIntegerField()


    class Meta:
        db_table = 'HealthRecords'