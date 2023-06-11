#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int n) {
    int len = arr.size();
    vector<int> result(arr);
    
    for (int i = 0; i < len; i++) {
        if (len % 2 == 1 && i % 2 == 0) {
            result[i] += n;
        } else if (len % 2 == 0 && i % 2 == 1) {
            result[i] += n;
        }
    }
    
    return result;
}