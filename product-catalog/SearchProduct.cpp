#include "FileHandler.cpp"

class SearchProduct
{
private:
    string filename;

public:
    string searchText;
    FileHandler fHandler;

    string to_lowercase(const string& text) {
        string lowercase_text;
        for (char c : text) {
            lowercase_text += tolower(c);
        }
        return lowercase_text;
    }

    vector<Product> searchByName(string name){

        // TODO
        //Add code to search by name. Searching is not case sensitive it means 
        //for input like: "name" products with names like "Name 1", "Product name" needs to included in the found results.
        vector<Product> pList = fHandler.readJsonFile();
        vector<Product> searchList;
        vector<Product>::iterator it = pList.begin();
        for (it; it < pList.end(); ++it) {
            string prodName = to_lowercase(it->getName());
            if (prodName.find(name) != string::npos) {
                if(prodName == ""){
                    continue;
                }
                searchList.push_back(*it);
            }
        }
        return searchList;
    
    };

    vector<Product> searchByCategory(string categ){

        // TODO
        //Add code to search by category. Searching is not case sensitive it means 
        //for input like: "categ" products with category like "category 1", "Product category" needs to included in the found results.

        vector<Product> pList = fHandler.readJsonFile();
        vector<Product> searchList;
        vector<Product>::iterator it = pList.begin();
        for (it; it < pList.end(); ++it) {
            string prodName = to_lowercase(it->getCategory());
            if (prodName.find(categ) != string::npos) {
                if(prodName == ""){
                    continue;
                }
                searchList.push_back(*it);
            }
        }
        return searchList;

    };

    vector<Product> searchByBrand(string brand){
      // TODO
        //Add code to search by brand. Searching is not case sensitive it means 
        //for input like: "br" products with names like "Brand 1", "brand name" needs to included in the found results.

        vector<Product> pList = fHandler.readJsonFile();
        vector<Product> searchList;
        vector<Product>::iterator it = pList.begin();
        for (it; it < pList.end(); ++it) {
            string prodName = to_lowercase(it->getBrand());
            if (prodName.find(brand) != string::npos) {
                if(prodName == ""){
                    continue;
                }
                searchList.push_back(*it);
            }
        }
        return searchList;
    };

    void showSearchResult(vector<Product> plist, string sTxt)
    {
        // TODO
        //Add code to display Search results
        cout << "Searching Text: " << sTxt << endl;
        vector<Product>::iterator it = plist.begin();
        for(it; it < plist.end(); ++it) {
            cout << it->toJson() << endl;
        }

    }
};