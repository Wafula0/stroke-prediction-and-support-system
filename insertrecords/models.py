from django.db import models
from cryptography.fernet import Fernet
import base64
import os
# Create your models here.
# Generate a key only once and store it securely
ENCRYPTION_KEY = os.environ.get("DJANGO_ENCRYPTION_KEY", Fernet.generate_key().decode())
#os.environ.get("DJANGO_ENCRYPTION_KEY")
fernet = Fernet(ENCRYPTION_KEY.encode())

class HealthRecords(models.Model):
    Gender = models.CharField(max_length=255)
    Age = models.IntegerField()
    Hypertension = models.CharField(max_length=255)
    Heartdisease = models.CharField(max_length=255)
    Evermarried = models.CharField(max_length=255)
    Worktype = models.CharField(max_length=255)
    Residencetype = models.CharField(max_length=255)
    Glucoselevel = models.CharField(max_length=255)  # Store as encrypted string
    Bmi = models.CharField(max_length=255)  # Store as encrypted string
    Smokingstate = models.CharField(max_length=255)
    Strokestatus = models.CharField(max_length=255)

    class Meta:
        db_table = 'HealthRecords'

    def save(self, *args, **kwargs):
        """Encrypt sensitive fields before saving"""
        self.Hypertension = fernet.encrypt(str(self.Hypertension).encode()).decode()
        self.Heartdisease = fernet.encrypt(str(self.Heartdisease).encode()).decode()
        self.Glucoselevel = fernet.encrypt(str(self.Glucoselevel).encode()).decode()
        self.Bmi = fernet.encrypt(str(self.Bmi).encode()).decode()
        super().save(*args, **kwargs)

    def decrypt_fields(self):
        """Decrypt sensitive fields when retrieving"""
        self.Hypertension = fernet.decrypt(self.Hypertension.encode()).decode()
        self.Heartdisease = fernet.decrypt(self.Heartdisease.encode()).decode()
        self.Glucoselevel = fernet.decrypt(self.Glucoselevel.encode()).decode()
        self.Bmi = fernet.decrypt(self.Bmi.encode()).decode()
        return self