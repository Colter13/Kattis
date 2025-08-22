#include <iostream>

using namespace std;

int main() {
    
    string s;
    string s2 = "";
    
    cin >> s;
    
    for (int i=0; i < s.length(); i++) {
        if (s[i] == '<') {
            s2 = s2.substr(0, s2.length()-1);
        } else {
            s2 += s[i];
        }
    }

    cout << s2 << endl;
    
    
    return 0;
}