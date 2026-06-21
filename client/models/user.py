from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=14, unique=True)
    user_code = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    birthday = models.DateField(blank=True, null=True)
    is_customer = models.BooleanField(default=False, db_default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name","username", "email"]

    def __str__(self):
        return self.phone_number
    
    def save(self, *args, **kwargs):
        self.set_user_id()
        super().save(*args, **kwargs)

    def set_user_id(self):
        if not self.user_code:
            last_user = User.objects.order_by("-id").first()
            if last_user:
                last_seq = int(last_user.user_code.split("-")[-1])
                new_seq = last_seq + 1
            else:
                new_seq = 1
        
            self.user_code = f"USR-{new_seq:04d}"