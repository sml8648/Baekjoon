#include <iostream>
#include <queue>
using namespace std;
int main(void)
{
	int t;
	cin >> t;
	while (t)
	{
		t--;
		int k, n;
		cin >> k;
		cin >> n;

		queue<pair<int, int>> q;
		priority_queue<pair<int, int>> pq;

		for (int i = 0; i < k; i++)
		{
			int s;
			cin >> s;
			q.push(make_pair(s, i));
			pq.push(make_pair(s, i));
		}

		int count = 0;
		while (1)
		{
			while (q.front().first != pq.top().first)
			{
				int a = q.front().first;
				int b = q.front().second;

				q.pop();
				q.push(make_pair(a, b));
			}

			count++;
			if (q.front().second == n)
			{
				cout << count << endl;
				break;
			}
			q.pop();
			pq.pop();
		}
	}
}