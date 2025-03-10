from django.contrib import admin
from .models import Doctor,DoctorDepartment,Patient,Appointment
from django.contrib.auth.admin import UserAdmin


admin.site.register(DoctorDepartment)
admin.site.register(Doctor)
admin.site.register(Appointment)

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('patient_address','patient_dob','patient_image',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('patient_address','patient_dob','patient_image',)}),
    )


admin.site.register(Patient, CustomUserAdmin)