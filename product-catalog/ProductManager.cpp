#include "SearchProduct.cpp"

class ProductManager
{
private:
    Product prod;
public:
    int getMenu(){

        int choice = 0;
        cout << "Menu: " << endl;
        cout << "1.\tAdd Product" << endl;
        cout << "2.\tSearch Products by Name" << endl;
        cout << "3.\tSearch Products by Brand" << endl;
        cout << "4.\tSearch Products by Category" << endl;
        cout << "5.\tUpdate Product" << endl;
        cout << "6.\tDelete Product" << endl;
        cout << "7.\tExit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        cout << endl;
        if (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5 && choice != 6 && choice != 7){
            cout << "Wrong Input!!! Please enter a correct value";
        }
        return choice;
    }

    void addProduct(){
        cin.ignore();
        prod.createProduct();
        FileHandler file;
        file.saveToJsonFile(prod);
        cout<<"Product added successfully " <<endl <<endl;
    }

    void updateProduct(string code){
        FileHandler file;
        vector<Product> pList;
        int idx;
        Product updatedProduct;
        pList = file.readJsonFile();
        vector<Product>::iterator it = pList.begin();
        for (it; it < pList.end(); ++it) {
            if (it->getCode() == code){
                updatedProduct = *it;
                idx = it - pList.begin();
                break;
            }
        }
        float price = updatedProduct.promptNumberField("Enter the updated price of the product: "); 
        int quantity = updatedProduct.promptNumberField("Enter the updated quantity of the product: "); 
        updatedProduct.setPrice(price);
        updatedProduct.setQuantity(quantity);
        pList[idx] = updatedProduct;
        file.saveListToJsonFile(pList);
        cout << "Product updated successfully " << endl;
    }

    void deleteProduct(string code){
        FileHandler file;
        vector<Product> pList;
        int idx;
        pList = file.readJsonFile();
        vector<Product>::iterator it = pList.begin();
        for (it; it < pList.end(); ++it) {
            if(it->getCode() == code){
                idx = it - pList.begin();
                break;
            }
        }
        pList.erase(pList.begin() + idx);
        file.saveListToJsonFile(pList);
        cout << "Product deleted successfully " << endl;

    }
    
};

int main()
{

    ProductManager pManager;
    int choice = 0;
    choice = pManager.getMenu();
   while (choice != 7){
        if (choice == 1){
            pManager.addProduct();
        } else if (choice == 2){
            SearchProduct sProduct;
            vector<Product> searchList;
            string name;
            cout << "Enter the name of the product you want to search: ";
            cin.ignore();
            getline(cin, name);
            searchList = sProduct.searchByName(name);
            sProduct.showSearchResult(searchList, name);
        } else if (choice == 3){
            SearchProduct sProduct;
            vector<Product> searchList;
            string brand;
            cout << "Enter the brand of the product you want to search: ";
            cin.ignore();
            getline(cin, brand);
            searchList = sProduct.searchByBrand(brand);
            sProduct.showSearchResult(searchList, brand);
        } else if (choice == 4){
            SearchProduct sProduct;
            vector<Product> searchList;
            string category;
            cout << "Enter the category of the product you want to search: ";
            cin.ignore();
            getline(cin, category);
            searchList = sProduct.searchByCategory(category);
            sProduct.showSearchResult(searchList, category);

        }else if (choice == 5) {
            string code;
            cout << "Enter the code of the product to update: ";
            cin.ignore();
            getline(cin, code);
            pManager.updateProduct(code);
        } else if (choice == 6) {
            string code;
            cout << "Enter the code of the product to delete: ";
            cin.ignore();
            getline(cin, code);
            pManager.deleteProduct(code);
        }
        choice = pManager.getMenu();
   }
    cout << "Exiting Program..." << endl;

    return 0;
}


