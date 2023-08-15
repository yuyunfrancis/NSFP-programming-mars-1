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
        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
        """
        #TODO: Implement the function
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
        stock_description = ""
        for product in self.products:
            stock_description += (
                f"Code: {product.code}\n"
                f"Name: {product.name}\n"
                f"Brand: {product.brand}\n"
                f"Description: {product.description}\n"
                f"Quantity: {product.quantity}\n"
                f"Price: {product.price}\n"
                f"Requires Prescription: {product.requires_prescription}\n\n"
            )
        return stock_description
        #TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field