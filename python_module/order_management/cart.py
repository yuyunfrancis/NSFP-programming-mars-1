from .product import Product
from .stock import Stock

class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity
        added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock

    def add(self, productCode: str, quantity: int):
        """Adds a product to the cart with the specified quantity
        
        Args:
            productCode: the identifier of the product
            quantity: quantity to add

        Returns: None
        """
        #TODO: Make sure the quantity is valid (> 0 and <= to the quantity in the stock)
        #TODO: If the product was already in the cart, increment the quantity
        
        #TODO: After the checks, add the product to the dictionary
        if self.products.get(productCode) is not None:
            if (self.products[productCode]["quantity"] + quantity <= self.stock.getProductByID(productCode)["quantity"] and quantity > 0):
                self.products[productCode] = self.stock.getProductByID(productCode).quantity
        else:
            if (quantity > 0 and self.stock.getProductByID(productCode)["quantity"] >= quantity):
                self.produts[productCode] = quantity
    def __str__(self) -> str:
        """String representation of the cart
        """
        #TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to

        return NotImplemented

    def remove(self, code):
        """
        Removes a specific product from the cart """
        #TODO: Removes a product from the cart. safely fail if the product code is not found
        try:
            del self.products[code]
        except KeyError:
            print("Product not found")

    def clear(self):
        """Clears up the cart.
        """
        self.products.clear()

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        #TODO: implement the function
        price = 0
        for product in self.products:
            price += product["price"]

        return price

    