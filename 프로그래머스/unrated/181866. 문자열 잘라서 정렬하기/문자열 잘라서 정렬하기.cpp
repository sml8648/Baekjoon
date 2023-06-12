#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

std::vector<std::string> solution(std::string myString) {
    std::vector<std::string> result;
    std::istringstream ss(myString);
    std::string buffer;

    while (std::getline(ss, buffer, 'x')) {
        if (!buffer.empty()) {
            result.push_back(buffer);
        }
    }

    std::sort(result.begin(), result.end());

    return result;
}
