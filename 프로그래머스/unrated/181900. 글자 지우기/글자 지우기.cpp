#include <string>
#include <vector>
#include <algorithm>

std::string solution(std::string my_string, std::vector<int> indices) {
    // indices를 내림차순으로 정렬
    std::sort(indices.begin(), indices.end(), std::greater<int>());

    // 각 인덱스에 해당하는 글자를 지움
    for (int index : indices) {
        my_string.erase(index, 1);
    }

    return my_string;
}
