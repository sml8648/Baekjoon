#include <vector>
#include <algorithm>

std::vector<int> solution(std::vector<int> num_list, int n) {
    std::rotate(num_list.begin(), num_list.begin() + n, num_list.end());
    return num_list;
}
