#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string my_string, string target) {
    int answer = 0;
    
    int result = my_string.find(target);
    
    if(result >= 0)
    {
        answer = 1;
    }
    
    return answer;
}