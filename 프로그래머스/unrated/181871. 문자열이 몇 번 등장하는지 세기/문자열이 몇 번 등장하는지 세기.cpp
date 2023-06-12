#include <string>

int solution(std::string myString, std::string pat) {
    int count = 0;
    size_t pos = 0;
    while((pos = myString.find(pat, pos)) != std::string::npos) {
        ++count;
        ++pos;
    }
    return count;
}
