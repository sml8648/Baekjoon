#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, int k) {
    vector<int> answer;
    
    for(int i = 0;i < n;i++)
    {
        if ((i+1) % k == 0)
        {
            answer.push_back(i+1);
        }
    }
    return answer;
}