from django.db import models
from client.models import User

class CustomerProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=10 , blank=True, null=True)
    first_visit_date = models.DateField(blank=True, null=True)
    last_visit_date = models.DateField(blank=True, null=True)
    customer_segment = models.CharField(max_length=10 ,blank=True, null=True)
    loyalty_points = models.IntegerField(default=0, db_default=0)
    referral_code = models.CharField(max_length=10,blank=True, null=True)
    is_active = models.BooleanField()