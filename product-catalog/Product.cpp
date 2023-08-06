#include <iostream>
#include <string.h>
#include <chrono>
#include <random>


using namespace std;
using namespace std::chrono;



class Product{

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

    string getName(){
        //TODO Add code that return the Product Name
    }

    string getBrand(){
        //TODO Add code that return the Product Brand
    }

    string getDecrisption(){
        //TODO Add code that return the Product Description
    }

    string getDosageInstraction(){
        //TODO Add code that return the Product Dosage Instruction
    }

    string getCategory(){
        //TODO Add code that return the Product Category
    }
    
    int getQuantity(){
        //TODO Add code that return the Product Quantity
    }

    float getPrice(){
        //TODO Add code that return the Product Price
    }

    bool getRequiresPrescription(){
        //TODO Add code that return Product Requires Prescription status
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

    string promptTextField(string promptText){

        // TODO Add code to prompt user for input for any Product string field
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
    }

    float promptNumberField(string promptText){
        // TODO Add code to prompt user for input for any Product Numeric field
        // method takes text to display e.g: "Enter Product Name:"
        // it prompts a user and return user input in form of text. Text can be made by multiple words.
    }

    bool promptRequirePrescription()
    {
        // TODO Add code to prompt user for choosing if Product requires prescription.
        // User can type 1 or 0. 
        // it prompts a user and return user input in form of boolean. 
    }

    void createProduct()
    {

        // TODO Add code that calls promptTextField() method and prompt user for entering product name and update the name field.
        // TODO Add code that calls promptTextField() method and prompt user for entering product brand and update the brand field.
        // TODO Add code that calls promptTextField() method and prompt user for entering product description and update the decription field.
        // TODO Add code that calls promptTextField() method and prompt user for entering product category and update the category field.
        // TODO Add code that calls promptTextField() method and prompt user for entering product dosageInstruction and update the dosage instruction field.
        // TODO Add code that calls promptNumberField() method and prompt user for entering product quantity and update the quantity field.
        // TODO Add code that calls promptNumberField() method and prompt user for entering product price and update the price field.
        // TODO Add code that calls promptRequirePrescription() method and prompt user for entering product requires presc and update the requiresprescription field.

        // Add code to generate Unique code for product using generateUniqueCode method
       
    };

    string toJson()
    {

        string productInJson;

      // TODO Add code for converting a product to json form from the private declared attributes.
      // The Output should look like:
      //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}

        return productInJson;
    };


    
    void productFromJson(string txt)
    {
        //TODO Add code to convert a json string product to product object
        // string is in the form below
        //{"code":"tgtwdNbCnwx","name":"name 1","brand":"br 2","description":"df","dosage_instruction":"dfg","price":123.000000,"quantity":13,"category":"des","requires_prescription":1}
        // You need to extract value for each field and update private attributes declared above.

    };
};
