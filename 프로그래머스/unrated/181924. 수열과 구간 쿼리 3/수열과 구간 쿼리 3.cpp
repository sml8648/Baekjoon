#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    
    for(auto num: arr)
    {
        answer.push_back(num);
    }
    
    for(auto query : queries)
    {
        int tmp = answer[query[0]];
        answer[query[0]] = answer[query[1]];
        answer[query[1]] = tmp;
    }
    
    return answer;
}