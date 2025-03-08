from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,DoctorDepartment,Doctor,Appointment

class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = UserCreationForm.Meta.fields + ('email','patient_address','patient_dob','patient_image')  


class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('__all__')

class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = DoctorDepartment
        fields = ('__all__')

class CreateAppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date','appointment_time','appointment_doctor','appointment_patient')
        widgets = {
            'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),
            'appointment_time': forms.TimeInput(attrs={'class': 'form-control', 'type': "time"}),
            'appointment_doctor': forms.Select(attrs={'class': 'form-control'}),
            'appointment_patient': forms.Select(attrs={'class': 'form-control'})
        }