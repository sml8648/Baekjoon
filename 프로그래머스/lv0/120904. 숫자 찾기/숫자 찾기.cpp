#include <string>
#include <iostream>

using namespace std;

int solution(int num, int k) {
    string num_str = to_string(num);
    int len = num_str.length();

    for (int i = 0; i < len; i++) {
        if (num_str[i] - '0' == k) {
            return i + 1;
        }
    }
    return -1;
}
