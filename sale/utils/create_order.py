from client.models import User
from sale.models import OrderModel, CartModel
from sale.utils import get_tax_ratio


def create_order(user: User, cart: CartModel) -> OrderModel:
    tax_ratio = get_tax_ratio()
    order = OrderModel.objects.create(
        user_id=user,
        cart_id=cart,
        total_amount=cart.total_amount,
        discount=0,
        discounted_amount=cart.total_amount,
        tax=cart.total_amount * tax_ratio,
        taxed_amount=cart.total_amount * (1 + tax_ratio),
    )
    return order
