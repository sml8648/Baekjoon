#include <string>
#include <vector>

using namespace std;

int solution(vector<int> date1, vector<int> date2) {
    
    int first = date1[0]*365 + date1[1]*24 + date1[2];
    int second = date2[0]*365 + date2[1]*24 + date2[2];
    
    if(first < second)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
}