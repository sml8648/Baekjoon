#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;

	vector<int> v;

	while (t--)
	{
		int n;
		cin >> n;
		v.emplace_back(n);
	}

	sort(v.begin(), v.end());

	for (auto a : v)
	{
		cout << a << '\n';
	}
}