#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> names) {
    vector<string> answer;
    
    vector<string> tmp;
    
    for(int i = 0; i < names.size();i++)
    {
        if(i%5 == 0)
        {
            answer.push_back(names[i]);
        }
    }
    
    return answer;
}