#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> Computer[101];
int checked[101];

int bfs(int start)
{
	int count = 0;
	queue<int> infection;
	infection.push(start);
	checked[start] = 1;
	while (infection.size())
	{
		int k = infection.front();
		infection.pop();
		for (int i = 0; i < Computer[k].size(); i++)
		{
			if (checked[Computer[k][i]] == 0)
			{
				infection.push(Computer[k][i]);
				checked[Computer[k][i]] = 1;
				count++;
			}
		}
	}

	return count;
}

int main(void)
{

	int t;
	cin >> t;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int Com1, Com2;
		cin >> Com1 >> Com2;
		Computer[Com1].push_back(Com2);
		Computer[Com2].push_back(Com1);
	}

	cout << bfs(1);

}