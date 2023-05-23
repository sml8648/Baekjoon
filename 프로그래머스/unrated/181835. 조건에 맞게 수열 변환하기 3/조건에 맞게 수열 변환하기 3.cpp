#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    
    if(k%2 == 1)
    {
        for(int num: arr)
        {
            answer.push_back(num*k);
        }
    }
    else
    {
        for(int num: arr)
        {
            answer.push_back(num + k);
        }
    }
    return answer;
}