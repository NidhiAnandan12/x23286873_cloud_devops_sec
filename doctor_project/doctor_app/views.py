from django.shortcuts import render
from .forms import AppUserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import DoctorDepartment,Doctor,Appointment,Patient
from .forms import CreateDoctorForm,CreateDepartmentForm,CreateAppoinmentForm
from django.core.mail import send_mail
from django.conf import settings




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

def CreateDoctor(request):
     if request.method == "POST":
        form = CreateDoctorForm(request.POST,request.FILES)
        form.save()
        if form.is_valid():
          return redirect('doctors')
     else:   
          form = CreateDoctorForm()
          return render(request, 'doctor_app/createdoctor.html', {"form": form})

def UpdateDoctor(request, doctor_id):
    doctor = Doctor.objects.get(doctor_id=doctor_id)
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST,request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request,"Doctor Updated Successfully.")
            return redirect('adminViewDoctors')
    else:
        form = CreateDoctorForm(instance=doctor)

    return render(request,'doctor_app/updatedoctor.html',{'form': form})

def DeleteDoctor(request, doctor_id):
    doctor = Doctor.objects.get(doctor_id=doctor_id)
    doctor.delete()
    return redirect('adminViewDoctors')

def AdminViewDoctors(request):
     doctors = Doctor.objects.all()
     doctors_context = {'doctors' :doctors}
     return render(request,'doctor_app/admin_view_doctors.html',doctors_context)

def DoctorSearch(request):        
    if request.method == 'GET': 
          doctor_name =  request.GET.get('search')    
          doctors = Doctor.objects.filter(doctor_name__icontains=doctor_name) 
          if not doctors:
               messages.error(request,f"No doctors found for {doctor_name}")
               return redirect('doctors')
          doctors_context = {'doctors': doctors,'doctor_search' :True}
          return render(request, 'doctor_app/doctors.html', doctors_context)
    
def CreateDepartment(request):
     if request.method == "POST":
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request,"Department created successfully")
          return redirect('adminViewDepartment')
     else:   
          form = CreateDepartmentForm()
          return render(request, 'doctor_app/create_department.html', {"form": form})




def UpdateDepartment(request, department_id):
    department = DoctorDepartment.objects.get(id=department_id)
    if request.method == 'POST':
        form = CreateDepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Category updated Successfully.")
            return redirect('adminViewDepartment')
    else:
        form = CreateDepartmentForm(instance=department)

    return render(request,'doctor_app/update_department.html',{'form': form})

def ViewDepartment(request):
     departments = DoctorDepartment.objects.all()
     departments_items_context = {'departments' :departments}
     return render(request,'doctor_app/admin_view_department.html',departments_items_context)

def DeleteDepartment(request, department_id):
    department = DoctorDepartment.objects.get(id=department_id)
    department.delete()
    messages.success(request,"Department Deleted Successfully.")
    return redirect('adminViewDepartment')

def BookDoctorAppoinment(request,doctor_id):
    doctor = Doctor.objects.get(doctor_id=doctor_id)
    if request.method == "POST":
        form = CreateAppoinmentForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request,"Appoinment created successfully")
          return redirect('doctors')
        else:
            # Show error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            form = CreateAppoinmentForm(instance=doctor)
            return render(request, 'doctor_app/book_appoinment.html', {"form": form})

    else:   
         form = CreateAppoinmentForm(instance=doctor)
         return render(request, 'doctor_app/book_appoinment.html', {"form": form})
    

def MyAppoinments(request):
         if request.user.is_superuser: 
               all_appoinments = Appointment.objects.all()
               appoinment_context= {'appoinments':all_appoinments }
               return render(request, 'doctor_app/my_appoinments.html',appoinment_context)  
         else:
              all_appoinments = Appointment.objects.filter(user = request.user)
              appoinment_context= {'appoinments':all_appoinments }
              return render(request, 'doctor_app/orders.html',appoinment_context)    

def AppoinmentDetails(request,appoinment_id):
     appoinment = Appointment.objects.get(appointment_id=appoinment_id)
     appoinment_context = {'appoinment': appoinment, 'appoinment_status_choices': Appointment.AppoinmentStatus.choices}
     return render(request, 'doctor_app/appoinment_details.html', appoinment_context) 

def updateAppoinmentStatus(request, appoinment_id):
    appointment = Appointment.objects.get(appointment_id=appoinment_id)
    if request.method == "POST":
        new_status = request.POST.get("appoinment_status")  
        doctor_remarks = request.POST.get("doctor_remarks")
        print(doctor_remarks)
        if new_status in dict(Appointment.AppoinmentStatus.choices):  
            appointment.appoinment_booking_status = new_status
            appointment.appoinment_doctor_remarks = doctor_remarks
            appointment.save()
            address = appointment.appointment_patient.email
            subject = f'Cloud Devops Project - Doctor Appoinment Update- {appoinment_id}'
            message = f'Your Doctor Appoinment with appoinment  id {appoinment_id} placed on {appointment.appointment_date:%d-%m-%Y} status has been changed to {new_status}. with the following doctors remarks {appointment.appoinment_doctor_remarks}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
            messages.success(request,"Appoinment Status updated successfully and the mail has been sent to the Patient.")
    return redirect("appoinmentDetails", appoinment_id=appoinment_id)


    
    
    

