#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> solution(string myStr) {
    vector<string> result;
    string temp;
    bool delimiterFound = false;

    for (char c : myStr) {
        if (c == 'a' || c == 'b' || c == 'c') {
            if (!temp.empty()) {
                result.push_back(temp);
                temp.clear();
            }
            delimiterFound = true;
        } else {
            temp += c;
        }
    }

    if (!temp.empty()) {
        result.push_back(temp);
    }

    if (result.empty()) {
        result.push_back("EMPTY");
    }

    return result;
}