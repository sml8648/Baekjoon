#include <string>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int solution(string n_str) {
    int answer = 0;
    
    
    
    for(int i = 0; i < n_str.size(); i++)
    {
        //answer += ((int)n_str[i] - 48)*(10**((int)n_str.size() -1));
        answer += ((int)n_str[i]-48)*pow(10,(int)n_str.size() - (i+1));
    }
    return answer;
}