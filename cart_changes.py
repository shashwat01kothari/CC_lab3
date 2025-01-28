import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list[Product]:
    """
    Fetches the cart for a given username.
    Returns a list of Product objects in the user's cart.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Process the contents directly into Product objects
    items = []
    for cart_detail in cart_details:
        product_ids = json.loads(cart_detail["contents"])  # Safely parse JSON
        items.extend(get_product(prod_id) for prod_id in product_ids)

    return items

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


