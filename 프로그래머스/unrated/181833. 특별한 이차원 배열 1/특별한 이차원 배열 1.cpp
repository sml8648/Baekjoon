#include <vector>

std::vector<std::vector<int>> solution(int n) {
    // Initialize n x n matrix with all zeros
    std::vector<std::vector<int>> arr(n, std::vector<int>(n, 0));
  
    // Set the elements on the main diagonal to 1
    for(int i = 0; i < n; i++) {
        arr[i][i] = 1;
    }
  
    return arr;
}
