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