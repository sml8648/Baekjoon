#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int size = arr.size();
    int targetSize = 1;
    
    // targetSize를 2의 거듭제곱으로 만듦
    while (targetSize < size) {
        targetSize *= 2;
    }

    // arr의 크기가 targetSize가 되도록 0 추가
    arr.resize(targetSize, 0);

    return arr;
}