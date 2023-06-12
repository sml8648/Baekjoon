#include <string>
#include <vector>
#include <sstream>

std::vector<int> solution(std::string myString) {
    std::vector<int> result;
    std::stringstream ss(myString);
    std::string segment;

    while (std::getline(ss, segment, 'x')) {
        result.push_back(segment.size());
    }

    // Append a 0 if the last character of the string is 'x'
    if (myString.back() == 'x') {
        result.push_back(0);
    }

    return result;
}