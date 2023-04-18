#include <iostream>
#include <sstream>
#include <string>
#include <stack>

using namespace std;

int solution(string s) {
    int answer = 0;
    stack<int> nums;
    stringstream ss(s);
    string token;
    while (getline(ss, token, ' ')) {
        if (token == "Z") {
            int prev = nums.top();
            nums.pop();
            answer -= prev;
        } else {
            int num = stoi(token);
            nums.push(num);
            answer += num;
        }
    }
    return answer;
}
