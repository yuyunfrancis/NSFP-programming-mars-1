import json
from typing import List

from .product import Product

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, code: str, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be update (+1 adds 1, -2 removes 2 for example)
        """
        #TODO: Make sure the product exists, and that by making the change, the value is still >= 0
        
        #TODO: Update the quantity
        product = self.getProductByID(code)
        if product is None:
            print("Product not found.")
            return

        # Calculate the new quantity
        new_quantity = product.quantity + change
        if new_quantity >= 0:
            product.quantity = new_quantity
            print(f"Quantity for {product.name} updated to {product.quantity}.")
        else:
            print("Quantity cannot be negative.")

    def getProductByID(self, code: str) -> Product | None:
        """Gets a product by its ID

        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        #TODO: Implement te function1
        for product in self.products:
            if product.code == code:
                return product
        
    def dump(self, outfile: str):
        """Saves the stock to a JSON file"""
        #TODO: Implement the function
        stock_data = [product.to_dict() for product in self.products]
        with open(outfile, 'w') as f:
            json.dump(stock_data, f, indent=4)
    
    @staticmethod
    def load(infile: str):
        with open(infile, 'r') as f:
            stock_data = json.load(f)
            products = [
                Product(code=data['code'], name=data['name'], brand=data['brand'], description=data['description'],
                        quantity=data['quantity'], price=data['price'],
                        requires_prescription=data['requires_prescription'],
                        category=data['category'], dosage_instruction=data['dosage_instruction'])
                for data in stock_data]
            return Stock(products)

    def __str__(self) -> str:
        """Returns a string representation of the stock
        """
        stock_description = "{:^4} | {:^38} | {:^25} | {:^15} | {:^50} | {:^8} | {:^15} | {:^20}\n".format(
            "No.", "Code", "Name", "Brand", "Description", "Quantity", "Price", "Requires Prescription"
        )
        stock_description += "-" * 215 + "\n"

        for idx, product in enumerate(self.products, start=1):
            code_display = product.code[:20]  # Display only the first 20 characters of the code
            name_display = product.name[:25]
            brand_display = product.brand[:15]
            description_display = product.description[:50]

            stock_description += "{:^4} | {:^38} | {:^25} | {:^15} | {:^50} | {:^8} | {:^15.2f} | {:^20}\n".format(
                idx, code_display, name_display, brand_display, description_display,
                product.quantity, product.price, product.requires_prescription
            )

        return stock_description

        #TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field