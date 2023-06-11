#include <string>
#include <algorithm>

int solution(std::string myString, std::string pat) {
    // 문자열을 모두 소문자로 변환
    std::transform(myString.begin(), myString.end(), myString.begin(), ::tolower);
    std::transform(pat.begin(), pat.end(), pat.begin(), ::tolower);

    // myString의 부분 문자열 중 pat과 일치하는 부분이 있는지 확인
    if (myString.find(pat) != std::string::npos) {
        return 1;  // 일치하는 부분이 있으면 1 반환
    } else {
        return 0;  // 일치하는 부분이 없으면 0 반환
    }
}