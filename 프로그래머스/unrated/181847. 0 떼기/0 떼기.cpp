#include <string>

std::string solution(std::string n_str) {
    return n_str.substr(n_str.find_first_not_of('0'));
}
