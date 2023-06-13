#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string solution(string myString) {
    for (char& c : myString) {
        if (c == 'a' || c == 'A') {
            c = 'A';
        } else if (isupper(c)) {
            c = tolower(c);
        }
    }
    return myString;
}