#include <iostream>
#include <string.h>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

class Product
{

private:
    int quantity;
    string name;
    string brand;
    string description;
    string code;
    float price;
    string dosageInstruction;
    string category;
    bool requires_prescription;

public:
    string getName()
    {
        // TODO Add code that return the Product Name
        return name;
    }

    string getBrand()
    {
        // TODO Add code that return the Product Brand
        return brand;
    }

    string getDecrisption()
    {
        // TODO Add code that return the Product Description
        return description;
    }

    string getDosageInstraction()
    {
        // TODO Add code that return the Product Dosage Instruction
        return dosageInstruction;
    }

    string getCategory()
    {
        // TODO Add code that return the Product Category
        return category;
    }

    int getQuantity()
    {
        // TODO Add code that return the Product Quantity
        return quantity;
    }

    float getPrice()
    {
        // TODO Add code that return the Product Price
        return price;
    }

    bool getRequiresPrescription()
    {
        // TODO Add code that return Product Requires Prescription status
        return requires_prescription;
    }

    string generateUniqueCode()
    {
        string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        string uniqueCode = "";
        auto now = system_clock::now();
        auto millis = duration_cast<milliseconds>(now.time_since_epoch());
        mt19937 generator(millis.count());
        uniform_int_distribution<int> distribution(0, 100000);

        // generate 10 characters long unique string

        for (int i = 0; i <= 10; i++)
        {
            int random_index = distribution(generator) % characters.length();
            uniqueCode += characters[random_index];
        }

        return uniqueCode;
    };

    string promptTextField(string promptText)
    {

        // TODO Add code to prompt user for input for any Product string field
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        string name;
        cout << promptText;
        cin.ignore();
        getline(cin, name);
        return name;
    }

    float promptNumberField(string promptText)
    {
        // TODO Add code to prompt user for input for any Product Numeric field
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
        float value;
        cout << promptText;
        cin >> value;
        return value;
    }

    bool promptRequirePrescription()
    {
        // TODO Add code to prompt user for choosing if Product requires prescription.
        // User can type 1 or 0.
        // it prompts a user and return user input in form of boolean.
        int value;
        cout << "Does this product require prescription (1 for yes, 0 for no): " << endl;
        cin >> value;
        if (value == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    void createProduct()
    {

        // TODO Add code that calls promptTextField() method and prompt user for entering product name and update the name field.
        name = promptTextField("Enter Name for the product: ");
        // TODO Add code that calls promptTextField() method and prompt user for entering product brand and update the brand field.
        brand = promptTextField("Enter Brand for the product: ");
        // TODO Add code that calls promptTextField() method and prompt user for entering product description and update the decription field.
        description = promptTextField("Enter Description for the product: ");
        // TODO Add code that calls promptTextField() method and prompt user for entering product category and update the category field.
        category = promptTextField("Enter Category for the product: ");
        // TODO Add code that calls promptTextField() method and prompt user for entering product dosageInstruction and update the dosage instruction field.
        dosageInstruction = promptTextField("Enter Dosage Instruction for the product: ");
        // TODO Add code that calls promptNumberField() method and prompt user for entering product quantity and update the quantity field.
        quantity = promptNumberField("Enter Quantity for the product: ");
        // TODO Add code that calls promptNumberField() method and prompt user for entering product price and update the price field.
        price = promptNumberField("Enter Price for the product: ");
        // TODO Add code that calls promptRequirePrescription() method and prompt user for entering product requires presc and update the requiresprescription field.
        requires_prescription = promptRequirePrescription();
        // Add code to generate Unique code for product using generateUniqueCode method
        code = generateUniqueCode();
    };

    string toJson()
    {

        string productInJson;

        // TODO Add code for converting a product to json form from the private declared attributes.
        // The Output should look like:
        //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}
        productInJson = "{\"code\":" + code + ",\"name\":" + name + ",\"brand\":" + brand + ",\"description\":" + description + ",\"dosage_instruction\":" + dosageInstruction + ",\"price\":" + to_string(price) + ",\"quantity\":" + to_string(quantity) + ",\"category\":" + category + ",\"requires_prescription\":" + to_string(requires_prescription) + " }";

        return productInJson;
    };

    void productFromJson(string txt)
    {
        
        // TODO Add code to convert a json string product to product object
        //  string is in the form below
        //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}
        //  You need to extract value for each field and update private attributes declared above.
        
        int idx = 0;
        while (idx < txt.length())
        {
            //    int idx = 0;
            int key_start_idx = txt.find('"', idx);
            int key_end_idx = txt.find('"', key_start_idx + 1);
            string key = txt.substr(key_start_idx + 1, key_end_idx - key_start_idx - 1);
            int value_start_idx = txt.find(":", key_end_idx) + 1; // Index of the first quote after the colon
            int value_end_idx;
            if (txt[value_start_idx] == '"') { // If the value is a string
                value_start_idx += 1;
                value_end_idx = txt.find('"', value_start_idx + 1);
            } else { // If the value is a number
                // Here the value_start_idx will be the first number of the value column
                value_end_idx = txt.find(",", value_start_idx);
                if (value_end_idx == -1) { // If no matches found meaning we are at the end of the json string
                    value_end_idx = txt.find("}", value_start_idx);
                }
            }
            string value = txt.substr(value_start_idx, value_end_idx - value_start_idx);
            if ( key == "code") {
                code = value;
            } else if ( key == "name") {
                name = value;
            } else if ( key == "brand") {
                brand = value;
            } else if ( key == "description") {
                description = value;
            } else if ( key == "dosage_instruction") {
                dosageInstruction = value;
            } else if ( key == "price") {
                price = stof(value);
            } else if ( key == "quantity") {
                quantity = stoi(value);
            } else if ( key == "category") {
                category = value;
            } else if ( key == "requires_prescription") {
                requires_prescription = stoi(value);
            }
            // std::cout << value << endl;

            idx = value_end_idx + 1;
        }
    };
};
