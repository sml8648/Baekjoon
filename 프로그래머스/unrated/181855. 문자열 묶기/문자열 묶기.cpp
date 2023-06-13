#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<string> strArr) {
    unordered_map<int, int> countMap;

    // 각 문자열의 길이를 카운트
    for (string str : strArr) {
        int length = str.length();
        countMap[length]++;
    }

    int maxCount = 0;
    for (auto pair : countMap) {
        int count = pair.second;
        if (count > maxCount) {
            maxCount = count;
        }
    }

    return maxCount;
}