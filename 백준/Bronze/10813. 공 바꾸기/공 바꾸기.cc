#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> balls(N);
    for (int i = 0; i < N; i++) {
        balls[i] = i + 1;
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        swap(balls[a - 1], balls[b - 1]);
    }

    for (int i = 0; i < N; i++) {
        cout << balls[i] << ' ';
    }
    cout << endl;

    return 0;
}