from client.models import Address


class ClientCheckoutService:
    @staticmethod
    def checkout_address(user):
        addresses = Address.objects.filter(user_id=user)
        return addresses
