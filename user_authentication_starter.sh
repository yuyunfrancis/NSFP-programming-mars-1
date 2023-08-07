#!/bin/bash
## to be updated to match your settings
# PROJECT_HOME="linux"
LOCAL_DATA_STORAGE="data"
credentials_file="$LOCAL_DATA_STORAGE/credentials.txt"
logged_in_user=""

creata_data_folder(){
    if [ ! -d "$LOCAL_DATA_STORAGE" ]; then
        mkdir "$LOCAL_DATA_STORAGE"
    fi

    if [ ! -f "$credentials_file" ]; then
        touch "$credentials_file"
    fi
}

#generate salt
generate_salt() {
   openssl rand -hex 8
   return 0
}

## function for hashing
hash_password() {
    password=$1
    salt=$2
    echo -n "${password}${salt}" | sha256sum | awk '{print $1}'
}

check_existing_username(){
    local email="$1"
    if grep -q ":$email:" "$credentials_file"; then
        return 0
    else
        return 1
    fi

}


##check email validity
is_valid_email(){
    local email="$1"
    if [[ "$email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        return 0
    else
        return 1
    fi
}

## function to add new credentials to the file
# Function to add new credentials to the file
register_credentials() {
    creata_data_folder
    check_user_is_logged_in

    echo "===== User Registration ====="

    read -p 'Enter your username: ' username
    read -p "Enter your email: " email

    if ! is_valid_email "$email" || check_existing_username "$email"; then
        echo -e "\nInvalid email or user with username '$username' or email '$email' already exists. Registration failed."
    else
        stty -echo
        read -p "Enter your password: " password
        stty echo
        echo
        stty -echo
        read -p "Re-enter your password: " password_reentered
        stty echo
        echo

        if [ "$password" != "$password_reentered" ]; then
            echo "Passwords do not match. Registration failed."
        else
            salt=$(generate_salt)
            hashed_password=$(hash_password "$password" "$salt")

           if [ "$role" = "admin" ]; then
           echo -e "\nSelect the role for the new user: "
           echo "1. admin"
           echo "2. salesperson"
           echo "3. normal"

           read -p "Enter the role number: " role_number

           case $role_number in
               1)
                   role="admin"
                   ;;
               2)
                   role="salesperson"
                   ;;
               *)
                   role="normal"
                   ;;
           esac
       else
           role="normal"
       fi

            echo "$username:$email:$hashed_password:$role:$salt:0" >> "$credentials_file"
            echo -e "\nRegistration successful. You can now login."
        fi
    fi
}


#Verify username already exists
check_username(){
    local username="$1"
    if [ -f "$credentials_file" ] && grep -q "^$username:" "$credentials_file"; then
        return 0
    else
        return 1
    fi
}



# Function to verify credentials
verify_credentials() {
    local username="$1"
    local password="$2"

    if check_username "$username"; then
        stored_credentials=$(grep "^$username:" "$credentials_file")
        stored_password=$(echo "$stored_credentials" | cut -d ":" -f 3)
        stored_salt=$(echo "$stored_credentials" | cut -d ":" -f 5)
        status=$(echo "$stored_credentials" | cut -d ":" -f 6)

        if [ "$status" = "1" ]; then
            echo -e "\nUser '$username' is already logged in."
            return 2
        fi

        hashed_password_input=$(hash_password "$password" "$stored_salt")

        if [ "$hashed_password_input" = "$stored_password" ]; then
          awk -v usr="$username" 'BEGIN { FS = ":"; OFS = ":" } $1 == usr { $6 = 1 } 1' "$credentials_file" > "$credentials_file.tmp"
            mv "$credentials_file.tmp" "$credentials_file"
            return 0 # Credentials are valid
        else
            return 1 # Invalid credentials
        fi
    else
        return 1 # Invalid credentials
    fi
}

get_user_role() {
    local username="$1"
    if [ -f "$credentials_file" ]; then
        user_data=$(grep "^$username:" "$credentials_file")
        if [ -n "$user_data" ]; then
            echo "$user_data" | cut -d ":" -f 4
        fi
    fi
}

check_user_is_logged_in() {
    if [ -f .logged_in ]; then
        logged_in_user=$(cat .logged_in)
        stored_credentials=$(grep "^$logged_in_user:" "$credentials_file")
        role=$(echo "$stored_credentials" | cut -d ":" -f 4)
    else
        role="normal"
    fi
}

# Function to display menu for admin
admin_menu() {
    echo -e "Welcome, Admin!"
    echo "1. Add a user"
    echo "2. View all users"
    echo "3. Delete a user"
    echo "4. Logout"
}

# Function to handle admin's options
admin_options() {
    local choice
    while true; do
        admin_menu
        read -p "Enter your choice: " choice

        case $choice in
            1)
                register_credentials
                ;;
            2)
                display_all_users
                ;;
            3)
                delete_user
                ;;
            4)
                log_out
                return
                ;;
            *)
                echo "Invalid choice. Try again"
                ;;
        esac
    done
}


