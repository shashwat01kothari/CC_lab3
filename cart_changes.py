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
"""
Reason for changing :
The optimized get_cart function improves readability and performance by streamlining the logic and reducing redundancy. 
It first checks if cart_details is empty and exits early, avoiding unnecessary processing. The nested loops are flattened by 
directly iterating through the product IDs in cart_detail["contents"] and appending the corresponding Product objects to the 
items list using a generator expression. This approach eliminates intermediate lists, simplifies the code structure, and ensures 
the function is efficient and easy to maintain.
"""
    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


