#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int number, int n, int m) {
    
    int a = number % n;
    int b = number % m;
    
    if (a == 0 and b == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}