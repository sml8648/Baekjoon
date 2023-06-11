#include <string>
#include <algorithm>
#include <cctype>

std::string solution(std::string my_string, std::string alp) {
    std::transform(my_string.begin(), my_string.end(), my_string.begin(),
                   [alp](unsigned char c) { return (c == alp[0]) ? std::toupper(c) : c; });
    return my_string;
}
