from django.shortcuts import render

def index(request):
     return render(request, 'doctor_app/index.html')
