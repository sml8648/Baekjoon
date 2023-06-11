#include <string>

std::string solution(std::string str1, std::string str2) {
    std::string result = "";
    for (int i = 0; i < str1.size(); i++) {
        result += str1[i];
        result += str2[i];
    }
    return result;
}