# Function to display menu for normal user
normal_user_menu() {
    echo -e "Welcome, Normal User!"
    echo "1. Buy drugs"
    echo "2. Logout"
}

# Function to handle normal user's options
normal_user_options() {
    local choice
    while true; do
        normal_user_menu
        read -p "Enter your choice: " choice

        case $choice in
            1)
                echo "Buy Product"
                ;;
            2)
                log_out
                return
                ;;
            *)
                echo "Invalid choice. Try again"
                ;;
        esac
    done
}

# Function to display menu for salesperson
salesperson_menu() {
    echo -e "Welcome, to your sales dashboard!"
    echo "1. Add Product"
    echo "2. Search Product By Name"
    echo "3. Search Product By Brand"
    echo "4. Search Product By Category"
    echo "5. Logout"
}

# Function to handle salesperson's options
salesperson_options() {
    local choice
    while true; do
        salesperson_menu
        read -p "Enter your choice: " choice

        case $choice in
            1)
                echo "Add Product"
                ;;
            2)
                echo "View Product"
                ;;
            3)
                echo "Delete Product"
                ;;
            4)
                log_out
                return
                ;;
            *)
                echo "Invalid choice. Try again"
                ;;
        esac
    done
}

# Function to prompt for credentials
get_credentials() {
    creata_data_folder
    echo "===== Login ====="
    
    read -p "Enter your username: " username
    stty -echo
    read -p "Enter your password: " password
    stty echo
    echo

    if verify_credentials "$username" "$password"; then
        echo -e "\nLogin successful. Welcome, $username!"
        echo "$username" > .logged_in

        user_role=$(get_user_role "$username")
        case $user_role in
            "admin")
                admin_options
                ;;
            "salesperson")
                salesperson_options
                ;;
            "normal")
                normal_user_options
                ;;
            *)
                echo "Unknown user role. Logging out..."
                log_out
                ;;
        esac
    else
        echo -e "\nLogin failed. Invalid credentials."
        rm -f .logged_in
    fi
}

delete_user() {
    check_user_is_logged_in

    if [ "$role" != "admin" ]; then
        echo "Only admin can delete users."
        return
    fi

    read -p "Enter the username of the user to delete: " username
    if [ -z "$username" ]; then
        echo "Username cannot be empty."
        return
    fi

    if grep -q "^$username:" "$credentials_file"; then
        sed -i "/^$username:/d" "$credentials_file"
        echo "User '$username' deleted successfully."
    else
        echo "User '$username' not found."
    fi
}


# Function to display all users for an admin
display_all_users() {
    check_user_is_logged_in

    if [ "$role" != "admin" ]; then
        echo "Only admin can view users."
        return
    fi

    echo "==== All Registered Users ===="
    cat "$credentials_file"
}

log_out() {
    echo -e "\nLogging out..."

    if [ -f .logged_in ]; then
        logged_in_user=$(cat .logged_in)
        awk -v usr="$logged_in_user" 'BEGIN { FS = ":"; OFS = ":" } $1 == usr { $6 = 0 } 1' "$credentials_file" > "$credentials_file.tmp"
        mv "$credentials_file.tmp" "$credentials_file"

        rm -f .logged_in
        echo "Logged out successfully."
    else
        echo "No user is currently logged in."
    fi
}


ctrl_c_handler() {
    if [ -f .logged_in ]; then
        logged_in_user=$(cat .logged_in)
        stored_credentials=$(grep "^$logged_in_user:" "$credentials_file")
        status=$(echo "$stored_credentials" | cut -d ":" -f 6)

        if [ "$status" = "1" ]; then
            log_out
            exit 130
        else
            echo "User '$logged_in_user' is already logged out."
            exit 130
        fi
    else
        echo -e "\nNo user is currently logged in."
        exit 130
    fi
}

trap ctrl_c_handler SIGINT


## Create the menu for the application
# at the start, we need an option to login, self-register (role defaults to normal)
# and exit the application.

# After the user is logged in, display a menu for logging out.
# if the user is also an admin, add an option to create an account using the 
# provided functions.

# Main script execution starts here
while true; do
    echo -e "Welcome to the authentication system."
    echo "\nselect an option"
    echo "1. Login"
    echo "2. Register"
    echo "3. Logout"
    echo "4. close the program"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            get_credentials
            ;;
        2)
            if [ -f .logged_in ]; then
            logged_in_user=$(cat .logged_in)
            stored_credentials=$(grep "^$logged_in_user:" "$credentials_file")
            role=$(echo "$stored_credentials" | cut -d ":" -f 4)
            
                if [ "$role" = "admin" ]; then
                    register_credentials
                else
                    echo "Only admin can create users."
                fi
            else
            role="normal"
            register_credentials
            fi
            ;;
        3)
            log_out
            ;;
        4)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid choice. Try again"
            ;;
    esac


done


#### BONUS
#1. Implement a function to delete an account from the file