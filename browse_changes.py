from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])



def list_products() -> list[Product]:
    """Fetches all products from the DAO and returns a list of Product objects."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches a single product by ID and returns it as a Product object."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)

"""
Reason for changing :

The use of list comprehension in list_products replaces the manual loop and append method, providing a more concise and efficient way to process products. Additionally, error handling in get_product ensures the function raises an error if no product is found for the given product_id, enhancing robustness and preventing unexpected behavior.
"""




def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)


