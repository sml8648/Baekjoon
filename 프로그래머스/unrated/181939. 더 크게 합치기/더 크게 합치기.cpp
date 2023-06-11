#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int solution(int a, int b) {
    string str_ab = to_string(a) + to_string(b);
    string str_ba = to_string(b) + to_string(a);
    
    if (str_ab >= str_ba) {
        return stoi(str_ab);
    } else {
        return stoi(str_ba);
    }
}
