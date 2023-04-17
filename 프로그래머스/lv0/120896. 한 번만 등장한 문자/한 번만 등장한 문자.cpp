#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    map<char, int> char_count; // 문자별 등장 횟수를 저장하는 맵
    vector<char> result_vec; // 결과 문자열을 저장하는 벡터

    // 문자열 s를 순회하며 각 문자의 등장 횟수를 카운트
    for (char c : s) {
        char_count[c]++;
    }

    // 등장 횟수가 1인 문자들을 사전 순으로 result_vec 벡터에 추가
    for (auto p : char_count) {
        if (p.second == 1) {
            result_vec.push_back(p.first);
        }
    }

    // 결과 문자열을 사전 순으로 정렬
    sort(result_vec.begin(), result_vec.end());

    // 정렬된 문자들을 문자열로 변환하여 반환
    return string(result_vec.begin(), result_vec.end());
}