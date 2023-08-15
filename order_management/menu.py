from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription
from .cart import Cart

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
                 prescriptions_file: str, stock_file: str) -> None:
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

    def run(self):
        """Run the menu and process user input"""
        while True:
            print("\nMain Menu:")
            print("1. Order management")
            print("2. Analytics")
            print("3. Exit")

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
            else:
                print(MSG_WRONG_INPUT)

            # Add this condition to return to the main menu only if explicitly chosen
            if choice != '4':
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
            else:
                print(MSG_WRONG_INPUT)

    def add_to_cart(self):
        """Add a product to the cart"""
        # TODO: Implement the logic to add a product to the cart
        print("Available Products:")
        for product in self.stock.products:
            print(f"ID: {product.code}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

        # Ask the user to enter the product ID and quantity
        product_id = str(input("Enter the product ID to add to the cart: "))
        quantity = int(input("Enter the quantity to add: "))
        self.cart.add(product_id, quantity)
        # pass

    def remove_from_cart(self):
        """Remove a product from the cart"""
        # TODO: Implement the logic to remove a product from the cart
        pass

    def clear_cart(self):
        """Clear the cart"""
        # TODO: Implement the logic to clear the cart
        pass

    def checkout(self):
        """Checkout the cart"""
        # TODO: Implement the logic to checkout the cart
        pass

    def total_income(self):
        """Calculate the total income from purchases"""
        # TODO: Implement the logic to calculate total income
        pass

    def prescription_statistics(self):
        """Display prescription statistics"""
        # TODO: Implement the logic to display prescription statistics
        pass

    def purchases_for_user(self):
        """Display purchases for a user"""
        # TODO: Implement the logic to display purchases for a user
        pass

    def sales_by_agent(self):
        """Display sales by an agent"""
        # TODO: Implement the logic to display sales by an agent
        pass

    def top_sales(self):
        """Display top sales"""
        # TODO: Implement the logic to display top sales
        pass

    # **CHALLENGE** (BONUS): Can you implement the menu to work as a USSD application? Implement and show your design