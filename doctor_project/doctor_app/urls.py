from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('doctors', views.Doctors, name='doctors'),
    path('createdoctor',views.CreateDoctor ,name='adminCreateDoctor'),
    path('updatedoctor/<int:doctor_id>',views.UpdateDoctor ,name='adminUpdateDoctor'),
    path('deletedoctor/<int:doctor_id>',views.DeleteDoctor ,name='adminDeleteDoctor'),
    path('viewdoctor',views.AdminViewDoctors ,name='adminViewDoctors'),
    path('searchdoctor',views.DoctorSearch ,name='doctorSearch'),

    path('createdepartment',views.CreateDepartment ,name='adminCreateDepartment'),
    path('updatedepartment/<int:department_id>',views.UpdateDepartment ,name='adminUpdateDepartment'),
    path('deletedepartment/<int:department_id>',views.DeleteDepartment ,name='adminDeleteDepartment'),
    path('viewdepartment',views.ViewDepartment ,name='adminViewDepartment'),

    path('bookdoctor/<int:doctor_id>',views.BookDoctorAppoinment ,name='bookDoctorAppoinment'),

    
    
    
    
    path('register', views.Register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='doctor_app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
  





]