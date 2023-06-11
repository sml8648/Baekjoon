#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

std::vector<std::string> solution(std::vector<std::string> strArr) {
    for (int i = 0; i < strArr.size(); ++i) {
        if (i % 2 == 0) {
            std::transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::tolower);
        } else {
            std::transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::toupper);
        }
    }
    return strArr;
}