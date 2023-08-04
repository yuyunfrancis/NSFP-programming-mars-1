#!/bin/bash
## to be updated to match your settings
# PROJECT_HOME="linux"
LOCAL_DATA_STORAGE="data"
credentials_file="$LOCAL_DATA_STORAGE/credentials.txt"

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
   salt=$(openssl rand -hex 8)
   echo "$salt"
}

## function for hashing
hash_password() {
    local password="$1"
    local salt="$2"
    hash_password=$(echo -n "$password$salt" | sha256sum | awk '{print $1}' )
    echo "$hash_password"
}

check_existing_username(){
    local email="$1"
    if grep -q "|$email|" "$credentials_file"; then
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
register_credentials() {
    creata_data_folder

    echo "===== User Registration ====="

    read -p 'Enter your username: ' username
    read -p "Enter your email: " email

    if ! is_valid_email "$email" || check_existing_username "$email"; then
        echo -e "\nInvalid email or user with username '$username' or email '$email' already exists. Regisration failed."

    else
       stty -echo
       read -p "Enter your password: " password
       stty -echo
    
    salt=$(generate_salt)

    hash_password=$(hash_password "$password" "$salt")

    echo -e "\nSelect your role: "
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
        3)
            role="normal"
            ;;
        *)
        echo "Invalid role. Assuming 'normal' role."
        role="normal"
        ;;
    
    esac

    echo "$username|$email|$hash_password|$role|$salt" >> "$credentials_file"
    echo -e "\nRegistration successful"

    fi
}

#Verify username already exists
check_username(){
    local username="$1"
    if grep -q "|$username|" "$credentials_file"; then
        return 0
    else
        return 1
    fi
}

# Function to verify credentials
verify_credentials() {
    local username="$1"
    local password="$2"
}

# Function to prompt for credentials
get_credentials() {
    creata_data_folder

    read -p "Enter your username: " username
    stty -echo
    read -p "Enter your password: " password
    stty echo
    echo 

    if verify_credentials "$username" "$password"; then
        echo -e "\nLogin successful. Welcome, $username!"
    else
        echo -e "\nLogin failed. Invalid credentials."
    fi
}

logout() {
    echo "Log out..."
    #TODO: check that the .logged_in file is not empty
    # if the file exists and is not empty, read its content to retrieve the username
    # of the currently logged in user

    # then delete the existing .logged_in file and update the credentials file by changing the last field to 0
}

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
            register_credentials
            ;;
        3)
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