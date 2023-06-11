#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    
    string ad = "ad";
    
    for(auto str:strArr)
    {
        if(str.find(ad) == std::string::npos)
        {
            answer.push_back(str);
        }
    }
    return answer;
}