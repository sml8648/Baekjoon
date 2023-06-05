#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int multi = 1;
    int summation = 0;
    for(auto num:num_list)
    {
        multi *= num;
        summation += num;
    }
    
    if (multi < (summation*summation))
    {
        answer = 1;
    }
    
    return answer;
}