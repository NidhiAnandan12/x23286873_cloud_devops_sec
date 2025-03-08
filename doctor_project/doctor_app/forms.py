from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient

class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = UserCreationForm.Meta.fields + ('email','patient_address','patient_dob','patient_image')  