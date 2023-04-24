#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int n) {
    
    sort(array.begin(), array.end());
    
    int answer = 0;
    int max_abs_diff = 99999;
    
    for(int i = 0; i < array.size();i++)
    {
        int current_abs = abs(array[i] - n);
        if(current_abs < max_abs_diff)
        {
            answer = array[i];
            max_abs_diff = current_abs;
        }
    }
    return answer;
}