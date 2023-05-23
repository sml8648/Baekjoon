#include <vector>
#include <algorithm>

std::vector<int> solution(std::vector<int> num_list) {
    std::sort(num_list.begin(), num_list.end());

    num_list.erase(num_list.begin(), num_list.begin() + 5);

    return num_list;
}