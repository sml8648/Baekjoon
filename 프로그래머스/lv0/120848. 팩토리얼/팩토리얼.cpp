#include <string>
#include <vector>
#include <iostream>

using namespace std;

int factorial(int num)
{   
    int result = 1;
    for(int i = 1;i <= num; i++)
    {
        result = result*i;
    }
    
    return result;
}


int solution(int n) {
    
    int answer = 0;
    
    answer = factorial(10);
    
    for(int i = 0;i <= 11;i++)
    {   
        
        if(n < factorial(i))
        {
            answer = i - 1;
            break;
        }
    }
    
    return answer;
}