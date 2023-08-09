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
        return name;
    }

    string getBrand()
    {
        return brand;
    }

    string getDecrisption()
    {
        return description;
    }

    string getDosageInstraction()
    {
        return dosageInstruction;
    }

    string getCategory()
    {
        return category;
    }

    string getCode()
    {
        return code;
    }

    int getQuantity()
    {
        return quantity;
    }

    float getPrice()
    {
        return price;
    }

    bool getRequiresPrescription()
    {
        return requires_prescription;
    }

    void setPrice(float p)
    {
        price = p;
    }

    void setQuantity(int q)
    {
        quantity = q;
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

        string name;
        cout << promptText;
        getline(cin, name);
        return name;
    }

    float promptNumberField(string promptText)
    {
        float value;
        cout << promptText;
        cin >> value;
        return value;
    }

    bool promptRequirePrescription()
    {
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

        name = promptTextField("Enter Name for the product: ");

        brand = promptTextField("Enter Brand for the product: ");

        description = promptTextField("Enter Description for the product: ");

        category = promptTextField("Enter Category for the product: ");

        dosageInstruction = promptTextField("Enter Dosage Instruction for the product: ");

        quantity = promptNumberField("Enter Quantity for the product: ");

        price = promptNumberField("Enter Price for the product: ");

        requires_prescription = promptRequirePrescription();

        code = generateUniqueCode();
    };

    string toJson()
    {

        string productInJson =
            "{\"code\":\"" + code +
            "\",\"name\":\"" + name +
            "\",\"brand\":\"" + brand +
            "\",\"description\":\"" + description +
            "\",\"dosage_instruction\":\"" + dosageInstruction +
            "\",\"price\":" + std::to_string(price) +
            ",\"quantity\":" + std::to_string(quantity) +
            ",\"category\":\"" + category +
            "\",\"requires_prescription\":" + std::to_string(requires_prescription) + "}";

        return productInJson;
    };

    void productFromJson(string txt)
    {

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
            }
            else { // If the value is a number
                // Here the value_start_idx will be the first number of the value column
                value_end_idx = txt.find(",", value_start_idx);
                if (value_end_idx == string::npos)
                { // If no matches found meaning we are at the end of the json string
                    value_end_idx = txt.find("}", value_start_idx);
                }
            }
            string value = txt.substr(value_start_idx, value_end_idx - value_start_idx);
            if (key == "code")
            {
                code = value;
            }
            else if (key == "name")
            {
                name = value;
            }
            else if (key == "brand")
            {
                brand = value;
            }
            else if (key == "description")
            {
                description = value;
            }
            else if (key == "dosage_instruction")
            {
                dosageInstruction = value;
            }
            else if (key == "price")
            {
                price = stof(value);
            }
            else if (key == "quantity")
            {
                quantity = stoi(value);
            }
            else if (key == "category")
            {
                category = value;
            }
            else if (key == "requires_prescription")
            {
                requires_prescription = stoi(value);
            }

            idx = value_end_idx + 1;
        }
    };
};
