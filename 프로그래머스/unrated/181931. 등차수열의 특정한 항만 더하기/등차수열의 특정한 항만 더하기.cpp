#include <vector>

int solution(int a, int d, std::vector<bool> included) {
    int result = 0;

    for (int i = 0; i < included.size(); i++) {
        if (included[i]) {
            // 등차수열의 i+1항을 계산하여 더함
            result += a + d * i;
        }
    }

    return result;
}
