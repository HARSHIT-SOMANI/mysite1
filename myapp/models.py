import email
from django.db import models

# Create your models here.
class business_registration(models.Model):
    name=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=150,null=True)
    phoneNumber=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=225,null=True)
    regId=models.CharField(max_length=225,null=True)
    class Meta:
        managed=False
        db_table='business_registration'