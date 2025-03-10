from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,DoctorDepartment,Doctor,Appointment

class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = UserCreationForm.Meta.fields + ('email','address','dateofbirth','image')
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
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'age': forms.NumberInput(attrs={'class': 'form-control'}),    
              'department': forms.Select(attrs={'class': 'form-control'}),
                'image': forms.FileInput(attrs={'class': 'form-control'}),
                'cost': forms.NumberInput(attrs={'class': 'form-control'}),
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
        fields = ('date','time','doctor','patient')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': "time"}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'})
        }