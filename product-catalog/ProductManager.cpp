#include "SearchProduct.cpp"

class ProductManager
{
private:
    Product prod;
public:
    int getMenu(){

        // TODO Add code to display Menu
        // Menu should have 
        // Add Product
        //Search Product By Name
        //Search Product By Category
        //Search Product By Brand
        // Update Product
        // Delete Product
        int choice = 0;
        cout << "Menu: " << endl;
        cout << "1.\tAdd Product" << endl;
        cout << "2.\tSearch Products by Name" << endl;
        cout << "3.\tSearch Products by Brand" << endl;
        cout << "4.\tSearch Products by Category" << endl;
        cout << "5.\tExit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        cout << endl;
        if (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5){
            cout << "Wrong Input!!! Please enter a correct value";
        }
    }

    void addProduct(){
        // TODO add code to add product and 
        // store the product to products.json file by using Product class and FileHandler class
        prod.createProduct();
        FileHandler file;
        file.saveToJsonFile(prod);
        cout<<"Product successfully added "<<endl<<endl;;
    }

    // TODO Add code for Updating a product
    void updateProduct(){

    }

    // TODO Add code for deleting a product
    
};

int main()
{

    // ADD Code for displaying a welcome Menu
    // and handle all required logic to add, search, update, and delete product
    ProductManager pManager;
    int choice = 0;
    choice = pManager.getMenu();
   while (choice != 5){
        if (choice == 1){
            pManager.addProduct();
        } else if (choice == 2){
            SearchProduct sProduct;
            string name;
            cout << "Enter the name of the product you want to search: ";
            cin >> name;
            sProduct.searchByName(name);
        } else if (choice == 3){
            SearchProduct sProduct;
            string brand;
            cout << "Enter the brand of the product you want to search: ";
            cin >> brand;
            sProduct.searchByBrand(brand);
        } else if (choice == 4){
            SearchProduct sProduct;
            string category;
            cout << "Enter the category of the product you want to search: ";
            cin >> category;
            sProduct.searchByCategory(category);
        }
        choice = pManager.getMenu();
   }
    cout << "Exiting Program..." << endl;

    return 0;
}


