#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, string control) {
    int answer = n;
    
    for (auto chr : control)
    {
        if(chr == 'w')
        {
            answer += 1;
        }
        else if(chr == 's')
        {
            answer -= 1;
        }
        else if(chr == 'd')
        {
            answer += 10;
        }
        else if(chr == 'a')
        {
            answer -= 10;
        }
    }
    return answer;
}