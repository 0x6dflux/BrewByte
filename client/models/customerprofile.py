from django.db import models
from django.conf import settings

from general.models import BaseModel

AUTH_USER = settings.AUTH_USER_MODEL


class CustomerProfile(BaseModel):
    class CustomerSegment(models.IntegerChoices):
        GOLD = 1
        SILVER = 2
        BRONZE = 3

    user_id = models.OneToOneField(AUTH_USER, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=10, blank=True, null=True)
    first_visit_date = models.DateField(blank=True, null=True)
    last_visit_date = models.DateField(blank=True, null=True)
    customer_segment = models.IntegerField(
        choices=CustomerSegment,
        blank=True,
        null=True,
    )
    loyalty_points = models.IntegerField(default=0, db_default=0)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=False, db_default=False)

    def __str__(self):
        return f"{self.user_id}-customer-profile"
