from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, unique=True)
    user_code = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="customuser_set",
        related_query_name="user",
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name","username"]

    def __str__(self):
        return self.phone_number
    
    def save(self, *args, **kwargs):
        if not self.user_code:
            last_user = CustomUser.objects.order_by("-id").first()
            if last_user:
                last_seq = int(last_user.user_code.split("-")[-1])
                new_seq = last_seq + 1
            else:
                new_seq = 1
        
            self.user_code = f"USR-{new_seq:04d}"
        super().save(*args, **kwargs)