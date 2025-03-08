from django.shortcuts import render
from .forms import AppUserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import DoctorDepartment,Doctor,Appointment,Patient


def index(request):
     return render(request, 'doctor_app/index.html')

def Register(request):
    if request.method == 'POST':
        form = AppUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"Registration has been successfull, and the registerd user has been logged in") 
            return redirect('/')
    else:
        form = AppUserRegisterForm()
        return render(request, 'doctor_app/register.html', {'form': form}) 

def Doctors(request):
     doctors = Doctor.objects.all()
     doctors_context = {'doctors': doctors}
     return render(request, 'doctor_app/doctors.html', doctors_context)
