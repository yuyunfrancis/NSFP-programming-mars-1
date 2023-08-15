from .product import Product
from .stock import Stock


class Cart:

    def __init__(self, stock: Stock) -> None:
        self.cart = Cart
        self.products = {}
        self.stock = stock

    def add(self, code: str, quantity1: int):
        try:
            product = self.stock.getProductByID(code)
            if quantity1 <= 0:
                print("Invalid quantity. Please enter a positive quantity.")
            elif quantity1 > product.quantity:
                print("Not enough stock available for the selected quantity.")
            else:
                if code in self.products:
                    self.products[code] += quantity1
                else:
                    self.products[code] = quantity1
                print(f"{quantity1} {product.code} {product.name} added to the cart.")

            print("\nProducts in cart:")
            print("{:^20} | {:^20} | {:^10} | {:^15}".format("Product Name", "Product ID", "Quantity", "Price"))
            print("-" * 75)
            total_price = 0
            for cart_code, quantity in self.products.items():
                product = self.stock.getProductByID(cart_code)
                price = product.price * quantity
                trimmed_id = product.code[:20] if len(product.code) > 20 else product.code
                print("{:<20} | {:<20} | {:^10} | {:>15}".format(product.name, trimmed_id, quantity, price))

            print("-" * 75)
            print("{:^20} | {:^20} | {:^10} | {:>15}".format("Total Price", "", "", self.cost))

        except ValueError as e:
            print(e)

    def display_cart(self):
        """Display the contents of the cart"""
        if not self.products:
            print("Cart is empty.")
            return

        print("Cart Contents:")
        print("{:<10} {:<30} {:<10} {:<10}".format("Product ID", "Product Name", "Quantity", "Price"))
        print("=" * 60)

        for product_code, quantity in self.products.items():
            product = self.stock.getProductByID(product_code)
            print("{:<10} {:<30} {:<10} {:<10}".format(product.code, product.name, quantity, product.price))

        print("=" * 60)

    def __str__(self) -> str:
        """String representation of the cart
        """
        # TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to
        return NotImplemented

    def remove_from_cart(self, product_code: str):

        if product_code in self.products:
            product = self.stock.getProductByID(product_code)
            removed_quantity = self.products.pop(product_code)
            print(f"{removed_quantity} {product.name} removed from the cart.")
        else:
            print("Product not found in the cart.")

    def clear(self):
        self.products = {}

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        total_cost = 0
        for code, quantity in self.products.items():
            product = self.stock.getProductByID(code)
            total_cost += product.price * quantity
        return total_cost
