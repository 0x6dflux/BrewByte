from django.db import IntegrityError
from client.models import User


def set_user_code(user: User):
    if not user.user_code:
        while True:
            try:
                last_user = User.objects.order_by("-id").first()
                if last_user:
                    last_seq = int(last_user.user_code.split("-")[-1])
                    new_seq = last_seq + 1
                else:
                    new_seq = 1

                user.user_code = f"USR-{new_seq:04d}"
                user.save()
                return True
            except IntegrityError:
                continue
