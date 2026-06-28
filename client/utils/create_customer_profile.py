from django.db import IntegrityError
from client.models import User, CustomerProfile


def create_customer_profile(user: User) -> CustomerProfile:

    try:
        customer_profile = CustomerProfile.objects.get(user_id=user)
        return customer_profile
    except CustomerProfile.DoesNotExist:
        while True:
            try:
                last_profile = CustomerProfile.objects.order_by("-id").first()
                if last_profile:
                    last_seq = int(last_profile.customer_id.split("-")[-1])
                    new_seq = last_seq + 1
                else:
                    new_seq = 1
                CustomerProfile.objects.create(
                    user_id=user,
                    customer_id=f"CPI-{new_seq:04d}",
                    referral_code=f"CRC{user.phone_number[-4:]}",
                    is_active=True,
                )
                return CustomerProfile
            except IntegrityError:
                continue
