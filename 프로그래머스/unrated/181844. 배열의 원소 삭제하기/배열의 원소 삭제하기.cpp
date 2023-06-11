#include <vector>
#include <unordered_map>

std::vector<int> solution(std::vector<int> arr, std::vector<int> delete_list) {
    std::unordered_map<int, bool> delete_map;
    std::vector<int> result;

    // populate the map with delete_list items
    for (const auto& item : delete_list) {
        delete_map[item] = true;
    }

    // iterate through arr and only keep the elements not in delete_map
    for (const auto& item : arr) {
        if (delete_map.find(item) == delete_map.end()) {
            result.push_back(item);
        }
    }

    return result;
}







