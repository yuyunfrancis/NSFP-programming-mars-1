import json

from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription
from .cart import Cart
from .wrapper import Wrapper
import os

MSG_WRONG_INPUT = "Wrong input. Try again!"


class Menu:
    """Represents the menu class for the project

    Attributes: 
        stock: stock variable
        profiles: user management module
        pharmacist: account of the salesperson
        records_file: path to the file containing the sales
        prescriptions_file: path to the file containing the prescriptions.
        stock_file: path to the file containing the stock data
    """

    def __init__(self, stock: Stock, profiles: UserManagement, pharmacist: User, records_file: str,
                 prescriptions_file: str, stock_file: str, wrapper: Wrapper) -> None:
        self.wrapper = wrapper
        self.stock = stock
        self.profiles = profiles
        self.pharmacist = pharmacist
        self.cart = Cart(stock=stock)
        # use the file instead of the object so that we can keep track
        self.records_file = records_file
        self.prescriptions_file = prescriptions_file
        self.stock_file = stock_file

    def display_order_management_menu(self):
        """Display the order management menu"""
        print("******************************************")
        print("Order Management and Analytics Menu:")
        print("[Loc:.order_management.menu]")
        print("******************************************")
        print("1. Add to a cart")
        print("2. Remove from a cart")
        print("3. Clear the cart")
        print("4. Checkout")
        print("5 Back")

    def display_analytics_menu(self):
        """Display the analytics menu"""
        print("******************************************")
        print("Order Management and Analytics Menu:")
        print("[Loc:.analytics_menu]")
        print("******************************************")
        print("1. Total income from purchases")
        print("2. Prescription statistics")
        print("3. Purchases for a user")
        print("4. Sales by an agent")
        print("5. Top sales")
        print("6. Back")

    def run(self):
        """Run the menu and process user input"""
        while True:
            print("\nMain Menu:")
            print("1. Order management")
            print("2. Analytics")
            print("3. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.run_order_management_menu()
            elif choice == '2':
                self.run_analytics_menu()
            elif choice == '3':
                print("Exiting the application.")
                break
            else:
                print(MSG_WRONG_INPUT)

    def run_order_management_menu(self):
        """Run the order management menu"""
        while True:
            self.display_order_management_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_to_cart()
            elif choice == '2':
                self.remove_from_cart()
            elif choice == '3':
                self.clear_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                return  # Return to the previous menu
            else:
                print(MSG_WRONG_INPUT)

            # Add this condition to return to the main menu only if explicitly chosen
            if choice != '5':
                return

    def run_analytics_menu(self):
        """Run the analytics menu"""
        while True:
            self.display_analytics_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.total_income()
            elif choice == '2':
                self.prescription_statistics()
            elif choice == '3':
                self.purchases_for_user()
            elif choice == '4':
                self.sales_by_agent()
            elif choice == '5':
                self.top_sales()
            elif choice == '6':
                return
            else:
                print(MSG_WRONG_INPUT)

    def add_to_cart(self):
        """Add a product to the cart"""
        # TODO: Implement the logic to add a product to the cart
        print("Available Products:")
        # for product in self.stock.products:
        #     print(f"ID: {product.code}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        print(self.stock.__str__())

        # Ask the user to enter the product ID and quantity
        product_id = int(input("Enter choice to add to the cart: "))
        quantity = int(input("Enter the quantity to add: "))
        self.cart.add(self.stock.products[product_id - 1].code, quantity)
        self.run_order_management_menu()
        # pass

    def remove_from_cart(self):
        """Remove a product from the cart"""
        self.cart.display_cart()

        if not self.cart.products:
            print("Cart is empty. Nothing to delete.")
            self.run_order_management_menu()
            return
        product_code = str(input("Enter the product code to remove: "))
        self.cart.remove_from_cart(product_code)
        self.run_order_management_menu()

    # TODO: Implement the logic to remove a product from the cart
    # pass

    def clear_cart(self):
        """Clear the cart"""
        # TODO: Implement the logic to clear the cart
        # pass
        self.cart.display_cart()

        if not self.cart.products:
            print("Cart is already empty.")
            input("Press Enter to go back to the cart menu...")
            self.run_order_management_menu()
            return

        confirmation = input("Are you sure you want to clear the cart? (y/n): ")
        if confirmation.lower() == 'y':
            self.cart.clear()
            print("Cart cleared successfully.")
        elif confirmation.lower() == 'n':
            print("Cart was not cleared.")

        input("Press Enter to go back to the cart menu...")
        self.run_order_management_menu()

    def display_prescription_data(self):
        with open(self.prescriptions_file, 'r') as file:
            prescriptions = json.load(file)

            if not prescriptions:
                print("No prescriptions found.")
                return

            print("Prescription Data:")
            print("|{:<15} | {:<20} | {:<25} | {:<25} {:<40} | {:<15}|".format("Prescription ID", "Doctor Name",
                                                                               "Customer ID",
                                                                               "Medication Name", "Medications",
                                                                               "Date"))
            print("=" * 125)

            for prescription in prescriptions:
                doctor_name = prescription["DoctorName"]
                prescription_id = prescription["PrescriptionID"]
                customer_id = prescription["CustomerID"]
                medications = prescription["Medications"]
                date = prescription["Date"]

                for med in medications:
                    medication_id = med['id']
                    medication_name = med['name']
                    medication_quantity = med['quantity']
                    print("| {:<15} | {:<20} | {:<25} | {:<25} | {:<40} | {:<15}|".format(prescription_id, doctor_name,
                                                                                          customer_id,
                                                                                          medication_name,
                                                                                          f"{medication_quantity} {medication_id}",
                                                                                          date))
                    print("-" * 125)

            # print("=" * 125)

    # Call the function with the prescription file path
    def checkout(self):
        """Checkout the cart"""
        if not self.cart.products:
            print("Cart is empty. Nothing to checkout.")
            return self.run_order_management_menu()

        # Display products in the cart
        print("Products in Cart:")
        self.cart.display_cart()

        # Display available products for reference
        print("\nAvailable Products:")
        print(self.display_prescription_data())

        customer_id = input("Enter customer ID: ")
        prescription_id = input("Enter prescription ID (if applicable, else press Enter): ")

        if prescription_id:
            prescription_data = Prescription.get(self.prescriptions_file, prescription_id)
            if not prescription_data:
                print("Prescription not found.")
                return

            prescription = Prescription(
                DoctorName=prescription_data["DoctorName"],
                PrescriptionID=prescription_data["PrescriptionID"],
                Medications=prescription_data["Medications"],
                CustomerID=prescription_data["CustomerID"],
                Date=prescription_data["Date"]
            )

            # Verify if products in cart are in prescription and match required quantities
            for product_code, quantity in self.cart.products.items():
                product = self.stock.getProductByID(product_code)
                if not prescription.medecineInPrescription(product, quantity):
                    print(
                        f"Product {product.name} with code {product.code} and quantity {quantity} not found in "
                        f"prescription or quantity does not match.")
                    return
            self.update_product_quantities(self.cart)

            self.wrapper.checkout(self.cart, customer_id, prescription)

            with open(self.records_file, 'r+') as sales_file:
                sales_data = json.load(sales_file)
                sales_data.append(self.wrapper.sales[-1])  # Append the last sale
                sales_file.seek(0)
                json.dump(sales_data, sales_file, indent=4)
                sales_file.truncate()
                print("Sales records updated successfully")
        self.cart.clear()

    def update_product_quantities(self, cart):
        with open(self.stock_file, 'r+') as file:
            products = json.load(file)
            for product_code, quantity in cart.products.items():
                product = next((p for p in products if p["code"] == product_code), None)
                if product:
                    product["quantity"] -= quantity

            file.seek(0)
            json.dump(products, file, indent=4)
            file.truncate()

    def total_income(self):
        """Calculate the total income from purchases"""
        total_income = 0

        with open(self.records_file, 'r') as sales_file:
            sales_data = json.load(sales_file)

            print("Sales Data:")
            print(
                "|{:<25} | {:<15} | {:<15} {:<20} | {:<15} | {:<15}|".format("Timestamp", "Total Price", "Customer ID",
                                                                             "Salesperson", "Prescription ID",
                                                                             "Product Details"))
            print("=" * 155)

            for sale_entry in sales_data:
                total_income += sale_entry["total_price"]

                product_details = ""
                for product_id, quantity in sale_entry["cart_items"].items():
                    product = self.stock.getProductByID(product_id)
                    product_details += f"{product.name} ({product_id}): {quantity}\n"

                print("{:<25} | {:<15.2f} | {:<15} | {:<20} | {:<15} | {:<15}|".format(
                    sale_entry["timestamp"],
                    sale_entry["total_price"],
                    sale_entry["customerID"],
                    sale_entry["salesperson"],
                    sale_entry.get("prescriptionID", ""),
                    product_details
                ))

            print("-" * 105)
        print("{:<25} {:<15} {:<15} {:<20} {:<15}".format("Total Income:", total_income, "", "", ""))

    def prescription_statistics(self):
        """Display prescription statistics"""
        # TODO: Implement the logic to display prescription statistics
        pass

    def purchases_for_user(self):
        """Display purchases for a user"""
        user_id = input("Enter the user ID: ")

        with open(self.records_file, 'r') as sales_file:
            sales_data = json.load(sales_file)

            user_sales = [sale_entry for sale_entry in sales_data if sale_entry["customerID"] == user_id]

            if not user_sales:
                print("No purchases found for the specified user.")
                return

            print("Purchases for User:")
            print("{:<25} {:<15} {:<15} {:<20} {:<15} {:<15}".format("Timestamp", "Total Price", "Customer ID",
                                                                     "Salesperson", "Prescription ID",
                                                                     "Product Details"))
            print("=" * 105)

            for sale_entry in user_sales:
                product_details = ""
                for product_id, quantity in sale_entry["cart_items"].items():
                    product = self.stock.getProductByID(product_id)
                    product_details += f"{product.name} ({product_id}): {quantity}\n"

                print("{:<25} {:<15.2f} {:<15} {:<20} {:<15} {:<15}".format(
                    sale_entry["timestamp"],
                    sale_entry["total_price"],
                    sale_entry["customerID"],
                    sale_entry["salesperson"],
                    sale_entry.get("prescriptionID", ""),
                    product_details
                ))

            print("-" * 105)

    def sales_by_agent(self):
        """Display sales by an agent"""
        agent_name = input("Enter the agent's name: ")

        with open(self.records_file, 'r') as sales_file:
            sales_data = json.load(sales_file)

            agent_sales = [sale_entry for sale_entry in sales_data if sale_entry["salesperson"] == agent_name]

            if not agent_sales:
                print("No sales found for the specified agent.")
                return

            print("Sales by Agent:")
            print("{:<25} {:<15} {:<15} {:<20} {:<15} {:<15}".format("Timestamp", "Total Price", "Customer ID",
                                                                     "Salesperson", "Prescription ID",
                                                                     "Product Details"))
            print("=" * 105)

            for sale_entry in agent_sales:
                product_details = ""
                for product_id, quantity in sale_entry["cart_items"].items():
                    product = self.stock.getProductByID(product_id)
                    product_details += f"{product.name} ({product_id}): {quantity}\n"

                print("{:<25} {:<15.2f} {:<15} {:<20} {:<15} {:<15}".format(
                    sale_entry["timestamp"],
                    sale_entry["total_price"],
                    sale_entry["customerID"],
                    sale_entry["salesperson"],
                    sale_entry.get("prescriptionID", ""),
                    product_details
                ))

            print("-" * 105)

    def top_sales(self):
        """Display top sales"""
        # TODO: Implement the logic to display top sales
        pass

    # **CHALLENGE** (BONUS): Can you implement the menu to work as a USSD application? Implement and show your design
