#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    vector<vector<int>> answer;
    
    vector<int> bucket;
    int count = 0;
    while(count < num_list.size())
    {
        bucket.push_back(num_list[count]);
        if((count+1) % n == 0)
        {
            answer.push_back(bucket);
            bucket.clear();
        }
        
        count += 1;
    }
    
    return answer;
}