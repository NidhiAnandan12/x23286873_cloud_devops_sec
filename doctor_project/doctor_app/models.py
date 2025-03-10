from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class DoctorDepartment(models.Model):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name



class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True,db_column='doctor_id')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(DoctorDepartment, on_delete=models.CASCADE,null=False)
    image = models.ImageField(upload_to="images/doctor",default=None)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

class Patient(AbstractUser):
    address = models.TextField(max_length=500, null=False)
    dateofbirth = models.DateField(default=None,null=True,blank=True)
    image = models.ImageField(upload_to="images/patient",default=None)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    class AppoinmentStatus(models.TextChoices):
        Confirmed = "Confirmed"    
        CANCELLED = "Cancelled"
        COMPLETED = "Completed"
    appointment_id = models.AutoField(primary_key=True,db_column='appointment_id')
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=False)
    booking_status = models.CharField(max_length=30,choices=AppoinmentStatus.choices,default=AppoinmentStatus.Confirmed.value)
    doctor_remarks = models.TextField(max_length=500, null=True)
    
    



