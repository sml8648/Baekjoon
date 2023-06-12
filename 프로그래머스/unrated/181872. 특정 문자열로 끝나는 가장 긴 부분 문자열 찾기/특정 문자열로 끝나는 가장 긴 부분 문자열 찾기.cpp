#include <string>

std::string solution(std::string myString, std::string pat) {
    // find the last occurrence of pat in myString
    size_t found = myString.rfind(pat);

    // if pat is not found in myString, return empty string
    if (found == std::string::npos) {
        return "";
    }

    // return the longest substring that ends with pat
    return myString.substr(0, found + pat.size());
}
