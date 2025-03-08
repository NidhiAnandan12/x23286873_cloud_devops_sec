from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,DoctorDepartment,Doctor,Appointment

class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = UserCreationForm.Meta.fields + ('email','patient_address','patient_dob','patient_image')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'patient_address': forms.Textarea(attrs={'class': 'form-control'}),
            'patient_dob': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),
            'patient_image': forms.FileInput(attrs={'class': 'form-control'}),
        }  


class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('__all__')
        widgets = {
           'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
           'doctor_age': forms.NumberInput(attrs={'class': 'form-control'}),    
              'doctor_department': forms.Select(attrs={'class': 'form-control'}),
                'doctor_image': forms.FileInput(attrs={'class': 'form-control'}),
                'doctor_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = DoctorDepartment
        fields = ('__all__')
        widgets = {
            'department_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

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