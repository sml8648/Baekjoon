#include <string>
#include <unordered_map>

using namespace std;

long long solution(string numbers) {
    // 각 문자열에 대응하는 숫자 매핑
    unordered_map<string, int> numberMap = {
        {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5},
        {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}, {"zero", 0}
    };
    
    long long answer = 0;
    string currentString = "";
    for (char c : numbers) {
        currentString += c;
        if (numberMap.find(currentString) != numberMap.end()) {
            // 현재 문자열이 숫자에 대응하는 경우, answer에 추가
            answer = answer * 10 + numberMap[currentString];
            currentString = "";
        }
    }
    return answer;
}