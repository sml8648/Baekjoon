#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(vector<string> str_list, string ex) {
    string answer = "";
    
    for(auto str: str_list)
    {
        if(str.find(ex) == std::string::npos)
        {
            for(auto chr:str)
            {
                answer += chr;
            }
        }
    }
    return answer;
}