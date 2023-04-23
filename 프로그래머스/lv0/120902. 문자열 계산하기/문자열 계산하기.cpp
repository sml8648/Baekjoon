#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int solution(string my_string) {
    int result = 0;
    stringstream ss(my_string);  // 문자열을 읽기 위한 stringstream 객체 생성

    int num;
    ss >> num;  // 첫 번째 숫자를 읽음
    result += num;

    char op;
    while (ss >> op) {  // 연산자가 있을 때까지 반복
        ss >> num;  // 숫자를 읽음
        if (op == '+') {
            result += num;
        } else if (op == '-') {
            result -= num;
        }
    }

    return result;
}