from django.contrib.auth.forms import UserCreationForm
from .models import AppUser,Product,ProductCategory
from django import forms
class AppUserRegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = UserCreationForm.Meta.fields + ('email','address',)  

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('__all__')