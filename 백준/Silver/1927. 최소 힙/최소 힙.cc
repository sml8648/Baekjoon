#include <iostream>
#include <queue>
using namespace std;
int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	priority_queue<int, vector<int>, greater<int>> pq;

	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		
		if (!n && pq.empty())
			cout << 0 << '\n';
		else if (!n)
		{
			cout << pq.top() << '\n';
			pq.pop();
		}
		else
			pq.push(n);
	}
	return 0;

}