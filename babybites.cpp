#include <iostream>

using namespace std;

int main()
{
    int n;
    string m;
    bool flag = false;
    cin >> n;
    
    for (int i=0; i<n; i++) {
        cin >> m;
        if (m != "mumble") {
            if (i+1 != stoi(m)) {
                flag = true;
            }
        }
    }
        
    if (flag == false) {
        cout << "makes sense" << endl;
    } else {
        cout << "something is fishy" << endl;
    }
    
    return 0;
}