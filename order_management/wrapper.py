from .cart import Cart
from .stock import Stock
from .product import Product
from .prescription import Prescription
from datetime import datetime

import json


## would need to     create a new object for each new order
class Wrapper:
    """
    Main class used to manage orders and carts.

    Attributes:
        sales: A list of the sales done during the program's execution
        stock: The stock used in the execution
        agentID: the username of the pharmacist running the program
    """

    def __init__(self, stock: Stock, agentID: str, prescriptions_file: str,) -> None:
        self.sales = []
        self.stock = stock
        self.agentID = agentID
        self.prescriptions_file = prescriptions_file

    def checkout(self, cart: Cart, customer_id: str, prescription: Prescription = None):
        """Handles the checkout procedure of the program.

        Args:
            cart: The cart to pay for
            customer_id: the ID of the customer
            prescription: the prescription that accompanies the order (default: None)
        """
        # Check if there are products in the cart
        if not cart.products:
            print("Cart is empty. Nothing to checkout.")
            return

        total_price = cart.cost  # Calculate the total price from the cart
        print("Total Price:", total_price)

        # Update the stock's product quantities and mark prescription items as complete
        for product_code, quantity in cart.products.items():
            product = self.stock.getProductByID(product_code)
            # product.decrementQuantity(quantity)
            if prescription:
                prescription.markComplete(product)
            sale = {
                "timestamp": datetime.now().isoformat(),
                "customerID": customer_id,
                "name": product.name,
                "doctorName": prescription.DoctorName,
                "salesperson": self.agentID,
                "price": product.price,
                "total_price": total_price,
                "prescriptionID": prescription.PrescriptionID,
                "cart_items": cart.products
            }
            self.sales.append(sale)
        # Create a sale record
        # Clear the cart after successful checkout
        cart.clear()

        print("Checkout successful. Sale recorded.")
        # Print the updated sales dictionary
        print("\nUpdated Sales Dictionary:")
        print(self.sales)

        # TODO: First check that all the product that require a prescription have all the criteria met
        # (i.e., (1) there is a prescription that (2) matches the customer's ID, and (3) contains the medication
        # in the specified quantity).
        # Raise an exception if either of those conditions is unmet.

        # TODO: Get the current datetime and save a Sale information for each product sold with the following schema
        # {"name": "<name>", "quantity": <quantity>, "price": <unit price>, "purchase_price": <total price>, "timestamp": <timestamp>,
        # "customerID": <customer username>, "salesperson": <pharmacist username>}

        # TODO: Append the list to the current sales

        # TODO: Make sure that the sold products are marked as complete in the prescriptions.

    def dump(self, outfile: str):
        """Dumps the current sales data to a file

        Args:
            outfile: the path to the output file
        """
        # TODO: Load the content, if any of the existing file

        # TODO: Update the content by appending the new entries to it, and save to the file
