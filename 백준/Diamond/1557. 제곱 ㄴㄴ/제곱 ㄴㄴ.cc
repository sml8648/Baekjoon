#include <bits/stdc++.h>
using namespace std;
const int KMAX = 1'000'000'000;
const int NMAX = 2*KMAX;
const int MAX = 50000;

int is_composite[MAX];
int sign[MAX];
vector<int> primes;

void get_sieve(int n) {
    for (int i = 2; i < n; i++) {
        if (!is_composite[i]) 
            primes.push_back(i);
        for (int j = i+i; j < n; j+=i) {
            is_composite[j] = 1;
        }
    }
}

void sign_precompute(int n) {
    memset(sign, -1, sizeof(sign));
    sign[1] = 1;
    for (int i = 2; i < n; i++) {
        for (int j = 2; j * j <= i; j++) {
            if (i % (j * j) == 0) {
                sign[i] = 0;
                break;
            }
        }
        if (sign[i] == 0) continue;
        int cnt = 0;
        int x = i;
        for (int j = 0; j < primes.size() && primes[j] <= x; j++) {
            if (x % primes[j] == 0) {
                cnt++;
                x /= primes[j];
            }
        }
        if (cnt % 2 == 0) sign[i] = 1;
    }
}

int Q(int x) {
    int ans = 0;
    for (int i = 1; i * i <= x; i++) {
        ans += sign[i] * (x / (i * i));
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    get_sieve(MAX);
    sign_precompute(MAX);
    int K; cin >> K;
    int s = 1, e = K*2, ans = e;
    while (s <= e) {
        int m = s + (e - s) / 2;
        if (Q(m) < K) s = m + 1;
        else e = m - 1, ans = m;
    }
    cout << ans;
}