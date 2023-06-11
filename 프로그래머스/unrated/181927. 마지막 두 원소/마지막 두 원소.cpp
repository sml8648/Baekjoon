#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    
    int idx = num_list.size();
    bool flag = true;
    
    if(num_list[idx-1] > num_list[idx-2])
    {
        for(auto num : num_list)
        {
            answer.push_back(num);
        }
        answer.push_back(num_list[idx-1] - num_list[idx-2]);
    }
    else
    {
        for(auto num : num_list)
        {
            answer.push_back(num); 
        }
        answer.push_back(num_list[idx-1]*2);
    }
    
    return answer;
}