from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class DoctorDepartment(models.Model):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name



class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True,db_column='doctor_id')
    doctor_name = models.CharField(max_length=100)
    doctor_age = models.IntegerField()
    doctor_department = models.ForeignKey(DoctorDepartment, on_delete=models.CASCADE,null=False)
    doctor_image = models.ImageField(upload_to="images/doctor",default=None)
    doctor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.doctor_name

class Patient(AbstractUser):
    patient_address = models.TextField(max_length=500, null=False)
    patient_dob = models.DateField(default=None,null=True,blank=True)
    patient_image = models.ImageField(upload_to="images/patient",default=None)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    class AppoinmentStatus(models.TextChoices):
        Confirmed = "Confirmed"    
        CANCELLED = "Cancelled"
        COMPLETED = "Completed"
    appointment_id = models.AutoField(primary_key=True,db_column='appointment_id')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=False)
    appointment_patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=False)
    appoinment_booking_status = models.CharField(max_length=30,choices=AppoinmentStatus.choices,default=AppoinmentStatus.Confirmed.value)
    appoinment_doctor_remarks = models.TextField(max_length=500, null=True)
    
    



