from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('doctors', views.Doctors, name='doctors'),

    
    
    
    
    path('register', views.Register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='doctor_app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
  





]