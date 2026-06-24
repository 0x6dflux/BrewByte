from django.db import models
from django.contrib.auth import get_user_model

from general.models import BaseModel
AUTH_USER = get_user_model()

class ManagerProfile(BaseModel):
    user_id = models.OneToOneField(AUTH_USER, on_delete=models.CASCADE, blank=True, null=True)
    employee_id = models.CharField(max_length=10, blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=150, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=13, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=False)
    employment_type = models.CharField(max_length=10, blank=True, null=False)
    hired_date = models.DateField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    technical_skills = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
