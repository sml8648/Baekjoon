#include <vector>

std::vector<int> solution(std::vector<int> arr, std::vector<std::vector<int>> intervals) {
    std::vector<int> result;

    for (auto& interval : intervals) {
        result.insert(result.end(), arr.begin() + interval[0], arr.begin() + interval[1] + 1);
    }

    return result;
}
