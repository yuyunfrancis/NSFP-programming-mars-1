#!/usr/bin/python3
import os

from order_management import (
    UserManagement,
    Stock,
    Cart,
    Wrapper,
    Menu,
    BookRecords
)


def show_salesperson_menu(menu):
    while True:
        print("******************************************")
        print("Order Management and Analytics Menu:")
        print("[Loc:.")
        print("******************************************")
        print("1. Order Management")
        print("2. Get Analytics")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu.run_order_management_menu()
        elif choice == '2':
            menu.run_analytics_menu()
        elif choice == '3':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue


def show_admin_menu(menu):
    while True:
        print("Admin Menu:")
        print("1. Add product to stock")
        print("2. View stock")
        print("3. View sales records")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            menu.add_product_to_stock()
        elif choice == '2':
            menu.view_stock()
        elif choice == '3':
            menu.view_sales_records()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def show_normal_menu(menu):
    while True:
        print("Normal Menu:")
        print("1. Add product to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu.add_to_cart()
        elif choice == '2':
            menu.view_cart()
        elif choice == '3':
            menu.checkout()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':

    # files path declaration
    data_folder = 'data'
    credentials_file = os.path.join(data_folder, 'credentials.txt')
    stock_file = os.path.join(data_folder, 'products.json')
    sales_file = os.path.join(data_folder, 'sales.json')
    prescription_file = os.path.join(data_folder, 'prescriptions.json')
    status_file = os.path.join(data_folder, '.logged_in')

    # load the user management file
    profiles = UserManagement.load(credentials_file)

    # Check if a user is logged in
    logged_in_user = profiles.get_logged_in_user()
    if logged_in_user is None:
        print("No user is logged in. Exiting.")
        exit()

    # Create an instance of the menu
    stock = Stock.load(stock_file)
    cart = Cart(stock=stock)
    wrap = Wrapper(stock, logged_in_user.username)
    books = BookRecords.load(sales_file)
    menu = Menu(stock, profiles, logged_in_user, sales_file, prescription_file, stock_file)

    # Show the appropriate menu based on user's role
    if logged_in_user.role == 'salesperson':
        show_salesperson_menu(menu)
    elif logged_in_user.role == 'admin':
        show_admin_menu(menu)
    elif logged_in_user.role == 'normal':
        show_normal_menu(menu)
    else:
        print("Invalid role. Exiting.")
