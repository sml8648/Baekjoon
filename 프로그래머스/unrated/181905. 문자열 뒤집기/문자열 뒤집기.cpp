#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(string my_string, int s, int e) {
    string answer = "";
    
    string first = "";
    for(int i = 0;i<s;i++)
    {
        first += my_string[i];
    }
    
    string second = "";
    for(int i = s;i<=e;i++)
    {
        second += my_string[i];
    }
    
    string third = "";
    for(int i = (e+1) ; i < my_string.size();i++)
    {
        third += my_string[i];
    }
    
    reverse(second.begin(), second.end());
    
    answer = first + second + third;
    
    return answer;
}