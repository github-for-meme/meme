#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s = "https://www.multisoft.se/";
    string a = "1112031584";
    for (int i = 1; i < (int)a.length(); i++) {
        if (a[i] % 2 == a[i-1] % 2) {
            char n = a[i] > a[i - 1] ? a[i] : a[i - 1];
            s += n;
        }
    };
    s += "/";
    cout << s << endl;

    return 0;
}
