import pytest
from django.utils import timezone
from doctor_app.models import DoctorDepartment

@pytest.mark.django_db

def test_doctor_department_creation():

    department = DoctorDepartment.objects.create(department_name="TestDepartment",)

    assert department.department_name == "TestDepartments"

    # assert str(post) == "Test"
